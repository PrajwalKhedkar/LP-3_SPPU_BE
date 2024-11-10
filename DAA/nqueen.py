
def print_board(board):
    for row in board:
        result = ["Q" if col == 1 else "." for col in row]
        result_str = " ".join(result)
        print(result_str)
    print("\n")


def is_safe(board, row, col, n):
    # Check this column on upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i in range(row, -1, -1):
        for j in range(col, -1, -1):
            if board[i][j] == 1:
                return False

    # Check upper diagonal on right side
    for i in range(row, -1, -1):
        for j in range(col, n):
            if board[i][j] == 1:
                return False

    return True


def solve_n_queens(board, row, n, solutions):
    # Base case: If all Queens are placed, add solution
    if row >= n:
        solutions.append([row[:] for row in board])
        return

    # Try placing Queen in each column in the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place Queen
            # Recursive call to place the next Queen
            solve_n_queens(board, row + 1, n, solutions)
            # Backtrack by removing the Queen
            board[row][col] = 0


def n_queens_with_fixed_position(n, initial_row, initial_col):
    # Initialize an empty board
    board = [[0] * n for _ in range(n)]
    # Place the initial Queen
    board[initial_row][initial_col] = 1
    # List to store all valid solutions for the given initial position
    solutions = []
    # Start backtracking from the next row
    solve_n_queens(board, initial_row + 1, n, solutions)
    
    # Print all valid solutions with the initial Queen fixed
    if solutions:
        print(f"Possible solutions with the first Queen at ({initial_row}, {initial_col}):")
        for solution in solutions:
            print_board(solution)
    else:
        print(f"No solution exists with the first Queen at ({initial_row}, {initial_col}).")


# Example usage
n = 8  # Size of the board
initial_row, initial_col = 0, 0  # Position of the first Queen
n_queens_with_fixed_position(n, initial_row, initial_col)
