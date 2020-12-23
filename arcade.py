import random
import time
import os
from ascii_art import guess_number_graphic, tic_tac_toe_graphic

def tic_tac_toe():
    os.system('cls||clear')
    print("Welcome to the Tic Tac Toe Game!\nPlease follow the instructions carefully!")
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
    winner_statement = "\n*****Player %s Wins!!!! Yay!*****\nWant a hint in escaping? Enter a secret code while you are looking at your inventory.\nNow, go find the code!"

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
        os.system('cls||clear')
        print("Welcome to the Tic Tac Toe Game!\nPlease follow the instructions carefully!")
        print("\nHere is your board!\nYou are X and Sean the computer is O.\n")
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
        if rabbit_foot == True:
            print("Computer's Turn!")
            time.sleep(3)
            os.system('cls||clear')
            print("Welcome to the Tic Tac Toe Game!\nPlease follow the instructions carefully!")
            print("\nHere is your board!\nYou are X and Sean the computer is O.\n")
        
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
            if rabbit_foot == False:
                user_input = input("Press ENTER to continue")
                os.system('cls||clear')
        #Changing player so messages will be correct
            if player == 1:
                player = 2
            else:
                player = 1

    #Someone has won or board is full:
    if i == 8:
        print("\n*****It's a cat! You guys are evenly matched!*****\nPlease play again!\n\n")
        user_input = input("Press ENTER to continue")
        os.system('cls||clear')
    else:
        print("\n\tPlease play again!\n\n")
        user_input = input("Press ENTER to continue")
        os.system('cls||clear')


# tetris board

# tetris pieces
# long_line = 

# def tetris():
#     SIZE = 15
#     board = []
#     for y in range(SIZE):
#         board.append([])        
#         for x in range(SIZE):
#             board[y].append(" ")


def number_guess():
    os.system('cls||clear')
    guess_number_graphic()
    print("I am thinking of a number between 1 and 100.")
    n = 1
    secret_number = random.randint(1, 100)
    while n <= 5:
        while True:
            try: 
                user_guess = int(input(f"\nAttempt {n}/5: "))
                break
            except ValueError:
                print("Please pick a number between 1 & 100?")
        n +=1
        if user_guess < secret_number:
            print(f"\nNope! You lose! Just kidding, {user_guess} is too low!")
        elif user_guess > secret_number:
            print(f"\nNo Way! {user_guess} is too big!")
        while n > 5 or user_guess == secret_number:
            if user_guess == secret_number:
                print("\nYou got it! You get a gold star!\n\nAnd a secret code!") 
                time.sleep(3)
                print("\nFor help escaping, call Ryan!\nSecret Code: 041221") 
            elif n > 5:
                print(f"\nToo many tries! You lose!\nMy number was: {secret_number}!")    
            new_game = input("\n\nPress ENTER to continue")
            os.system('cls||clear')
            return False
            # if new_game.upper() == "Y":
            #     n = 1
            #     secret_number = random.randint(1, 100)
            #     print("\nI am thinking of a number between 1 and 100.")
            #     break
            # else:
            #     print("Thanks for playing!")
            #     n = 6
            #     break