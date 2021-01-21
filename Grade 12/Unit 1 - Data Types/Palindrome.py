# Program: Palidrome
# Date: February 16th, 2020
# Programmer: Alex Dorodko
# Description: By entering the year a word, it will spell it in reverse and will tell you if its a pelidrome

#Input for the word



def palidrome():
    again = ""
    original_word = str(input("Enter a word: "))
    original_word = original_word.lower()

    backwards_word = ""

    for i in range(len(original_word) - 1, -1, -1):
        backwards_word = backwards_word + original_word[i]

    print(original_word +" in reverse is: " + backwards_word)

    if (original_word == backwards_word):
        print("This word is a palindrome")

    elif (original_word != backwards_word):
        print("This word is not a palindrome")

    again = str(input("Would you like to enter another word?(Y/N):"))
    again = again.upper()
    while (again != "Y" and again != "N"):
        again = str(input("Invalid answer. Would you like to enter another word?(Y/N): "))
        again = again.upper()

    if (again == "Y"):
        palidrome()
    elif (again == "N"):
        pass

palidrome()