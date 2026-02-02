board = [" "," "," ",
         " "," "," ",
         " "," "," "]



def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_win(player):
    possible_wins = [(0,1,2),(3,4,5),(6,7,8),                #check the winning by putting index to the board and match the signs X or O
                     (0,3,6),(1,4,7),(2,5,8),
                     (0,4,8), (2,4,6)]

    for a,b,c in possible_wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False
moves = 0
choose_player = input("With Which Player Do You Want To Start With\nChoose X or O: ")
player = choose_player
while moves<9:
    show_board()
    pos = int(input("Player " + player + ", enter position (1-9): ")) - 1

    if board[pos] == " ":
        board[pos] = player
        moves +=1 #increments the move
    else:
        print("Position already taken!")
        continue

    if check_win(player): #function return true or false in case of a win!
        show_board()
        print("Player", player, "wins!")
        break

    if player == "X": #switches between players!
        player = "O"
    else:
        player = "X"
else:
    show_board()
    print("It's a draw!")
