#Name: Alex
#Course: ICS3U
#Colored blocks game

print("!!!!!IMPORTANT !!!!")
print("#Go to WIN+R, search CMD, and write 'pip install colorama' for this to work properly")

import random
from colorama import init, Fore, Back, Style
init(convert=True)

def play_again():
    global answer
    answer = (input("Do you want to play again?(Y/N): "))
    answer = answer.upper()
    while (answer != "Y" and answer != "N"):
            answer = str(input("Invalid answer. Do you want to play again?(Y/N): "))
            answer = answer.upper()

block1 = "red"
block2 = "yellow"
block3 = "green"
block4 = "blue"
wins = 0
losses = 0
answer = "Y"

print("Welcome to the colored blocks game! Here, you will try to guess the postioning of all four blocks, colored"+ Fore.RED, "Red"+ Fore.RESET+ ",", Fore.YELLOW + "Yellow" + Fore.RESET + ",", Fore.CYAN + "blue" + Fore.RESET + ","+ Fore.RESET, "and"+ Fore.GREEN, "green.", Fore.RESET)
print("You will be given the positioning of one colored blocks, rest you will have to guess. Watch out, you have a limited ammount of guesses.")
print()

while (answer == "Y"):
       attempts = 6 #2 attempts per each color
       guess1 = 0
       guess2 = 0
       guess3 = 0
       guess4 = 0
       round = 0

       block1_position = random.randint(1, 4)
       block2_position = random.randint(1, 4)
       while (block2_position == block1_position):
              block2_position = random.randint(1, 4)
       block3_position = random.randint(1, 4)
       while (block3_position == block1_position or block3_position == block2_position):
              block3_position = random.randint(1, 4)
       block4_position = random.randint(1, 4)
       while (block4_position == block1_position or block4_position == block2_position or block4_position == block3_position):
              block4_position = random.randint(1, 4)

       #giving the person the 1st block
       if (block1_position == 1):
           print("You're given block will be", Fore.RED + "red"+ Fore.RESET, "and it is in position number", block1_position)
           guess1 += 1
       elif (block2_position == 1):
             print("You're given block will be", Fore.YELLOW + "yellow"+ Fore.RESET, "and it is in position number", block2_position)
             guess2 += 1
       elif (block3_position == 1):
             print("You're given block will be", Fore.GREEN + "green"+ Fore.RESET, "and it is in position number", block3_position)
             guess3 += 1
       elif (block4_position == 1):
             print("You're given block will be", Fore.CYAN + "blue"+ Fore.RESET, "and it is in position number", block4_position)
             guess4 += 1

       if (block1_position != 1):
           guess1 = int(input("Try to guess the position of the red block: "))
           while (guess1 > 4 or guess1 < 1):
                  guess1 = int(input("Invalid. Has to be between one and four. Try to guess the position of the red block: "))
           attempts -= 1
       if (block2_position != 1):
           guess2 = int(input("Try to guess the position of the yellow block: "))
           while (guess2 > 4 or guess2 < 1):
                  guess2 = int(input("Invalid. Has to be between one and four. Try to guess the position of the red block: "))
           attempts -= 1
       if (block3_position != 1):
           guess3 = int(input("Try to guess the position of the green block: "))
           while (guess3 > 4 or guess3 < 1):
                  guess3 = int(input("Invalid. Has to be between one and four. Try to guess the position of the red block: "))
           attempts -= 1
       if (block4_position != 1):
           guess4 = int(input("Try to guess the position of the blue block: "))
           while (guess4 > 4 or guess4 < 1):
                  guess4 = int(input("Invalid. Has to be between one and four. Try to guess the position of the red block: "))
           attempts -= 1

       #Results per round
       print()
       round += 1
       print("Results for round number", round)
       print("======================")
       if (block1_position != 1):
           if (block1_position == guess1 and guess1 > 0):
               print(Fore.RED + "Red"+ Fore.RESET, "block is correct!")
           elif (block1_position != guess1):
               print(Fore.RED + "Red"+ Fore.RESET, "block is incorrect.")
       if (block2_position != 1):
           if (block2_position == guess2 and guess2 > 0):
               print(Fore.YELLOW + "Yellow"+ Fore.RESET, "block is correct!")
           elif (block2_position != guess2):
               print(Fore.YELLOW + "Yellow"+ Fore.RESET, "block is incorrect.")
       if (block3_position != 1):
           if (block3_position == guess3 and guess3 > 0):
               print(Fore.GREEN + "Green"+ Fore.RESET, "block is correct!")
           elif (block3_position != guess3):
               print(Fore.GREEN + "Green"+ Fore.RESET, "block is incorrect.")
       if (block4_position != 1):
           if (block4_position == guess4 and guess4 > 0):
               print(Fore.CYAN + "Blue"+ Fore.RESET, "block is correct!")
           elif (block4_position != guess4):
               print(Fore.CYAN + "Blue"+ Fore.RESET, "block is incorrect.")
       print("=======================")

       if (block1_position == guess1 and block2_position == guess2 and block3_position == guess3 and block4_position == guess4):
           print("You "+Fore.GREEN + "won!"+ Fore.RESET)
           wins += 1
           play_again()

       else:
           while(attempts > 0):
                 print("You have", attempts, "attempts left. Try to guess them again. Keep mind of the ones you got right.")

                 if (attempts > 0):
                     if (block1_position != 1):
                         guess1 = int(input("Try to guess the position of the red block: "))
                         while (guess1 > 4 or guess1 < 1):
                                guess1 = int(input("Invalid. Has to be between one and four. Try to guess the position of the red block: "))
                         attempts -= 1
                     if (block2_position != 1):
                         guess2 = int(input("Try to guess the position of the yellow block: "))
                         while (guess2 > 4 or guess2 < 1):
                                guess2 = int(input("Invalid. Has to be between one and four. Try to guess the position of the red block: "))
                         attempts -= 1
                     if (block3_position != 1):
                         guess3 = int(input("Try to guess the position of the green block: "))
                         while (guess3 > 4 or guess3 < 1):
                                guess3 = int(input("Invalid. Has to be between one and four. Try to guess the position of the red block: "))
                         attempts -= 1
                     if (block4_position != 1):
                         guess4 = int(input("Try to guess the position of the blue block: "))
                         while (guess4 > 4 or guess4 < 1):
                                guess4 = int(input("Invalid. Has to be between one and four. Try to guess the position of the red block: "))
                         attempts -= 1


                 print()
                 round += 1
                 print("Results for round number", round)
                 print("======================")
                 if (block1_position != 1):
                     if (block1_position == guess1 and guess1 > 0):
                         print(Fore.RED + "Red"+ Fore.RESET, "block is correct!")
                     elif (block1_position != guess1):
                         print(Fore.RED + "Red"+ Fore.RESET, "block is incorrect.")
                 if (block2_position != 1):
                     if (block2_position == guess2 and guess2 > 0):
                         print(Fore.YELLOW + "Yellow"+ Fore.RESET, "block is correct!")
                     elif (block2_position != guess2):
                         print(Fore.YELLOW + "Yellow"+ Fore.RESET, "block is incorrect.")
                 if (block3_position != 1):
                     if (block3_position == guess3 and guess3 > 0):
                         print(Fore.GREEN + "Green"+ Fore.RESET, "block is correct!")
                     elif (block3_position != guess3):
                         print(Fore.GREEN + "Green"+ Fore.RESET, "block is incorrect.")
                 if (block4_position != 1):
                     if (block4_position == guess4 and guess4 > 0):
                         print(Fore.CYAN + "Blue"+ Fore.RESET, "block is correct!")
                     elif (block4_position != guess4):
                         print(Fore.CYAN + "Blue"+ Fore.RESET, "block is incorrect.")
                 print("=======================")

                 if (block1_position == guess1 and block2_position == guess2 and block3_position == guess3 and block4_position == guess4):
                     print("You "+Fore.GREEN + "won!"+ Fore.RESET)
                     wins += 1
                     play_again()
                     print("==================================")
                     print()
                     break
                 elif (attempts == 0):
                     print("You have no more guesses, you", Fore.RED + "lost!"+ Fore.RESET)
                     losses += 1
                     play_again()
                     print("==================================")
                     print()
       print()
       print("Score after round", round)
       print(Fore.MAGENTA + "================="+ Fore.RESET)
       print(Fore.GREEN + "Wins:"+ Fore.RESET , wins)
       print(Fore.RED + "Losses:"+ Fore.RESET , losses)
       print(Fore.MAGENTA + "================="+ Fore.RESET)
x = input("Press Enter to close the program.")
