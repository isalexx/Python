#Name: Alex
#Course: ICS3U
#Guess the number
print("!!!!!IMPORTANT !!!!")
print("#Go to WIN+R, search CMD, and write 'pip install colorama' for this to work properly")
print()
print()
#Imports
import random
from colorama import init, Fore, Back, Style

init(convert=True)
#Variables
attempt = 0
wins = 0
losses = 0
round = 0
#Introduction
answer = "Y"
print("Here you will have to guess a number. You will pick the starting range, and a finishing range. ")
print("The number in-between those two values(including them) will be the one to guess.")
print("While setting up the range, the first number entered MUST be lower then the second, as well as they cannot be the same numbers.")
print()

#Functions
def play_again():
    global answer
    answer = (input("Do you want to play again?(Y/N): "))
    answer = answer.upper()
    while (answer != "Y" and answer != "N"):
            answer = str(input("Invalid answer. Do you want to play again?(Y/N): "))
            answer = answer.upper()

def clue(number_user):
     diff_bot = 0-number_bot
     diff_user = 0-number_user
     if (diff_user <= diff_bot):
         print("The number is lower")
     elif(diff_user >= diff_bot):
          print("The number is higher")



#Main Structure
while (answer == "Y"):
       round += 1
       print()
       attempt = 0
       #Ranges
       first = int(input("Pick a starting range of the number: "))
       second = int(input("Pick a finishing range of the number: "))
       while (second <= first or second == ""):
              second = int(input("The second number is lower or equal to the first, pick a different finishing range value: "))

       guesses = int(input("How many guesses would you like?: "))
       while (guesses <= 0):
              guesses = int(input("Invalid number, has to be above zero. How many guesses would you like?: "))

       #Computer selects a random number
       number_bot = random.randint(first, second)
       print()
       number_user = int(input("The computer has picked a value. Try to guess it: "))
       while (number_user < first or number_user > second):
              number_user = int(input("The guess is out of number range. Try again: "))




       if (number_user == number_bot):
           print(Fore.GREEN + "Correct!"+ Fore.RESET)
           wins += 1
           play_again()

       while (number_user != number_bot):
              attempt += 1
              print()
              if (number_user == number_bot):
                    print(Fore.GREEN + "Correct!"+ Fore.RESET)
                    wins += 1
                    play_again()
              elif (guesses-attempt == 0):
                  print("You" ,Fore.RED + "lost!"+ Fore.RESET, "Out of guesses.")
                  losses += 1
                  play_again()
                  break

              elif (number_user != number_bot):

                  clue(number_user)
                  print("Attempts left:", guesses-attempt)
                  number_user = int(input("Try again: "))
                  while (number_user < first or number_user > second):
                         number_user = int(input("The guess is out of number range. Try again: "))
                  if (number_user == number_bot):
                      print(Fore.GREEN + "Correct!"+ Fore.RESET)
                      wins += 1
                      play_again()

       print()
       print("Score after round", round)
       print(Fore.MAGENTA + "================="+ Fore.RESET)
       print(Fore.GREEN + "Wins:"+ Fore.RESET , wins)
       print(Fore.RED + "Losses:"+ Fore.RESET , losses)
       print(Fore.MAGENTA + "================="+ Fore.RESET)

x = input("Press Enter to close the program.")
