# Program: Palidrome
# Date: February 18th, 2020
# Programmer: Alex Dorodko
# Description: By entering the year a phrase, it will spell it in reverse and will tell you if its a pelidrome.

#Input for the word

def palidrome():
    again = ""
    #Input
    sentence = str(input("Enter a sentance: "))
    sentence = sentence.lower()
    sentence = sentence.replace(" ", "")

    #Reversing senntence
    sentence_backwards = sentence[::-1]

    #Output
    if (sentence == sentence_backwards):
        print("This phrase is a palidrome.")
    elif (sentence != sentence_backwards):
        print("This phrase is not a palidrome.")

    #Another phrase or no
    again = str(input("Would you like to enter another sentence?(Y/N):"))
    again = again.upper()
    while (again != "Y" and again != "N"):
        again = str(input("Invalid answer. Would you like to enter another sentence?(Y/N): "))
        again = again.upper()

    if (again == "Y"):
        palidrome()
    elif (again == "N"):
        pass

palidrome()