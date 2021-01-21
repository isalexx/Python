# Program Name: Triplets
# Date: March 13, 2020
# Programmer: Alex Dorodko
#Plays a game which is based on life cells, and life forms.

import random

def gameoflife():
    #setting up the 20x20 board
    board = []

    for i in range(0, 20):
        board.append([])
        for j in range(0, 20):
            board[i].append(".")


    #input for starting population
    cells = int(input("How many cells would you like to start the game with?: "))

    #replacing the random cells on the board
    for i in range (0, cells):
        rand_col = random.randint(0, 19)
        rand_row = random.randint(0, 19)
        board[rand_col][rand_row] = "O"

    generation = 0
    continue_game = ""

    while (continue_game != 2):
        board2 = []
        print("----- Generation", generation, "-----")
        generation += 1

        for i in range(0, 20):
            for j in range (0, 20):
                print(board[i][j], end="")
            print("")

        continue_game = int(input("\n1 - Advance one generation ahead.\n2 - Exit game\n"))
        while (continue_game != 1 and continue_game != 2):
            continue_game = int(input("\Invalid selection.\n1 - Advance one generation ahead.\n2 - Exit game\n"))


        if (continue_game == 1):
            for i in range(0, 20):
                board2.append([])
                for j in range(0, 20):
                    neighbours = 0
                    board2[i].append('.')
                    if (i > 0 and j > 0):
                        if (board[i - 1][j - 1] == "O"):
                            neighbours += 1
                    if (i > 0):
                        if (board[i - 1][j] == "O"):
                            neighbours += 1
                    if (i > 0 and j < 19):
                        if (board[i - 1][j + 1] == "O"):
                            neighbours += 1
                    if (j > 0):
                        if (board[i][j - 1] == "O"):
                            neighbours += 1
                    if (j < 19):
                        if (board[i][j + 1] == "O"):
                            neighbours += 1
                    if (i < 19 and j > 0):
                        if (board[i + 1][j] == "O"):
                            neighbours += 1
                    if (i < 19):
                        if (board[i + 1][j] == "O"):
                            neighbours += 1
                    if (i < 19 and j < 19):
                        if (board[i + 1][j + 1] == "O"):
                            neighbours += 1
                    if (board[i][j] == "O" and (neighbours == 2 or neighbours == 3)):
                        board2[i][j] = "O"
                    if (board[i][j] == "." and neighbours == 3):
                        board2[i][j] = "O"
            board = board2

gameoflife()

