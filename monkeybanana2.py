from poodle import Object, schedule
from typing import Set

class Position(Object):
    #def __init__(self, locname=None):
        #self.locname = locname
        
    def __str__(self):
        if not hasattr(self, "locname"):return "unknown"
        return self.locname
        #return self.locname or "unknown"

class HasHeight(Object):
    height: int

class HasPosition(Object):
    at: Position

class Monkey(HasHeight, HasPosition):
    pass

class PalmTree(HasHeight, HasPosition):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = 2

class Box(HasHeight, HasPosition):
    pass

class Banana(HasHeight, HasPosition):
    owner: Monkey = None
    attached: PalmTree = None

class World(object):
    def __init__(self):
        self.locations: Set[Position] = set()

    def add_location(self, position: Position):
        self.locations.add(position)

# Create World and positions
w = World()
p1 = Position("Position A")
p2 = Position("Position B")
p3 = Position("Position C")

w.add_location(p1)
w.add_location(p2)
w.add_location(p3)

# Create Monkey, Box, PalmTree, and Banana
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

# Define actions
def go(monkey: Monkey, where: Position):
    assert where in w.locations
    assert monkey.height < 1, "Monkey can only move while on the ground"
    monkey.at = where
    return f"Monkey moved to {where}"

def push(monkey: Monkey, box: Box, where: Position):
    assert monkey.at == box.at
    assert where in w.locations
    assert monkey.height < 1, "Monkey can only move while on the ground"
    box.at = where
    return f"Monkey moved box to {where}"

def climb_up(monkey: Monkey, box: Box):
    assert monkey.at == box.at
    monkey.height += box.height
    return "Monkey climbs the box"

def grasp(monkey: Monkey, banana: Banana):
    assert monkey.height == banana.height
    assert monkey.at == banana.at
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

# Run the plan
actions = [go, push, climb_up, grasp, infer_banana_height, infer_owner_at]
objects = [w, p1, p2, p3, m, box, p, b]
goal = lambda: b.owner == m

result = schedule(actions, objects, goal)
print('\n'.join(x() for x in result))
