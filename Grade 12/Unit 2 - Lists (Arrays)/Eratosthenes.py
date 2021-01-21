# Program Name: Eratosthenes
# Date: March 3rd, 2020
# Programmer: Alex Dorodko
# Description: Outputs all of the prime numbers up to a thousand.

import math

def eratosthenes():

    print("The prime numbers from 1 - 1000 are:")
    numbers = []
    for i in range (0, 1000):
        numbers.append(True)

    next_prime = 2

    while (next_prime < math.sqrt(1000)):
        #setting multiples to false
        for i in range(next_prime*2, 1000, next_prime):
            numbers[i] = False
        next_prime += 1
        while (numbers[next_prime] == False):
            next_prime += 1

    #Formatting
    counter = 0

    for i in range (2, 1000):
        if (numbers[i] == True):
            counter += 1
            print(str(i) + " ", end= "")
            if counter == 10:
                print("\n")
                counter = 0

    again = input("\nWould you like to run the program again?(Y/N)\n")
    again = again.upper()
    while (again != "Y" and again != "N"):
        again = input("Invalid answer. Would you like to run the program again?(Y/N)\n")
        again = again.upper()

    if (again == "Y"):
        eratosthenes()
    else:
        pass

eratosthenes()