# Program Name: Triplets
# Date: March , 2020
# Programmer: Alex Dorodko
#Picks a random word / phrase from a category wwhich would display on the screen in dashes.

import random

win = False

sports = ["SPORTS", "SOCCER", "BASKETBALL", "FOOTBALL", "VOLLEYBALL", "BIKING", "RUNNING", "HIKING"]
car_brands = ["CAR BRANDS", "BMW", "MINI", "AUDI", "MERCEDES", "ACURA", "GMC", "PORCHE"]
pc_brands = ["PC BRANDS", "ACER", "SAMSUNG", "LENOVO", "ASUS", "BENQ", "DELL", "APPLE"]

hang_man_words = [sports, car_brands, pc_brands]
graphics = ["  O \n/ | \\\n  |\n/   \\", "  O \n/ | \\\n  |\n/", "  O \n/ | \\\n  |", "  O \n/ | \\", "  O \n/ |", "  O \n/", "  O", " "]

category_index = random.randint(0, 2)
word_index = random.randint(0, len(hangmancategory_index)-1)
category = hang_man_words[category_index][0]
word = hang_man_words[category_index][word_index]
blank_word = ""
num_words = 1

for pos in range (0, len(word)):
    if (ord(word[pos]) >= 65) and (ord(word[pos]) <= 90):
        blank_word += "-"
    else:
        blank_word += word[pos]
        if word[pos] == " ":
            num_words += 1

letters_used = ""
num_guesses = 7

while num_guesses > 0:
    print("*******************************\nCategory:", category, "\nNumber of Words:", num_words, "\n", blank_word)
    print(graphics[num_guesses])
    print("Number of guesses remaining:", num_guesses)
    my_guess = input("Guess a letter: ")
    my_guess = my_guess.upper()
    found = False
    for pos in range(0, len(word)):
        if word[pos] == my_guess:
            blank_word = blank_word[0:pos] +my_guess +blank_word[pos + 1:len(blank_word)]
            found = True
    if found == True:
        print("\n"+my_guess, "is in the word!")
    else:
        print("\n"+my_guess, "is not in the word")
        num_guesses -= 1

    if (blank_word == word):
        print("\nCongradulations, you guessed correctly! The word is"+blank_word)
        num_guesses = -1
        win = True

    if (num_guesses <= 0 and win == False):
        print("Game over.\n", graphics[0], "\nThe correct word is:", word)


