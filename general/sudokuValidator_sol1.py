# Given a sudoku board (complete or incomplete) check whether the current state of the board is valid

# Sudoku board is a 9X9 board which can hold numbers from 1-9. Any other number on that board is invalid

# RULES
# 1. No row or column should have numbers 1-9 repeated
# 2. No designated 3X3 block within the board should have numbers 1-9 repeated

# Example
# [
#   [ 8, -1, -1, 4, -1, 6, -1, -1, 7],
#   [-1, -1, -1, -1, -1, -1, 4, -1, -1],
#   [-1, 1, -1, -1, -1, -1, 6, 5, -1],
#   [5, -1, 9, -1, 3, -1, 7, 8, -1],
#   [-1, -1, -1, -1, 7, -1, -1, -1, -1],
#   [-1, 4, 8, -1, 2, -1, 1, -1, 3],
#   [-1, 5, 2, -1, -1, -1, -1, 9, -1],
#   [-1, -1, 1, -1, -1, -1, -1, -1, -1],
#   [3, -1, -1, 9, -1, 2, -1, -1, 5]
# ]

BLANK_CELL = "."


def is_valid_block(board, row, col):
    """
    Ensure the second rule of Sudoku is valid.
    No designated 3X3 block within the board should have numbers 1-9 repeated
    """
    nums_seen = set()

    for i in range(row, row + 3):
        for j in range(col, col + 3):
            # if the number have been seen before, then it fails rule 2
            if board[i][j] in nums_seen:
                return False

            if board[i][j] != BLANK_CELL:  # if the number is not blank
                nums_seen.add(board[i][j])  # add the number in the nums_seen set
    return True


def is_valid_cell(orig_cell, target):
    if orig_cell == BLANK_CELL:  # the cell is just not filled yet
        return True

    # ensure the cells filled is valid
    if orig_cell == target:
        return False
    return True


def is_valid_row_and_col(board, row, col):
    cell_value = board[row][col]
    new_row = row + 1  # row to use for compare
    new_col = col + 1  # col to be used to compare

    # ensure there's no duplicate data in same row different column
    while new_col < len(board):
        # if any data in that column match is duplicate
        if not is_valid_cell(cell_value, board[row][new_col]):
            return False
        new_col += 1

    # ensure there's no duplicate data in same column different row
    while new_row < len(board):
        # check for duplicate
        if not is_valid_cell(cell_value, board[new_row][col]):
            return False
        new_row += 1

    return True


def is_valid_sudoku(board):
    for i in range(len(board)):
        nums_viewed = set()
        for j in range(len(board)):
            cell_value = board[i][j]
            # found duplicate value
            if cell_value in nums_viewed:
                return False
            # ensure there's no duplicate data in the rows and columns
            if not is_valid_row_and_col(board, i, j):
                return False

            # get the 3x3 matrice position
            row_3x3 = i if i % 3 == 0 else -1
            col_3x3 = j if j % 3 == 0 else -1

            # check the 3x3 matrix if valid
            if row_3x3 >= 0 and col_3x3 >= 0:
                if not is_valid_block(board, row_3x3, col_3x3):
                    return False

            # add to the number view set
            if board[i][j] != BLANK_CELL:
                nums_viewed.add(board[i][j])
    return True


if __name__ == "__main__":
    board1 =[
        ["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    board2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    board3 = [
        [".", ".", ".", ".", "5", ".", ".", "1", "."],
        [".", "4", ".", "3", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "3", ".", ".", "1"],
        ["8", ".", ".", ".", ".", ".", ".", "2", "."],
        [".", ".", "2", ".", "7", ".", ".", ".", "."],
        [".", "1", "5", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "2", ".", ".", "."],
        [".", "2", ".", "9", ".", ".", ".", ".", "."],
        [".", ".", "4", ".", ".", ".", ".", ".", "."]
    ]

    board4 = [
        ["1", "2", "3", "4", "5", "6"],
        ["2", "3", "1", "5", "6", "4"],
        ["3", "1", "2", "6", "4", "5"],
        ["4", "6", "5", "3", "2", "1"],
        ["5", "4", "6", "1", "3", "2"],
        ["6", "5", "4", "2", "1", "3"],
    ]

    boards = [board1, board2, board3, board4]

    for board in boards:
        print(is_valid_sudoku(board))