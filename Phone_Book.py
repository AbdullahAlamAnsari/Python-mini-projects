board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_win(player):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in win_conditions:
        print(a)
        print(b)
        print(c)
        if board[a] == board[b] == board[c] == player:
            return True
    return False

player = "X"

for turn in range(9):
    show_board()
    pos = int(input("Player " + player + ", enter position (1-9): ")) - 1

    if board[pos] == " ":
        board[pos] = player
    else:
        print("Position already taken!")
        continue

    if check_win(player):
        show_board()
        print("Player", player, "wins!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"
else:
    show_board()
    print("It's a draw!")
