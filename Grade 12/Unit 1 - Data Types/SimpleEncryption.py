# Program: Simple Encryption
# Date: February 18th, 2020
# Programmer: Ecrypt/Decrypt messages using letter rotation

def simpleencryption():
    again = ""
    #Input -----------------------------------------------------------------------------------------------------------
    print("This program will decrypt or encrypt a phrase using the simple encyption method of rotating the letters.\n")

    #Decrypt or Encrypt
    choice = input("1 - Encryption\n2 - Decryption\nWhat would you like to do?(1/2):")
    while (choice != "1" and choice != "2"):
           choice = input("Invalid answer. What would you like to do?(1/2):")

    phrase = input("Please enter a phrase: ")

    # Rotation ammount
    ammount = int(input("Enter the rotation ammount (1-25): "))
    while (ammount <= 0 or ammount > 25):
        ammount = int(input("Invalid Answer. Enter the rotation ammount (1-25): "))

    #Encryption
    if (choice == "1"):
        en_phrase = ""
        for i in range(0, len(phrase)):
            char_value = ord(phrase[i])
            if (char_value == 32):
                char_value = 32
                en_phrase += chr(char_value)
            elif(char_value != 32):
                char_value += ammount
                if (char_value > 122):
                    char_value -= 122
                    char_value += 96
                en_phrase += chr(char_value)
        print("\nThe original phrase is", phrase, "\nThe encrypted message is", en_phrase)

    #Decryption
    elif (choice == "2"):
        de_phrase = ""
        for i in range(0, len(phrase)):
            char_value = ord(phrase[i])
            if (char_value == 32):
                char_value = 32
                de_phrase += chr(char_value)
            elif (char_value != 32):
                char_value -= ammount
                if (char_value < 96):
                    char_value -= 96
                    char_value += 122
                de_phrase += chr(char_value)
        print("\nThe original phrase is", phrase, "\nThe decrypted message is", de_phrase)

    #Another phrase or no ---------------------------------------------------------------------------------------------
    again = str(input("\nWould you like to decrypt/encrypt another message?(Y/N): :"))
    again = again.upper()
    while (again != "Y" and again != "N"):
        again = str(input("Invalid answer. Would you like to decrypt/encrypt another message?(Y/N): "))
        again = again.upper()

    if (again == "Y"):
        simpleencryption()
    elif (again == "N"):
        pass

simpleencryption()