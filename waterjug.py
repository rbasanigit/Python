from collections import deque

def water_jug(capacity, start, goal):
    queue = deque([start])
    visited = set([start])
    parent_map = {start:None}
    while queue:
        current_state = queue.popleft()
        if current_state == goal:
            return reconstruct_path(parent_map, start, goal)
        for next_state in generate_next_states(current_state, capacity):
            if next_state not in visited:
                visited.add(next_state)
                parent_map[next_state] = current_state
                queue.append(next_state)
    return None

def generate_next_states(state, capacity):
    next_states = []
    jug_count = len(state)
    for i in range(jug_count): 
        for j in range(jug_count):
            if i != j:
                new_state = list(state)
                transfer_amount = min(state[i], capacity[j] - state[j]) 
                new_state[i] -= transfer_amount
                new_state[j] += transfer_amount 
                next_states.append(tuple(new_state))
        new_state = list(state)
        new_state[i] = capacity[i] 
        next_states.append(tuple(new_state))
        
        new_state = list(start)
        new_state[i] = 0 
        next_states.append(tuple(new_state))
    return next_states

def reconstruct_path(parent_map, start, goal):
    path = []
    state = goal
    while state != start:
        path.append(state)
        state = parent_map[state]
    path.append(start) 
    path.reverse()
    return path

capacity = (8, 5, 3)
start = (0, 0, 0)
goal = (4, 4, 0)
solution = water_jug(capacity, start, goal)
if solution:
    print("Solution found!")
    for step in solution:
        print(step)
else:
    print("No solution found.")
        

