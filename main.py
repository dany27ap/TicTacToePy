bord = [ "-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True

winner = None

current_player = "X"

def display_bord():
    print(bord[0] + " | " + bord[1] + " | " + bord[2])
    print(bord[3] + " | " + bord[4] + " | " + bord[5])
    print(bord[6] + " | " + bord[7] + " | " + bord[8])


def play_game():
    #Dispaly initial board
    display_bord()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    #The game has ended
    if winner == "X" or winner == "0":
        print("Winner is " + winner)
    elif winner == None:
        print("Tie")


def handle_turn(player):
    print(player + " turn ")
    position = input("Choose a position from 1-9: ")


    position = int(position) - 1

    bord[position] = player
    display_bord()

def check_if_game_over():
    check_if_win()

    check_if_tie()


def check_if_win():
    global winner

    row_winner = check_rows()
    column_winner = check_rows()
    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
    return
def check_if_tie():
    global game_still_going
    if "-" not in bord:
        game_still_going = False
    return

def check_rows():
    global game_still_going
    row_1 = bord[0] == bord[1] == bord[2] != "-"
    row_2 = bord[3] == bord[4] == bord[5] != "-"
    row_3 = bord[6] == bord[7] == bord[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return bord[0]
    elif row_2:
        return bord[3]
    elif row_3:
        return bord[7]

    return

def check_columns():
    global game_still_going
    column_1 = bord[0] == bord[3] == bord[6] != "-"
    column_2 = bord[1] == bord[4] == bord[7] != "-"
    column_3 = bord[2] == bord[5] == bord[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return bord[0]
    elif column_2:
        return bord[1]
    elif column_3:
        return bord[2]
    return

def check_diagonals():
    global game_still_going
    diagonal_1 = bord[0] == bord[4] == bord[8] != "-"
    diagonal_2 = bord[2] == bord[4] == bord[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return bord[0]
    elif diagonal_2:
        return bord[2]
    return

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "0"
    elif current_player == "0":
        current_player = "X"
    return

play_game()


#board
#display board
#play game
#handle turn
#check win
    #check row
    #check columms
    #check diagonals
#check tie
#flip player