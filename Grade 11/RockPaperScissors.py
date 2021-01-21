#Name: Alex
#Course: ICS3U
#Rock paper, scissors game
print("!!!!!IMPORTANT !!!!")
print("#Go to WIN+R, search CMD, and write 'pip install colorama' for this to work properly")
print()
print()

#Imports

import string
import random
import time
from colorama import init, Fore, Back, Style
init(convert=True)

#List
object = ["paper", "rock", "scissors"]

#Functions
def play_again():
    global answer
    answer = (input("Do you want to play again?(Y/N): "))
    answer = answer.upper()
    while (answer != "Y" and answer != "N"):
           answer = str(input("Invalid answer. Do you want to play again?: "))
           answer = answer.upper()
answer = "Y"
wins = 0
losses = 0
ties = 0
round = 0

#Main Structure
while (answer == "Y"):
       round += 1
       choice_user = str(input("Rock, paper, or scissors?: "))
       choice_user = choice_user.lower()
       while (choice_user != "rock" and choice_user != "paper" and choice_user != "scissors"):
              choice_user = str(input("Invalid answer. Rock, paper, or scissors?: "))

       choice_bot = object[random.randint(0, 2)]

       print("The bot picked "+choice_bot)

       if (choice_bot == choice_user):
           print(Fore.YELLOW + "Tie!"+ Fore.RESET)
           ties += 1
       elif (choice_bot == "rock" and choice_user == "paper"):
             print("You "+Fore.GREEN + "won!"+ Fore.RESET)
             wins += 1
       elif (choice_bot == "rock" and choice_user == "scissors"):
             print("You", Fore.RED + "lost!"+ Fore.RESET)
             losses += 1
       elif (choice_bot == "paper" and choice_user == "rock"):
             print("You", Fore.RED + "lost!"+ Fore.RESET)
             losses += 1
       elif (choice_bot == "paper" and choice_user == "scissors"):
             print("You "+Fore.GREEN + "won!"+ Fore.RESET)
             wins += 1
       elif (choice_bot == "scissors" and choice_user == "rock"):
             print("You "+Fore.GREEN + "won!"+ Fore.RESET)
             wins += 1
       elif (choice_bot == "scissors" and choice_user == "paper"):
             print("You", Fore.RED + "lost!"+ Fore.RESET)
             losses += 1
       print()
       print("Score after round", round)
       print(Fore.MAGENTA + "================="+ Fore.RESET)
       print(Fore.GREEN + "Wins:"+ Fore.RESET , wins)
       print(Fore.RED + "Losses:"+ Fore.RESET , losses)
       print(Fore.YELLOW + "Ties:"+ Fore.RESET , ties)
       print(Fore.MAGENTA + "================="+ Fore.RESET)
       play_again()
       print()
x = input("Press Enter to close the program.")
