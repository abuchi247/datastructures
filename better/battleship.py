
def generate_ship_pos(pos1, pos2):
    # A1, A3
    # same column
    if pos1[0] == pos2[0]:
        if int(pos1[1]) in col_map and int(pos2[1]) in col_map:
            if abs(int(pos2[1]) - int(pos1[1])) == 2:
                min_pos = min(pos1, pos2)
                max_pos = max(pos1, pos2)
                missing_pos = min_pos[0] +  str(int(min_pos[1]) + 1)
                return min_pos, missing_pos, max_pos
    # same row
    if pos1[1] == pos2[1]:
        if pos1[0] in row_map and pos2[0] in row_map:
            if abs(row_map.index(pos2[0]) - row_map.index(pos1[0])) == 2:
                min_pos = min(pos1, pos2)
                max_pos = max(pos1, pos2)
                # letter = row_map[row_map.index(min_pos[0]) + 1]
                missing_letter = chr(ord(min_pos[0]) + 1)
                missing_pos = missing_letter + str(min_pos[1])
                return min_pos, missing_pos, max_pos
    return None


def populate_board():
    board = []

    for i in range(6):
        row = []
        for j in range(6):
            row.append('.')
        board.append(row)
    return board


def update_board(board, pos, action):
    row = row_map.index(pos[0])
    col = col_map.index(int(pos[1]))

    if board[row][col] != ".":
        return -1
    if action == "hit":
        board[row][col] = 'X'
        return 0
    else:
        board[row][col] = 'O'
        return 0

def play(playerOneShips, playerTwoGuesses):
    # Write your code here

    MAX_GUESS = 10
    entered_guess = len(playerTwoGuesses)
    playerOneShipInput = playerOneShips.split()

    if len(playerOneShipInput) % 2 != 0:
        print("Invalid!")
        return
    num_ships = len(playerOneShipInput) // 2

    # Invalid play one input. We can only enter 3 ships at max
    if len(playerOneShipInput) > 6:
        print("Invalid!")
        return

    ships = []
    unique_ships = set()

    for x in range(0, len(playerOneShipInput), 2):
        print(f"{playerOneShipInput[x]}, {playerOneShipInput[x+1]}")
        cordinates = generate_ship_pos(playerOneShipInput[x], playerOneShipInput[x+1])
        if not cordinates:
            print("Invalid!")
            return
        ships.append(cordinates)

    for ship in ships:
        for pos in ship:
            if pos in unique_ships:
                print("Invalid")
                return
            else:
                unique_ships.add(pos)

    board = populate_board()
    from pprint import pprint

    print(f"Player One entered {num_ships} ships.")

    for player_guess in playerTwoGuesses:
        print()
        print(f"Player Two, you have {MAX_GUESS} guesses left. Board Status:")
        pprint(board)

        status = "miss"

        if player_guess in unique_ships:
            status = "hit"
            valid_input = update_board(board, player_guess, "hit")
        else:
            valid_input = update_board(board, player_guess, "miss")

        if valid_input == -1:
            print("Invalid!")
            return

        print(f"Player Two, please enter your guess: {player_guess}")
        print(f"That was a {status}!")
        MAX_GUESS -= 1


if __name__ == '__main__':
    row_map = ["A", "B", "C", "D", "E", "F"]
    col_map = [num for num in range(1, 7)]
    playerOneShips = "A3 A1 D5 F5 C2 A2"

    print(playerOneShips)

    playerTwoGuesses_count = int(6)

    playerTwoGuesses = []

    inputs = ["A2", "A3", "A4", "F4", "A1", "D5"]

    for _ in range(playerTwoGuesses_count):
        playerTwoGuesses_item = inputs[_]
        playerTwoGuesses.append(playerTwoGuesses_item)


    # play(playerOneShips, playerTwoGuesses)
    play(playerOneShips, playerTwoGuesses)