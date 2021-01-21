# Program: Palidrome 2
# Date: February 18th, 2020
# Programmer: Alex Dorodko
# Description: By entering the year a sentence, it will tell you if any words in it are pelidromes.

#Input for the word

def palidrome():
    again = ""
    #Input
    sentence = str(input("Enter a sentence: "))
    sentence = sentence.lower()
    words = sentence.split()

    #Number of palidromes
    palidromes = []
    palidrome_counter = 0

    #testing if a word is a palidrome
    for i in range(0, len(words)):
        backwards_word = words[i][::-1]
        if (words[i] == backwards_word):
            palidrome_counter += 1
            palidromes.append(words[i])

    if (palidrome_counter >= 2):
        print("There are", palidrome_counter, "palidrome in the entered sentence.")
        palidromes = str(palidromes)
        print("The palidromes are", palidromes[1:len(palidromes)-1])
    elif (palidrome_counter == 1):
        print("There is", palidrome_counter, "palidrome in the entered sentence.")
        palidromes = str(palidromes)
        print("The palidrome is", palidromes[1:len(palidromes)-1])
    elif (palidrome_counter == 0):
        print("There are no palidromes in the entered sentence.")

    again = str(input("Would you like to enter another sentence?(Y/N):"))
    again = again.upper()
    while (again != "Y" and again != "N"):
        again = str(input("Invalid answer. Would you like to enter another sentense?(Y/N): "))
        again = again.upper()

    if (again == "Y"):
        palidrome()
    elif (again == "N"):
        pass

palidrome()