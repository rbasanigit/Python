N = 8  
# Function to check if a queen can be placed at board[row][col]
def isSafe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

# Recursive utility function to solve the problem using backtracking
def solveQueens(board, col):
    # If all queens are placed
    if col >= N:
        return True

    # Consider this column and try placing a queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col):
            # Place this queen
            board[i][col] = 1

            # Recursively place the rest of the queens
            if solveQueens(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, remove it (backtrack)
            board[i][col] = 0

    # If the queen can't be placed in any row for this column, return False
    return False

# Function to solve the N-Queens problem
def solutionQueens():
    board = [[0 for _ in range(N)] for _ in range(N)]  # Initialize the chessboard

    if not solveQueens(board, 0):
        print("Solution does not exist")
        return False

    # Print the solution
    for row in board:
        print(" ".join(str(x) for x in row))
    return True

if __name__ == "__main__":
    solutionQueens()
