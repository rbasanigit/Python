from collections import deque

# Define the initial and goal states 
initial_state = ('L', 'L', 'L', 'L') 
goal_state = ('R', 'R', 'R', 'R')

# Define the constraints 
def is_valid(state):
    M, T, G, C = state
    if (T == G and M != T) or (G == C and M != G):
        return False
    return True

# Define the possible transitions 
def get_next_states(state):
    M, T, G, C = state 
    next_states = []
    # Man crosses alone 
    if M == 'L':
        next_states.append(('R', T, G, C)) 
    else:
        next_states.append(('L', T, G, C))
    # Man takes the tiger
    if M == T:
        if M == 'L':
            next_states.append(('R', 'R', G, C))
        else:
            next_states.append(('L', 'L', G, C))
    # Man takes the goat
    if M == G:
        if M == 'L':
            next_states.append(('R', T, 'R', C))
        else:
            next_states.append(('L', T, 'L', C))
    # Man takes the cabbage
    if M == C:
        if M == 'L':
            next_states.append(('R', T, G, 'R'))
        else:
            next_states.append(('L', T, G, 'L'))
    # Filter out invalid states
    valid_states = [state for state in next_states if is_valid(state)] 
    return valid_states

# Solve the puzzle using BFS 
def solve_puzzle():
    queue = deque([(initial_state, [])]) 
    visited = set()
    while queue:
        current_state, path = queue.popleft()
        if current_state in visited: 
            continue
        visited.add(current_state) 
        path = path + [current_state]
        if current_state == goal_state: 
            return path
        for next_state in get_next_states(current_state): 
            if next_state not in visited:
                queue.append((next_state, path))
    return None

# Print the solution 
solution = solve_puzzle() 
if solution:
    print("Solution found:") 
    for step in solution:
        print(step) 
else:
    print("No solution found.")
