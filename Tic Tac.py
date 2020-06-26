row_order = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]  # current state of tic tac toe board, bottom to top row
player_list = ["X", "O"]
turn = player_list[0]  # set first player to "X"
row_win_sequences = ["", "", ""]  # "XXX" or "OOO" in any element = a win horizontally for one of the players
col_win_sequences = ["", "", ""]  # "XXX" or "OOO" in any element = a win vertically for one of the players
diagonal_win_sequences = ["", ""]  # "XXX" or "OOO" in any element = a win diagonally for one of the players


def print_board():
    print(9 * "-")
    print(f"| {' '.join(row_order[2])} |")
    print(f"| {' '.join(row_order[1])} |")
    print(f"| {' '.join(row_order[0])} |")
    print(9 * "-")


def update_board():
    # update board representation (row_order elements order is the reverse of next_move entries (less 1))
    row_order[int(next_move[1]) - 1][int(next_move[0]) - 1] = turn
    # update win sequences for later count (if 3 "X"s in any element, X wins; if 3 "O"s, then O wins)
    row_win_sequences[int(next_move[1]) - 1] += turn  # updates status of X and O sequences across the board
    col_win_sequences[int(next_move[0]) - 1] += turn  # updates status of X and O sequences down the board
    if next_move == ["2", "2"]:  # a move in the centre of the board counts for both diagonal sequences
        diagonal_win_sequences[0] += turn
        diagonal_win_sequences[1] += turn
    # update diagonal sequence for a top left or bottom right move
    elif next_move[0] == next_move[1]:
        diagonal_win_sequences[0] += turn
    # update diagonal sequence for a top right or bottom left move
    elif (next_move == ["1", "3"]) or (next_move == ["3", "1"]):
        diagonal_win_sequences[1] += turn

print_board()

while True:
    next_move = input("Enter the coordinates: ").split()
    # check valid input
    if not(next_move[0].isdecimal() and next_move[1].isdecimal):
        print("You should enter numbers!")
    elif 3 < max(int(next_move[0]), int(next_move[1])):
        print("Coordinates should be from 1 to 3!")
    elif row_order[int(next_move[1]) - 1][int(next_move[0]) - 1] in ("X", "O"):
        print("This cell is occupied! Choose another one!")
    # valid input actions
    else:
        update_board()
        print_board()
        # check for win/draw
        if any([row_win_sequences.count(turn * 3), col_win_sequences.count(turn * 3), diagonal_win_sequences.count(turn * 3)]):
            print(turn, "wins")
            break
        elif not any([group.count("_") for group in row_order]):
            print("Draw")
            break
        # swap player symbol, ready for next turn
        else:
            turn = player_list[abs(player_list.index(turn) - 1)]


