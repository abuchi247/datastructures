#
# - This is a command line, text-only game to simulate battleship against an easy computer opponent.
#
# - The game is played between 2 players, who each have a 10x10 grid with columns A-J and rows 1-10
#
# - Ships are all 1 square wide and the player gets 1 each of length 2, 3, 4, and 5.
#
# - The user types a command to start battleship game and the computer lays out the ships for both players. Ships can only be horizontal or vertical and cannot intersect.
#
# - The players alternate turns and pick a coordinate to fire upon during each turn.
#
# - After the user selects a square, the computer informs them of the result. If the square has no ship, it was a miss. If the square has a ship that has not been hit, it was a hit. When the user hits all of the squares of the ship, they have sunk the ship. When they have sunk all of the opponents' ships, they win. The user should be allowed to hit the same square twice.
#
# - The computer is an easy opponent: it needs only to make a random selection from the squares it has not selected.
#
# - Displaying the board graphically is not required.
#
# - The purpose of this exercise is to demonstrate program design and code readability with a program that is relatively quick to implement. A pretty user interface is not required.

# Requirements
# 1. 2 player game each have 10 x 10 grid with A - J columns and rows 1 - 10
#       So is the opponent the computer? or another player?
#       Each play will have its own grid board?
# 2. Ships are all 1 square wide, with length 2, 3, 4 and 5? Do you mean that all the sizes are equal more like a square. For example
# if the ship was of length 3, it's going to occupy a 3x3 grid on the board?

# Inputs:
#   User type a command to START battleship game
#          Computer lays out the ships for both players. Ships can only be horizontal or vertical and cannot intersect
#   Both players alternate turns and picks a coordinate to fire upon during each turn
#   After the user selects a square, the computer informs them of the result.
#     if the square has no ship, it was a miss. If the square has a ship that has not been hit, it was a hit. When the
#     user hits all the squares of the ship, they have sunk the ship. When they have sunk all the opponents ships, they
#     win. The user should be allowed to hit the same square twice.
#   The computer is an easy opponent: it needs only to make a random selections from the squares it has not selected.

import random
import copy

COLUMNS = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9
}

SHIP_SIGN = "S"
SHIP_HIT = "X"
BOARD_DIMENSION = (6, 6)


class Ship:
    def __init__(self, name, length,  coordinates, hit_coordinates):
        self.name = name
        self.length = length
        self.coordinates = coordinates
        self.hit_coordinates = hit_coordinates


def generate_ships():
    """
    Populate ships
    """
    return [
        Ship(name="patrol_boat", length=2, coordinates=set(), hit_coordinates=set()),
        Ship(name="submarine", length=3, coordinates=set(), hit_coordinates=set()),
        Ship(name="battleship", length=4, coordinates=set(), hit_coordinates=set()),
        Ship(name="carrier", length=5, coordinates=set(), hit_coordinates=set())

    ]

SHIPS = generate_ships()

SHIPS_AND_COORDS = {}

POSSIBLE_PLACEMENTS = ["horizontal", "vertical"]


def populate_board(rows, cols):
    """
    Generate the board
    """
    board = []
    for row in range(rows):
        board.append(["O"] * cols)
    return board


def _display_board(board):
    """
    Display the board to user
    """
    header = f"{'r/c':4s}{' '.join(list(COLUMNS.keys())[:len(board)])}"
    print(header)
    for row_no in range(len(board)):
        print(f"{row_no + 1:3d} {' '.join(board[row_no])}")
    # print(header)


def is_valid_placement_row(board, row, col, size):
    """
    Check if the new ship can fit horizonally using the current coordinates and
     ensures there's no ship overlap.
    """
    for i in range(row, row + size):
        # Checks for overlap with other ships
        if board[i][col] == SHIP_SIGN:
            return False
    return True


def is_valid_placement_column(board, row, col, size):
    """
    Check if the new ship can fit vertically using the current coordinates and
     ensures there's no ship overlap.
    """
    for i in range(col, col + size):
        # Checks for overlap with other ships
        if board[row][i] == SHIP_SIGN:
            return False
    return True


def place_ship_horizontal(board, row, col, new_ship):
    """
    Places ship horizontal on the grid
    """
    upper_bound = new_ship.length
    for i in range(col, col + upper_bound):
        # if the number have been seen before, then it fails rule 2
        board[row][i] = SHIP_SIGN
        # add coordinate to the ship coordinates in the form of (row, column)
        new_ship.coordinates.add((row, i))


def place_ship_vertical(board, row, col, new_ship):
    """
    Places ship vertically on the grid
    """
    upper_bound = new_ship.length
    for i in range(row, row + upper_bound):
        # if the number have been seen before, then it fails rule 2
        board[i][col] = SHIP_SIGN
        # add coordinate to the ship coordinates in the form of (row, column)
        new_ship.coordinates.add((i, col))


def get_random_row(board, upper_bound=0):
    """
    Get a random row number on the board
    """
    upper_limit = (len(board) - upper_bound) - 1
    return random.randint(0, upper_limit)


def get_random_col(board, upper_bound=0):
    """
    Get a random column number on the board
    """
    upper_limit = (len(board[0]) - upper_bound) - 1
    return random.randint(0, upper_limit)


def place_ship(board, ship):
    """
    Place ship on the grid
    """
    while True:
        placement = random.choice(POSSIBLE_PLACEMENTS)
        # print(f"placement: {placement}")
        # horizontal placement
        if placement == POSSIBLE_PLACEMENTS[0]:
            row = get_random_row(board)
            col = get_random_col(board, upper_bound=ship.length)
            # check if the selected row/column meets the requirement of the ship size without overlapping
            if is_valid_placement_column(board, row=row, col=col, size=ship.length):
                place_ship_horizontal(board, row=row, col=col, new_ship=ship)
                break
        else:
            row = get_random_row(board, ship.length)
            col = get_random_col(board)
            # print(f"row: {row}, col: {col}, size: {size}")
            if is_valid_placement_row(board, row=row, col=col, size=ship.length):
                place_ship_vertical(board, row=row, col=col, new_ship=ship)
                break


def select_ship_position(ship):
    """
    Positions a ship in the board
    """
    possible_positions = ["vertical", "horizontal"]
    for i in range(10):
        print(COLUMNS.keys())
        print(random.choice(possible_positions))


def _place_ship_on_board(ships, board):
    """
    Places all the ships in a random position in the grid board
    """
    for ship in ships:
        place_ship(board, ship=ship)


def shoot_ship(opponent, x_coord: int, y_coord: int):
    """
    Selects a coordinate on the board
    """
    coordinates = (x_coord, y_coord)

    ship_hit = False

    # go through the opponent's ships to see if the coordinate matches any of his/her ship position
    for ship in opponent.ships:
        if coordinates in ship.coordinates:
            # update the hit coordinates
            ship.hit_coordinates.add(coordinates)
            if len(ship.hit_coordinates) == ship.length:
                print(f"{ship.name} was sunk")
            else:
                print(f"{ship.name} was hit")
            ship_hit = True
            break
    opponent.board_visible_to_opponent[x_coord][y_coord] = SHIP_HIT
    if not ship_hit:
        print("Ship was missed")


class Player:
    def __init__(self, name):
        self.name = name
        self.ships = generate_ships()
        self.__board_with_ships = populate_board(*BOARD_DIMENSION)
        self.board_visible_to_opponent = copy.deepcopy(self.__board_with_ships)
        # place ships in the board
        _place_ship_on_board(board=self.__board_with_ships, ships=self.ships)

    def get_num_of_sunk_ships(self):
        num_sunk_ships = 0
        for ship in self.ships:
            if len(ship.hit_coordinates) == ship.length:
                num_sunk_ships += 1
        return num_sunk_ships

    def display_personal_board(self):
        """
        Display player's personal board
        """
        _display_board(self.__board_with_ships)

    def display_board(self):
        """
        Display player's board visible to opponents
        """
        _display_board(self.board_visible_to_opponent)


def read_game_input(player, opponent):
    print(f"{player.name.capitalize()}'s turn")

    # Display the board
    opponent.display_board()

    # pick coordinates
    x_cord = int(input("Enter x cooridate: "))
    y_cord = int(input("Enter y cooridate: "))

    shoot_ship(opponent, x_cord-1, y_cord-1)

    opponent.display_board()



if __name__ == "__main__":
    oten = Player("Oten")
    abuchi = Player("Abuchi")

    count = 0
    while True:
        if count % 2 == 0:
            read_game_input(oten, abuchi)
        else:
            read_game_input(abuchi, oten)
        count += 1




    # for ship in oten.ships:
    #     print(f"{ship.name}, coordinates: {ship.coordinates}, hit_coordinates: {ship.hit_coordinates}")
    #
    # for ship in abuchi.ships:
    #     print(f"{ship.name}, coordinates: {ship.coordinates}, hit_coordinates: {ship.hit_coordinates}")

    # for ship in SHIPS:
    #     print(f"{ship.name}, coordinates: {ship.coordinates}, hit_coordinates: {ship.hit_coordinates}")
    # exit()
