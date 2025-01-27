from typing import Set

class Object:
    def __init__(self):
        pass

def schedule(actions, objects, goal):
    for action, args in actions:
        result = action(*args)
        if result:
            print(result)
        if goal():
            return
    print("Goal not achieved")

class Position(Object):    
    def __init__(self, locname):
        self.locname = locname

    def __str__(self):
        return self.locname

class HasHeight(Object):
    def __init__(self):
        self.height: int

class HasPosition(Object):
    def __init__(self):
        self.at: Position

class Monkey(HasHeight, HasPosition):
    pass

class PalmTree(HasHeight, HasPosition):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = 2

class Box(HasHeight, HasPosition):
    pass

class Banana(HasHeight, HasPosition):
    def __init__(self):
        self.owner: 'Monkey' = None
        self.attached: 'PalmTree' = None

class World(object):
    def __init__(self):
        self.locations: Set[Position] = set()

    def add_location(self, position: Position):
        self.locations.add(position)

w = World()
p1 = Position("Position A")
p2 = Position("Position B")
p3 = Position("Position C")

w.add_location(p1)
w.add_location(p2)
w.add_location(p3)

m = Monkey()
m.height = 0
m.at = p1

box = Box()
box.height = 2
box.at = p2

p = PalmTree()
p.at = p3

b = Banana()
b.attached = p

def go(monkey: Monkey, where: Position):
    assert where in w.locations
    assert monkey.height < 1, "Monkey can only move while on the ground"
    monkey.at = where
    return f"Monkey moved to {where}"

def push(monkey: Monkey, box: Box, where: Position):
    assert monkey.at == box.at, f"Monkey is not at the box's position {box.at}"
    assert where in w.locations
    assert monkey.height < 1, "Monkey can only move while on the ground"
    box.at = where
    return f"Monkey moved box to {where}"

def climb_up(monkey: Monkey, box: Box):
    assert monkey.at == box.at, "Monkey is not at the box"
    monkey.height += box.height
    return "Monkey climbs the box"

def grasp(monkey: Monkey, banana: Banana):
    assert monkey.height == banana.height, "Monkey is not at the right height"
    assert monkey.at == banana.at, "Monkey is not at the banana's position"
    banana.owner = monkey
    return "Monkey takes the banana"

def infer_owner_at(palmtree: PalmTree, banana: Banana):
    assert banana.attached == palmtree
    banana.at = palmtree.at
    return "Remembered that if the banana is on the palm tree, its location is where palm tree is"

def infer_banana_height(palmtree: PalmTree, banana: Banana):
    assert banana.attached == palmtree
    banana.height = palmtree.height
    return "Remembered that if the banana is on the palm tree, its height equals the tree's height"

actions = [
    (go, [m, p2]),               # Move the monkey to the box's location
    (push, [m, box, p3]),        # Push the box to the palm tree's location
    (go, [m, p3]),               # Move the monkey to the palm tree's location
    (climb_up, [m, box]),        # Climb up the box to reach the banana
    (infer_banana_height, [p, b]),# Infer the banana's height
    (infer_owner_at, [p, b]),    # Infer the banana's location
    (grasp, [m, b]),             # Take the banana
]

objects = [w, p1, p2, p3, m, box, p, b]
goal = lambda: b.owner == m

result = schedule(actions, objects, goal)
