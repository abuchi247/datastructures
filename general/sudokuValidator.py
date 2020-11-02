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


def is_valid_block(board):
    """
    Ensure the second rule of Sudoku is valid.
    No designated 3X3 block within the board should have numbers 1-9 repeated
    """
    block_list = []

    # have an integer set associated with whether a number occurs in that block or not
    for _ in range(9):
        block_list.append(set())

    for row_block in range(3):
        for col_block in range(3):
            # iterate through each cell in the block
            for mini_row in range(3):
                for mini_col in range(3):
                    # This calculation gives us the actual cell in the sudoku board
                    # Since each block is a 3x3 block and the mini rows and columns are
                    # rows and columns in that block that moves us to the right row and
                    # right cell within it
                    row = row_block * 3 + mini_row
                    col = col_block * 3 + mini_col

                    cell_value = board[row][col]
                    # If no value has been assigned to a cell then continue, don't perform check
                    if cell_value == BLANK_CELL:
                        continue

                    if int(cell_value) < 0 or int(cell_value) > 9:
                        return False

                    # get the actual block number = we have a total of 9 blocks
                    block_number = row_block * 3 + col_block

                    if cell_value in block_list[block_number]:
                        return False

                    block_list[block_number].add(cell_value)
    return True


def is_valid_rows_and_cols(board):
    """
    Time complexity of this O(N^2)
    Space complexity O(2N^2)
    :param board:
    :return:
    """
    # store the rows data and cols data in a list of sets
    row_list = []
    column_list = []

    # populate the row and column list with a empty sets
    for _ in range(9):
        row_list.append(set())
        column_list.append(set())

    # check the rows and columns if they are valid
    for row in range(len(board)):
        for col in range(len(board)):
            # get the value in the sudoku cell
            cell_value = board[row][col]

            # if no value is assigned continue. No need to perform check
            if cell_value == ".":
                continue

            # ensure the cell value is valid
            if int(cell_value) < 0 or int(cell_value) > 9:
                return False

            # check if the value have been seen before in row or col
            if cell_value in row_list[row]:
                return False

            if cell_value in column_list[col]:
                return False

            # add the value in the row and colume set
            row_list[row].add(cell_value)
            column_list[col].add(cell_value)

    return True


def is_valid_sudoku(board):

    # check if the sudoku board rows and columns are valid
    if not is_valid_rows_and_cols(board):
        return False

    if not is_valid_block(board):
        return False
    return True


if __name__ == "__main__":
    board1 =[
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
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
    boards = [board1]

    for board in boards:
        print(is_valid_sudoku(board))