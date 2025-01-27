import heapq

class State:
    def __init__(self, board, parent = None, move = "", depth = 0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.size = int(len(board) ** 0.5)
        
    def goal(self):
        return self.board == list(range(1, self.size**2)) + [0]
    
    def manhdist(self):
        dist = 0
        for i, val in enumerate(self.board):
            if val != 0:
                trow = (val - 1) // self.size
                tcol = (val - 1) % self.size
                currrow = i // self.size
                currcol = i % self.size
                dist += abs(currrow - trow) + abs(currcol - tcol)
        return dist
    
    def gensuccessors(self):
        def swappos(board, pos1, pos2):
            board = board[:]
            board[pos1], board[pos2] = board[pos2], board[pos1]
            return board
        
        neighbors = []
        zero_index = self.board.index(0)
        zero_row, zero_col = zero_index // self.size, zero_index % self.size
        moves = {
            "Up": (zero_row - 1, zero_col),
            "Down": (zero_row + 1, zero_col),
            "Left": (zero_row, zero_col - 1),
            "Right": (zero_row, zero_col + 1)
        }
        for move, (new_row, new_col) in moves.items():
            if 0 <= new_row < self.size and 0 <= new_col < self.size:
                new_index = new_row * self.size + new_col
                new_board = swappos(self.board, zero_index, new_index)
                neighbors.append(State(new_board, self, move, self.depth + 1))
        return neighbors
    
    def __lt__(self, other):
        return self.manhdist() < other.manhdist()
    
    def __repr__(self):
        return str(self.board)

def bfs(initial_board):
    inistate = State(initial_board)
    queue = []
    heapq.heappush(queue, (inistate.manhdist(), inistate))
    visstates = set()
    
    while queue:
        _, currstate = heapq.heappop(queue)
        
        if currstate.goal():
            return currstate
        
        visstates.add(tuple(currstate.board))
        
        for successor in currstate.gensuccessors():
            if tuple(successor.board) not in visstates:
                heapq.heappush(queue, (successor.manhdist(), successor))
    
    return None

def reconstruct_path(state):
    path = []
    while state.parent is not None:
        path.append(state.move)
        state = state.parent
    return path[::-1]

initial_board = [1, 2, 3, 4, 0, 5, 6, 7, 8]
solution = bfs(initial_board)

if solution:
    print("Solution found!")
    path = reconstruct_path(solution)
    print(f"Moves: {' -> '.join(path)}")
    print("Final board configuration:")
    print(solution.board)
else:
    print("No solution found.")
