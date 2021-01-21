# Program Name: AreaOfTriangle
# Date: February 5th, 2020
# Programmer: Alex Dorodko
# Description: Calculates the area of a scalene triangle using two different formulas

import math

def areaoftriangle():
    play_again = "x"
    # Formula descision
    print("Calculate triangle area using:\n1 - Heron's formula\n2 - Trigonometry")
    formula = int(input("Which formula would you like to use? (1/2): "))
    while formula != 1 and formula != 2:
        formula = int(input("Invalid number. Choose the 1st or 2nd formula (1/2): "))
    print()

    # Calculating the area using the requested formula
    if formula == 1:
        # Requestiong dimensions
        a = float(input("What is the length of side \'a\'?: "))
        b = float(input("What is the length of side \'b\'?: "))
        while b == a:
            b = float(input("Invalid length. Scalene triangle cannot have the same length sides. What is the length of side \'b\'?:  "))
        c = float(input("What is the length of side \'c\'?: "))
        while c == a or c == b:
            c = float(input("Invalid length. Scalene triangle cannot have the same length sides. What is the length of side \'c\'?:  "))
        #The Triangle Inequality Theorem rule
        while max(a,b,c) >= a+b+c-max(a,b,c):
              print("\nInvaid lengths. Due to the Triangle Inequality Theorem, the longest side length must be higher then the shorter sides combined. Input the sides again.\n")
              a = float(input("What is the length of side \'a\'?: "))
              b = float(input("What is the length of side \'b\'?: "))
              while b == a:
                  b = float(input("Invalid length. Scalene triangle cannot have the same length sides. What is the length of side \'b\'?:  "))
              c = float(input("What is the length of side \'c\'?: "))
              while c == a or c == b:
                  c = float(input("Invalid length. Scalene triangle cannot have the same length sides. What is the length of side \'c\'?:  "))



        # Using the formula
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        # converting to string to attach the comas
        a = str(a)
        b = str(b)
        print()
        print("The area of the triangle with side lengths", a + ",", b + ", and", c, "is", area)

        #Another triangle?
        play_again = input("Would you like to calculate another triangle? (Y/N)")
        play_again = play_again.upper()
        while (play_again != "Y" and play_again != "N"):
            play_again = input("Invalid answer. Would you like to calculate another triangle? (Y/N)")
        if (play_again == "Y"):
            print("")
            areaoftriangle()
        elif (play_again == "N"):
            pass

    elif formula == 2:
        # Requesting dimensions and an angle
        a = float(input("What is the length of side \'a\'?: "))
        b = float(input("What is the length of side \'b\'?: "))
        while b == a:
            b = float(input("Invalid length. Scalene triangle cannot have the same length sides. What is the length of side \'b\'?:  "))
        C = float(input("What is the measurement of angle \'C\' in degres?: "))
        while C >= 180 or 0 >= C:
            C = float(input("Invalid measurement. Must be between 0 - 180 degrees. What is the measurement of angle \'C\' in degres?:  "))

        # Using the formula
        area = (a * b * math.sin(C * math.pi / 180)) / 2
        # converting to string to attach the comas
        a = str(a)
        b = str(b)
        print()
        print("The area of the triangle with side lengths", a + ",", b + ", and angle degree of", C, "is", area)
        #Another triangle?
        play_again = input("Would you like to calculate another triangle? (Y/N)")
        play_again = play_again.upper()
        while (play_again != "Y" and play_again != "N"):
            play_again = input("Invalid answer. Would you like to calculate another triangle? (Y/N)")
        if (play_again == "Y"):
            print("")
            areaoftriangle()
        elif (play_again == "N"):
              pass

areaoftriangle()