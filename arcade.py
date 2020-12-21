import random

def tic_tac_toe():
    print("Welcome to Crystal's Tic Tac Toe Game!\nPlease follow the instructions carefully!")
    SIZE = 3
    board = []
    for y in range(SIZE):
        board.append([])        
        for x in range(SIZE):
            board[y].append("[%d][%d]" % (y, x))
    print("\nHere is your board!\nYou are X and Sean the computer is O.\n")

    for row in board:
        for column in row:
            print("%s  " % column, end="")
        print("\n")

    player_token = ["  X   ", "  O   "]

    player = 1

    error_number_message = "\n*******\nPlease enter a number between 0 and 2.\n*******"
    winner_statement = "\n*****Player %s Wins!!!! Yay!*****"

    rabbit_foot = True
    while rabbit_foot:
        print(f"\nPlayer {player}'s turn!\n")

        while True:
            try:
                row = int(input(f"\n***Player {player}***\nWhich row would you like to use (This is the first number [row] [column]?\n0, 1, or 2? "))
                if 0 <= row <= 2:
                    column = int(input("\nWhich column would you like to mark?\n0, 1, or 2? "))
                    if 0 <= column <= 2:
                        if board[row][column] in player_token:
                            print("\n*****\nThat space is already taken. Try again!\n*****")
                        else:
                            break
                    else:
                        print(error_number_message)
                else:
                    print(error_number_message) 
            except ValueError:
                print(error_number_message)
        
        board[row][column] = player_token[player - 1]
        print("\n")
        for row in board:
            for column in row:
                print("%s  " % column, end="")
            print("\n")
    #checking for wins! if rabbitfoot is false, it will end the loop
        for i in range(SIZE):#checking rows
            if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
                print(winner_statement % player)
                rabbit_foot = False
                break
        for i in range(SIZE):#checking columns
            if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
                print(winner_statement % player)
                rabbit_foot = False
                break
        #checking diagnals...
        if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            print(winner_statement % player)
            rabbit_foot = False
            break
        elif board[2][0] == board[1][1] and board[2][0] == board[0][2]:
            print(winner_statement % player)
            rabbit_foot = False
            break

    #Changing player so messages will be correct
        if player == 1:
            player = 2
        else:
            player = 1

    #Computer's Turn!
        while True:
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            if board[row][column] in player_token:
                pass
            else:
                break
        
        board[row][column] = player_token[player - 1]
        print("\n")
        for row in board:
            for column in row:
                print("%s  " % column, end="")
            print("\n")
    #checking for wins! if rabbitfoot is false, it will end the loop
        for i in range(SIZE):#checking rows
            if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
                print(winner_statement % player)
                rabbit_foot = False
                break
        for i in range(SIZE):#checking columns
            if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
                print(winner_statement % player)
                rabbit_foot = False
                break
        #checking diagnals...
        if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            print(winner_statement % player)
            rabbit_foot = False
            break
        elif board[2][0] == board[1][1] and board[2][0] == board[0][2]:
            print(winner_statement % player)
            rabbit_foot = False
            break
    #Changing player so messages will be correct
        if player == 1:
            player = 2
        else:
            player = 1

    #Someone has won or board is full:
    if i == 8:
        print("\n*****It's a cat! You guys are evenly matched!*****\nPlease play again!\n\n")
    else:
        print("\n\tPlease play again!\n\n")


# tetris board

# tetris pieces
long_line = 

def tetris():
    SIZE = 15
    board = []
    for y in range(SIZE):
        board.append([])        
        for x in range(SIZE):
            board[y].append(" ")

tic_tac_toe()