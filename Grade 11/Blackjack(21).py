#Name: Alex
#Course: ICS3U

print("!!!!!IMPORTANT !!!!")
print("#Go to WIN+R, search CMD, and write 'pip install colorama' for this to work properly")

#Imports
import random
from colorama import init, Fore, Back, Style
init(convert=True)

#List (deck)
card = [1, 1, 1, 1, 10, 10, 10, 10, 2, 2, 2, 2, 3, 3, 3, 3, 10, 10, 10, 10, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 10, 10, 10, 10, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, ]

answer = "Y"
round = 0
wins = 0
losses = 0
ties = 0

#Functions
def play_again():
    global answer
    answer = (input("Do you want to play again?(Y/N): "))
    answer = answer.upper()
    while (answer != "Y" and answer != "N"):
            answer = str(input("Invalid answer. Do you want to play again?(Y/N): "))
            answer = answer.upper()

def another_card():
    global answer_card
    answer_card = (input("Would you like another card?(Y/N): "))
    answer_card = answer_card.upper()
    while (answer_card != "Y" and answer_card != "N"):
           answer_card = str(input("Invalid answer. Would you like another card?(Y/N): "))
           answer_card = answer_card.upper()

#Main Structure
while (answer == "Y"):
       user_deck = []
       y = 0
       round += 1
       print("Round", round)
       print(Fore.MAGENTA + "======="+ Fore.RESET)
       print("")
       bot_cards = 0
       user_cards = 0
       #first given cards
       user_cards = user_cards + card[random.randint(0,51)]
       card_1 = user_cards
       user_deck.append(card_1)
       user_cards = user_cards + card[random.randint(0,51)]
       card_2 = user_cards-card_1
       user_deck.append(card_2)
       print("Your starting hand is a", user_deck[0], "and", user_deck[1], ". Total is", user_deck[0]+user_deck[1])
       bot_cards = bot_cards + card[random.randint(0,51)]
       bot_cards = bot_cards + card[random.randint(0,51)]
       print("Opponent has recieved two cards")
       another_card()
       print()

       if (user_cards <= 21):
           while (answer_card == "Y"):
                  y += 1
                  user_cards = user_cards + card[random.randint(0,51)]
                  if (y == 1):
                      user_deck.append(user_cards - user_deck[0] - user_deck[1])
                  elif (y == 2):
                        user_deck.append(user_cards - user_deck[0] - user_deck[1] - user_deck[2])
                  elif (y == 3):
                        user_deck.append(user_cards - user_deck[0] - user_deck[1] - user_deck[2] - user_deck[3])
                  elif (y == 4):
                        user_deck.append(user_cards - user_deck[0] - user_deck[1] - user_deck[2] - user_deck[3] - user_deck[4])
                  elif (y == 5):
                        user_deck.append(user_cards - user_deck[0] - user_deck[1] - user_deck[2] - user_deck[3] - user_deck[4] - user_deck[5])
                  elif (y == 6):
                        user_deck.append(user_cards - user_deck[0] - user_deck[1] - user_deck[2] - user_deck[3] - user_deck[4] - user_deck[5] - user_deck[6])
                  elif (y == 7):
                        user_deck.append(user_cards - user_deck[0] - user_deck[1] - user_deck[2] - user_deck[3] - user_deck[4] - user_deck[5] - user_deck[6] - user_deck[7])
                  print("Your updated total card value is", user_cards, ". Your cards are", user_deck)
                  if (bot_cards < 16):
                      bot_cards = bot_cards + card[random.randint(0,51)]
                      print("Opponent has recieved a card")
                  if (user_cards > 21):
                      losses += 1
                      print("You"+Style.BRIGHT, Fore.RED + "lost!"+ Fore.RESET, Style.RESET_ALL, "Card value went over 21.")
                      play_again()
                      break
                  else:
                      another_card()
                      print()

       if (user_cards <= 21):
           while (bot_cards < 16):
                  bot_cards = bot_cards + card[random.randint(0,51)]
                  print("Opponent has recieved a card")

       if (user_cards <= 21):
           if (bot_cards > 21):
               wins += 1
               print("Your final hand value is", user_cards, "and the opponent's final value is", bot_cards)
               print("You ", Fore.GREEN + "win!"+ Fore.RESET, "The opponent went over 21.")
               play_again()
           elif (user_cards == bot_cards):
                 ties += 1
                 print("Your final hand value is", user_cards, "and the opponent's final value is", bot_cards)
                 print(Fore.YELLOW + "Tie!"+ Fore.RESET)
                 play_again()
           elif (user_cards > bot_cards):
                 wins += 1
                 print("Your final hand value is", user_cards, "and the opponent's final value is", bot_cards)
                 print("You", Fore.GREEN + "win!"+ Fore.RESET)
                 play_again()
           elif (bot_cards > user_cards):
                 losses += 1
                 print("Your final hand value is", user_cards, "and the opponent's final value is", bot_cards)
                 print("You"+Style.BRIGHT, Fore.RED + "lost!"+ Fore.RESET, Style.RESET_ALL)
                 play_again()
       print()
       print("Score after round", round)
       print(Fore.MAGENTA + "================="+ Fore.RESET)
       print(Fore.GREEN + "Wins:"+ Fore.RESET , wins)
       print(Fore.RED+ Style.BRIGHT + "Losses:"+ Fore.RESET, Style.RESET_ALL , losses)
       print(Fore.YELLOW + "Ties:"+ Fore.RESET , ties)
       print(Fore.MAGENTA + "================="+ Fore.RESET)
       print()

x = input("Press Enter to close the program.")
