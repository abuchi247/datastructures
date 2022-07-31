"""
File contains the Battleship game implementation
@author Abuchi Obiegbu
"""

import os
import random
import copy
import time
from typing import List, Tuple

# Constant values

LOGO = """
========================================
||   WELCOME TO OUR BATTLESHIP GAME   ||
========================================
"""

GAME_OPTIONS_LOGO = """
\tOptions:
\t\t 1. Start Game
\t\t 2. Exit 
"""

PLAYER_BOARD_LOGO = """
=====================================================================
||                        YOUR PLAY BOARD                          ||
||                            GUIDE                                ||
||            MISS = X, HIT = S, UNGUESSED SQUARES = O             ||
||   Ships are of length: 2 - 5 placed vertical or horizontal      ||
=====================================================================
"""

# Display values
SHIP_SIGN = "S"
MISS = "X"
PADDING = "   "
HIDDEN = "O"

BOARD_COLUMNS = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9
}

# Board information
GRID_WIDTH = 10
GRID_HEIGHT = 10
BOARD_DIMENSION = (GRID_WIDTH, GRID_HEIGHT)
BOARD_ROWS = [x for x in range(1, 11)]
BOARD_HEADER = header = PADDING + f" {PADDING.join(list(BOARD_COLUMNS.keys()))}"
ALLOWED_SHIP_POSITION = ["horizontal", "vertical"]
# set to keep track of computer guesses
COMPUTER_GUESSES = set()


##################################
# CUSTOM EXCEPTION SECTION
##################################
class ShipIntersectException(Exception):
    """
    Ship Intersect Exception
    """
    pass


class InvalidRowSelectionException(Exception):
    """
    Invalid row selection exception
    """
    pass


class InvalidColumnSelectionException(Exception):
    """
    Invalid column selection exception
    """
    pass


##################################
# CLASS SECTION
##################################
class Ship:
    """
    A class to represent a ship.

    ...

    Attributes
    ----------
    name : str
        name of the ship
    length : int
        length of the ship
    position : set
        position of the ship
    hit_coordinates : set
        hit coordinates on the ship
    """

    def __init__(self, name: str, length: int, position: set, hit_coordinates: set):
        """
        Constructs all the necessary attributes for the ship object.

        Parameters
        ----------
            name : str
                name of the ship
            length : int
                length of the ship
            position : set
                position of the ship
            hit_coordinates : set
                hit coordinates on the ship
        """
        self.name = name
        self.length = length
        self.position = position
        self.hit_coordinates = hit_coordinates


class BattleShipBoard:
    """
    A class to represent a battleship board.

    ...

    Attributes
    ----------
    width : int
        width of the board
    height : int
        height of the board

    Methods
    -------
    show_board(show_private_board=False):
        Prints the board to standard output.

    is_all_ship_sunk():
        Check if all the ships on the board have been sunk.

    is_ship(row, column):
        Check if there's a ship at the row and column on the board.

    set_guess(row, column, pin):
        Set a pin on the board at the row and column

    place_ships_on_grid():
        Place all the ships in a random position on the board in a horizontal or vertical position

    __place_ship_horizontal(row, current_ship):
        Place a ship in a horizontal position while ensuring that the ship fits in that row

    __place_ship_vertical(column, current_ship):
        Place a ship in a vertical position while ensuring that the ship fits in that column

    __is_valid_horizontal_placement(row, column, ship_length):
        Check if the specified ship length can fit horizontally on the board in the row and column
        
    __is_valid_vertical_placement(row, column, ship_length):
        Check if the specified ship length can fit vertically on the board in the row and column

    """

    def __init__(self, width: int, height: int) -> None:
        """
        Constructs all the necessary attributes for the battleship board object.

        Parameters
        ----------
            width : int
                width of the board
            height : int
                height of the board
        """
        self.width = width
        self.height = height
        # create board grid where ships are placed
        self.__grid = [[HIDDEN] * width for _ in range(height)]
        # create board to be view on screen with game play
        self.__play_board = copy.deepcopy(self.__grid)
        # create available ship list
        self.ships = generate_ships()
        # keep track of number of ships sunk
        self.num_sunk_ships = 0
        # place ships on the board grid
        self.place_ships_on_grid()

    def show_board(self, show_private_board: bool = False) -> None:
        """
        Prints the play board to the standard output.

        If the argument 'show_private_board' is passed, then it will display the board with the player ships visible.

        Parameters
        ----------
        show_private_board : bool, optional
            Decide to show player private board or play board (default is False = show play board)

        Returns
        -------
        None
        """
        # constructing board display
        output: List[str] = [BOARD_HEADER]

        # deciding on which board to display
        board = self.__grid if show_private_board else self.__play_board

        # populate board for viewing
        for index, row in enumerate(board):
            output.append(f"{index + 1:^3d} {PADDING.join([column for column in row])}")

        # display board on screen
        print("\n".join(output))

    def is_all_ship_sunk(self) -> bool:
        """
        Check if all the ships on the board have been sunk.

        Returns
        -------
        True if all ships are sunk otherwise, False
        """
        return self.num_sunk_ships == len(self.ships)

    def is_ship(self, row: int, column: int) -> bool:
        """
        Check if there's a ship at the row and column on the board.
        
        Parameters
        ----------
        row : int
            Row on the board
        column : int
            Column on the board

        Returns
        -------
        True if a ship was found in that position otherwise, False
        """

        return self.__grid[row][column] == SHIP_SIGN

    def set_guess(self, row: int, column: int, pin: str) -> None:
        """
        Set a pin on the play board at the row and column.

        Parameters
        ----------
        row : int
            Row on the board
        column : int
            Column on the board
        pin: str
            Pin to be displayed on board. X for miss and S for ship hit

        Returns
        -------
        None
        """
        self.__play_board[row][column] = pin

    def place_ships_on_grid(self) -> None:
        """
        Place all the ships in a random position on the board in a horizontal or vertical position.
        
        Rules to be followed:
        1. Ships are all 1 square wide and the player gets 1 each of length 2, 3, 4, and 5.
        2. Ships can only be placed in a horizontal or vertical and cannot intersect.

        Returns
        -------
        None
        """
        # Go through all the ship on the ship list
        for ship in self.ships:
            while True:
                try:
                    # pick a placement for the ship by random - horizontal or vertical
                    ship_placement = random.choice(ALLOWED_SHIP_POSITION)
                    # place ship horizontally
                    if ship_placement == ALLOWED_SHIP_POSITION[0]:
                        # select a random row
                        row = random.randint(0, self.height - 1)
                        # place ship horizontally
                        self.__place_ship_horizontal(row, ship)
                        break
                    else:
                        # select a random column
                        column = random.randint(0, self.width - 1)
                        # place ship vertically
                        self.__place_ship_vertical(column, ship)
                        break
                # Placing current ship at a given position caused a ship overlap.
                # Trying again
                except ShipIntersectException:
                    continue

    def __place_ship_horizontal(self, row: int, current_ship: Ship) -> None:
        """
        Place a ship in a horizontal position while ensuring that the ship fits in that row.
        
        Parameters
        ----------
        row : int
            Row on the board where to place ship
        current_ship : Ship
            current ship to be placed

        Returns
        -------
        None
        """
        # get a random column on the grid that can accommodate current ship's length
        column = random.randint(0, self.width - current_ship.length - 1)
        # check if ship can be place horizontally without intercepting with other ships
        if not self.__is_valid_horizontal_placement(row=row, column=column, ship_length=current_ship.length):
            raise ShipIntersectException(f"{current_ship.name} cannot be placed horizontally on ({row}, {column}) "
                                         f"position")

        # place ship on grid
        for i in range(column, column + current_ship.length):
            # draw ship on board
            self.__grid[row][i] = SHIP_SIGN
            # add ship coordinates (row, column) to the ship position set
            current_ship.position.add((row, i))

    def __place_ship_vertical(self, column: int, current_ship: Ship) -> None:
        """
        Place a ship in a vertical position while ensuring that the ship fits in that column.

        Parameters
        ----------
        column : int
            column on the board where to place ship
        current_ship : Ship
            current ship to be placed

        Returns
        -------
        None
        """
        # get a random row on the grid that can accommodate current ship's length
        row = random.randint(0, self.height - current_ship.length - 1)
        # check if ship can be place vertically without intercepting with other ships
        if not self.__is_valid_vertical_placement(row=row, column=column, ship_length=current_ship.length):
            raise ShipIntersectException(f"{current_ship.name} cannot be placed vertically on ({row}, {column}) "
                                         f"position")

        # place ship on grid
        for i in range(row, row + current_ship.length):
            # draw ship on board
            self.__grid[i][column] = SHIP_SIGN
            # add ship coordinates (row, column) to the ship position set
            current_ship.position.add((i, column))

    def __is_valid_horizontal_placement(self, row: int, column: int, ship_length: int) -> bool:
        """
        Check if the specified ship length can fit horizontally on the board in the row and column.

        Parameters
        ----------
        row : int
            Row on the board
        column : int
            Column on the board
        ship_length : int
            Size of current ship

        Returns
        -------
        True if there are no ship interception, otherwise, False
        """
        # upper limit in order for ship to fit horizontally
        upper_limit = column + ship_length
        # go through the columns
        for i in range(column, upper_limit):
            # Checks for overlap with other ships
            if self.__grid[row][i] == SHIP_SIGN:
                return False
        return True

    def __is_valid_vertical_placement(self, row: int, column: int, ship_length: int) -> bool:
        """
        Check if the specified ship length can fit vertically on the board in the row and column.

        Parameters
        ----------
        row : int
            Row on the board
        column : int
            Column on the board
        ship_length : int
            Size of current ship

        Returns
        -------
        True if there are no ship interception, otherwise, False
        """
        # upper limit in order for ship to fit vertically
        upper_limit = row + ship_length
        # go through the rows
        for i in range(row, upper_limit):
            # Checks for overlap with other ships
            if self.__grid[i][column] == SHIP_SIGN:
                return False
        return True


class Player:
    """
    A class to represent a player.

    ...

    Attributes
    ----------
    name : str
        name of the player
    board : BattleShipBoard
        instance of battleship board
    """

    def __init__(self, name):
        self.name = name
        self.board = BattleShipBoard(*BOARD_DIMENSION)


class BattleShipGame:
    """
    A class to represent a two player battleship game.

    ...
    Attributes
    ----------
    players : List[Player]
        list of player - user and computer

    Methods
    -------
    create_players():
        creates the user and computer players.

    start_game():
        Starts the battleship game.

    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the battleship game object.
        """
        # create the players
        self.players = create_players()

    def start_game(self):
        """
        Start the battleship game until a player wins

        Returns
        -------
        None
        """
        count = 0

        while True:
            # calculate index of current player
            current_player_index = count % len(self.players)
            # deciding current player and opponent
            current_player = self.players[current_player_index]
            opponent = self.players[int(not current_player_index)]

            # decide current player and opponent
            if turn(current_player, opponent):
                # check if the game over
                if opponent.board.is_all_ship_sunk():
                    print(f"Congratulations! Player {current_player.name!r} won!")
                    print("GAME OVER!!!")
                    break

            # Adding 2 seconds sleep to all user see report
            time.sleep(2)
            count += 1


##################################
# HELPER FUNCTION SECTION
##################################
# clear console
clear_console = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def create_players() -> List[Player]:
    """
    Create the battleship player list - 1 user and computer player.

    Returns
    -------
    List of player objects
    """
    return [
        Player("Player 1"),
        Player("Computer")
    ]


def generate_ships() -> List[Ship]:
    """
    Generate list of supported ships and populate the ship attributes.

    Returns
    -------
    List of ship objects
    """
    ships = [
        Ship(name="patrol_boat", length=2, position=set(), hit_coordinates=set()),
        Ship(name="submarine", length=3, position=set(), hit_coordinates=set()),
        Ship(name="battleship", length=4, position=set(), hit_coordinates=set()),
        Ship(name="carrier", length=5, position=set(), hit_coordinates=set())

    ]
    return ships


def validate_row_selection(row_selected: int) -> None:
    """
    Ensures the selected row is valid

    Parameters
    ----------
    row_selected : int
        Row guessed

    Returns
    -------
    None
    """
    # raise exception when the row is not valid
    if row_selected not in set(BOARD_ROWS):
        raise InvalidRowSelectionException(f"row selected is invalid")


def validate_column_selection(column_selected: str) -> None:
    """
    Ensures the selected column is valid

    Parameters
    ----------
    column_selected : int
        Column guessed

    Returns
    -------
    None
    """
    # raise exception when the column is not valid
    if column_selected not in BOARD_COLUMNS.keys():
        raise InvalidColumnSelectionException(f"column selected is invalid")


def make_computer_guess():
    """
    Make a guess for the computer

    RULE:
        Make a random selection for the computer and ensuring it doesn't select the same square twice

    Returns
    -------
    row_guessed, col_guessed : Tuple[int, str]
        Row and column guessed
    """
    # keep guessing until you pick a select that wasn't guessed by the computer in the past
    while True:
        row_guessed = random.choice(BOARD_ROWS)
        col_guessed = random.choice(list(BOARD_COLUMNS.keys()))
        coordinates = f"{col_guessed}{row_guessed}"
        # make sure computer doesn't guess the same square again
        if coordinates not in COMPUTER_GUESSES:
            COMPUTER_GUESSES.add(coordinates)
            break
        else:
            continue
    return row_guessed, col_guessed


def read_or_generate_guess(player) -> Tuple[int, str]:
    """
    Read the user guess from keyboard

    Parameters
    ----------
    player : Player
        current player instance
        
    Returns
    -------
    row_guessed, col_guessed : Tuple[int, str]
        Row and column guessed
    """
    error_message = "Invalid Selection"
    if player.name.lower() == "computer":
        return make_computer_guess()

    while True:
        help_str = "Allowed choices: rows = 1-10, columns = A-J"
        try:
            print(help_str)
            user_input = input("Make your selection your guess in format (ex. A1): ")
            col_guessed = user_input[0].upper()
            row_guessed = int(user_input[1:])
            # print(col_guessed, row_guessed)
            # validate row selection
            validate_row_selection(row_guessed)

            # validate column selection
            validate_column_selection(col_guessed)

            return row_guessed, col_guessed
        # there was an invalid selection
        except (IndexError, TypeError, ValueError, InvalidColumnSelectionException, InvalidRowSelectionException):
            print(error_message)
            continue


def turn(current_player: Player, opponent: Player) -> bool:
    """
    Responsible for allowing a player make a selection

    Parameters
    ----------
    current_player : Player
        current player instance

    opponent : Player
        opponent player instance

    Returns
    -------
    True if there was a hit or sunk ship action otherwise false
    """
    print()
    if current_player.name.lower() != "computer":
        clear_console()
        print(PLAYER_BOARD_LOGO)
        # display a opponent board
        opponent.board.show_board()
    print(f"Current player: {current_player.name!r}")
    row_guessed, col_guessed = read_or_generate_guess(current_player)
    print(f"\tGuessed: {col_guessed}{row_guessed}")
    return place_guess_and_report_status(opponent, row_guessed, col_guessed)


def place_guess_and_report_status(opponent: Player, row_guessed: int, column_guessed: str) -> bool:
    """
    Places current player's guess and report status on player's board - hit or miss or sunk ship

    Following rules: After the user selects a square, the computer informs them of the result.
    1. If the square has no ship, it was a miss.
    2. If the square has a ship that has not been hit, it was a hit.
    3. When the user hits all the squares of the ship, they have sunk the ship.
    4. When they have sunk all the opponents' ships, they win. The user should be allowed to
        hit the same square twice.

    Parameters
    ----------
    opponent : Player
        opponent player instance

    row_guessed : int
        Row guessed

    column_guessed : str
        Column guessed

    Returns
    -------
    True if there was a hit or sunk ship action otherwise false
    """
    # convert row and column guessed into integer
    row_selected = row_guessed - 1  # board number is actually starting from 0 index
    column_selected = BOARD_COLUMNS[column_guessed]  # converting selected column from alphabet to number

    guessed_coordinate = (row_selected, column_selected)

    # player selected a spot without a ship
    if not opponent.board.is_ship(row_selected, column_selected):
        # place a miss pin on board
        opponent.board.set_guess(row_selected, column_selected, pin=MISS)
        print("Sorry, It was a miss!")
        return False

    # place a ship sign on the board
    opponent.board.set_guess(row_selected, column_selected, pin=SHIP_SIGN)
    # find the ship at the coordinate specified
    for ship in opponent.board.ships:
        # checking which ship was hit
        if guessed_coordinate in ship.position:
            if guessed_coordinate not in ship.hit_coordinates:
                # add the ship to the hit coordinates for the current hit ship
                ship.hit_coordinates.add(guessed_coordinate)
                # if the ship has not been hit before only then you report a hit
                if len(ship.hit_coordinates) == 1:
                    print(f"It was a hit {ship.name!r}!")
                # did we sink a ship? all ship square were hit
                if len(ship.hit_coordinates) == ship.length:
                    print(f"Congrats, You sunk a ship {ship.name!r}!")
                    opponent.board.num_sunk_ships += 1
            return True


def ask_to_play() -> None:
    """
    Ask the user if they want to play

    Returns
    -------
    None
    """

    while True:
        try:
            # Clear screen
            clear_console()
            # display logo
            print(LOGO)
            print(GAME_OPTIONS_LOGO)
            user_input = int(input("Make a choice: "))
            if user_input == 1:
                break
            if user_input == 2:
                print("Exiting!!!")
                exit()
            else:
                continue
        except (ValueError, TypeError):
            continue


def main():
    """
    Start Program
    """
    ask_to_play()
    # Clear screen
    clear_console()
    game = BattleShipGame()
    game.start_game()


if __name__ == "__main__":
    main()
