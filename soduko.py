def print_sudoku(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_valid_move(board, row, col, num):
    # Check if the number is not present in the same row or column
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False

    # Check if the number is not present in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(board):
    row, col = find_empty_location(board)

    # If there is no empty location, the puzzle is solved
    if row is None:
        return True

    # Try placing a number in the empty location
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num

            # Recursively attempt to solve the rest of the puzzle
            if solve_sudoku(board):
                return True

            # If the current placement doesn't lead to a solution, backtrack
            board[row][col] = 0

    # No valid number found for the current empty location
    return False

# Example usage:
initial_state = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Make a copy of the initial state to keep it unchanged
final_state = [row[:] for row in initial_state]

# Solve the Sudoku puzzle using backtracking
if solve_sudoku(final_state):
    print("Sudoku solved successfully:")
    print_sudoku(final_state)
else:
    print("No solution exists.")


