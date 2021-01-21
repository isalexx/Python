# Program Name: RoundingError
# Date: February 5th, 2020
# Programmer: Alex Dorodko
# Description: Compares the square of the square root of any number to itself, due to the rounding error in python.

import math

#input
number = int(input("Enter a number: "))
while number <= 0:
      number = int(input("Invalid number, impossible to square numbers 0 and below. Enter a different number: "))

#variables
square = math.sqrt(number)
squaresquare = math.pow(square, number)
diff = squaresquare-number

#output
print("The square of the square =",squaresquare)
print("The round off error =", diff)
