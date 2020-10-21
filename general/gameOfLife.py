# A cell in a matrix can be alive or dead and change its state based on the below conditions
# a cell is a block in a matrix surrounded by neighbours. A cell can be in two states, alive or dead.
# A cell can change its state from one generation to another under certain circumstances.
# RULES
#   1. A live cell with fewer than 2 live neighbours dies of loneliness
#   2. A dead cell with exactly 2 live neighbours comes alive
#   3. A live cell with greater than 2 live neighbours dies due to overcrowding

# alive = 1
# dead = 0

# Need to keep track of what cells have change between the two generations

# cells = 2D N X N matrix

# Example:
# First generation matrix
#     [0, 1, 0, 0, 0]
#     [1, 1, 1, 0, 0]
#     [0, 0, 0, 0, 0]
#     [0, 0, 0, 1, 0]
#     [0, 0, 0, 1, 0]

# Next generation
#     [0, 0, 0, 0, 0]
#     [1, 0, 1, 0, 0]
#     [1, 0, 0, 1, 0]
#     [0, 0, 1, 0, 1]
#     [0, 0, 1, 0, 1]

def print_cells(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            print(matrix[row][col], end=" ")
        print()


def get_cell_state(matrix, row, col):
    no_alive_neighbors = 0

    # check neighbors on same column
    if row > 0:
        no_alive_neighbors += matrix[row - 1][col]
    if row + 1 < len(matrix):
        no_alive_neighbors += matrix[row + 1][col]
    # check neighbor on same row
    if col > 0:
        no_alive_neighbors += matrix[row][col - 1]
    if col + 1 < len(matrix):
        no_alive_neighbors += matrix[row][col + 1]

    # check left down diagonal
    if row + 1 < len(matrix) and col > 0:
        no_alive_neighbors += matrix[row + 1][col - 1]
    # check left up diagonal
    if row > 0 and col > 0:
        no_alive_neighbors += matrix[row - 1][col - 1]

    # check right up diagonal
    if row > 0 and col + 1 < len(matrix):
        no_alive_neighbors += matrix[row - 1][col + 1]
    # check right down diagonal
    if row + 1 < len(matrix) and col + 1 < len(matrix):
        no_alive_neighbors += matrix[row + 1][col + 1]

    return 1 if no_alive_neighbors == 2 else 0


def next_gen(matrix):
    new_gen = []
    for row in range(len(matrix)):
        next_gen_row = []
        for col in range(len(matrix)):
            next_gen_cell = get_cell_state(matrix, row, col)
            # update the cell in next generation
            next_gen_row.append(next_gen_cell)
        new_gen.append(next_gen_row)
    return new_gen

if __name__ == "__main__":
    cells = [
        [0, 1, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0]
    ]

    new_gen = next_gen(cells)

    third_gen = next_gen(new_gen)

    print("Before")
    print_cells(cells)

    print("2nd generation")
    print_cells(new_gen)

    print("3rd generation")
    print_cells(third_gen)