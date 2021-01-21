# Program: Mors Code
# Date: February 19th, 2020
# Programmer: Input phrases and return them as morse code.

def morsecode():
    counter = 0
    phrase = input("Enter a phrase which you would like to change to morse code: ")
    phrase = phrase.upper()
    morse_phrase = ""
    while (counter < len(phrase)):
        if (phrase[counter] == "A"):
            morse_phrase += ".- "
        elif (phrase[counter] == "B"):
            morse_phrase += "-... "
        elif (phrase[counter] == "C"):
            morse_phrase += "-.-. "
        elif (phrase[counter] == "D"):
            morse_phrase += "-.. "
        elif (phrase[counter] == "E"):
            morse_phrase += ". "
        elif (phrase[counter] == "F"):
            morse_phrase += "..-. "
        elif (phrase[counter] == "G"):
            morse_phrase += "--. "
        elif (phrase[counter] == "H"):
            morse_phrase += ".... "
        elif (phrase[counter] == "I"):
            morse_phrase += ".. "
        elif (phrase[counter] == "J"):
            morse_phrase += ".--- "
        elif (phrase[counter] == "K"):
            morse_phrase += "-.- "
        elif (phrase[counter] == "L"):
            morse_phrase += ".-.. "
        elif (phrase[counter] == "M"):
            morse_phrase += "-- "
        elif (phrase[counter] == "N"):
            morse_phrase += "-. "
        elif (phrase[counter] == "O"):
            morse_phrase += "--- "
        elif (phrase[counter] == "P"):
            morse_phrase += ".--. "
        elif (phrase[counter] == "Q"):
            morse_phrase += "--.- "
        elif (phrase[counter] == "R"):
            morse_phrase += ".-. "
        elif (phrase[counter] == "S"):
            morse_phrase += "... "
        elif (phrase[counter] == "T"):
            morse_phrase += "- "
        elif (phrase[counter] == "U"):
            morse_phrase += "..- "
        elif (phrase[counter] == "V"):
            morse_phrase += "...- "
        elif (phrase[counter] == "W"):
            morse_phrase += ".-- "
        elif (phrase[counter] == "X"):
            morse_phrase += "-..- "
        elif (phrase[counter] == "Y"):
            morse_phrase += "-.-- "
        elif (phrase[counter] == "Z"):
            morse_phrase += "--.. "
        elif (phrase[counter] == "1"):
            morse_phrase += ".---- "
        elif (phrase[counter] == "2"):
            morse_phrase += "..--- "
        elif (phrase[counter] == "3"):
            morse_phrase += "...-- "
        elif (phrase[counter] == "4"):
            morse_phrase += "....- "
        elif (phrase[counter] == "5"):
            morse_phrase += "..... "
        elif (phrase[counter] == "6"):
            morse_phrase += "-.... "
        elif (phrase[counter] == "7"):
            morse_phrase += "--... "
        elif (phrase[counter] == "8"):
            morse_phrase += "---.. "
        elif (phrase[counter] == "9"):
            morse_phrase += "----. "
        elif (phrase[counter] == "0"):
            morse_phrase += "----- "
        elif (phrase[counter] == " "):
            morse_phrase += " "
        counter += 1
    print("Morse Code:", morse_phrase)

    # Another phrase or no
    again = str(input("Would you like to translate another sentence?(Y/N):"))
    again = again.upper()
    while (again != "Y" and again != "N"):
        again = str(input("Invalid answer. Would you like to enter another sentense?(Y/N): "))
        again = again.upper()

    if (again == "Y"):
        morsecode()
    elif (again == "N"):
        pass


morsecode()





















