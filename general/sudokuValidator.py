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

# have a list to keep track of what value I've seen
def is_valid_sudoku(board):
    blank = -1
    upper_bound = len(board)
    not_complete = False

    for i in range(upper_bound):
        nums_seen = set()
        for j in range(upper_bound):
            current = board[i][j]
            row = i + 1
            col = j + 1
            if current == blank:    # empty entry
                not_complete = True
                continue
            # there's an entry in the board
            # ensure the entry is not in the nums_seen set
            if current in nums_seen:
                return False
            while row < upper_bound:   # check the entry in the same column but different row
                if board[row][j] == current:
                    return False
                row += 1

            # check entries on same row but different column
            while col < upper_bound:
                if board[i][col] == current:
                    return False
                col += 1
            # add that data to the seen set
            nums_seen.add(current)

    return True if not not_complete else False


if __name__ == "__main__":
    board = [
        [1, 2, 3, 4, 5, 6],
        [2, 1, 4, 5, 6, 3],
        [2, 1, 4, 5, 6, 3],
        [3, 1, 2]
    ]

    print(is_valid_sudoku(board))