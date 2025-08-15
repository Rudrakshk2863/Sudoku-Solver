import numpy as np

def check_empty(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return row, col
    return None

sudoku = [
 [0, 0, 0, 0, 0, 0, 0, 0, 3],
 [6, 5, 0, 0, 7, 0, 0, 0, 2],
 [0, 0, 2, 0, 5, 0, 0, 9, 0],
 [0, 6, 4, 8, 0, 0, 0, 2, 1],
 [2, 0, 1, 0, 0, 0, 9, 8, 0],
 [8, 0, 0, 2, 3, 0, 6, 0, 0],
 [7, 8, 0, 3, 0, 5, 0, 0, 0],
 [0, 0, 6, 0, 0, 9, 1, 3, 0],
 [3, 0, 0, 4, 2, 6, 0, 0, 9]
]


def put_number(sudoku, row, col, num):
    # Check if number exists in the same row
    for c in range(9):
        if sudoku[row][c] == num:
            return False

    # Check if number exists in the same column
    for r in range(9):
        if sudoku[r][col] == num:
            return False

    # Check in the 2x2 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if sudoku[r][c] == num:
                return False

    return True

def sudoku_solver(sudoku):
    if check_empty(sudoku) is None:
        return True  # sudoku is solved

    row, col = check_empty(sudoku)

    for num in range(1, 10):
        if put_number(sudoku, row, col, num):
            sudoku[row][col] = num

            if sudoku_solver(sudoku):
                return True

            sudoku[row][col] = 0  # backtrack

    return False

if sudoku_solver(sudoku):
    for row in sudoku:
        print(row)
else:
    print("No solution exists")