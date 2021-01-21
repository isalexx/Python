# Program Name: Course Culminating Task (CCT).py
# Date: June 16th, 2020
# Programmer: Alex
# Program Description: Calculates an everage of a students grades and gives them a letter grade.

def grades():

    try:
        print("\nGrade Average\n**************\nThis program will ask you for your grade in each of your four courses.\nIt will then average them for you and give you your letter grade.\n") #Program introduction which states its purpose.

        name = str(input("Enter your first name: ")) #Input for users name.

        p1 = int(input("Enter your Period 1 percentage grade: ")) #Input for period 1 percentage, and a while loop to make sure they enter a correct one.
        while p1 not in range(0, 101):
            p1 = int(input("Invalid percentage. Enter your Period 1 percentage grade: "))

        p2 = int(input("Enter your Period 2 percentage grade: ")) #Input for period 2 percentage, and a while loop to make sure they enter a correct one.
        while p2 not in range(0, 101):
            p2 = int(input("Invalid percentage. Enter your Period 2 percentage grade: "))

        p3 = int(input("Enter your Period 3 percentage grade: ")) #Input for period 3 percentage, and a while loop to make sure they enter a correct one.
        while p3 not in range(0, 101):
            p3 = int(input("Invalid percentage. Enter your Period 3 percentage grade: "))

        p4 = int(input("Enter your Period 4 percentage grade: ")) #Input for period 4 percentage, and a while loop to make sure they enter a correct one.
        while p4 not in range(0, 101):
            p4 = int(input("Invalid percentage. Enter your Period 4 percentage grade: "))

        avg = round((p1 + p2 + p3 + p4) / 4, 1) #calculating the average percentage.

        #If statements which decide the Letter Grade by looking at the average percentage.
        if (avg >= 0) and (avg < 50):
            grade = "F"
        elif (avg >= 50) and (avg < 60):
            grade = "D"
        elif (avg >= 60) and (avg < 70):
            grade = "C"
        elif (avg >= 70) and (avg < 80):
            grade = "B"
        elif (avg >= 80) and (avg <= 100):
            grade = "A"

        print(f"\nHello {name}!\nYour average mark for the semester is: {avg}%\nYour Letter Grade for the semester is: {grade}\n") #printing the final output.

    except ValueError:
        print("\nNext time, please enter an integer for the program to work correctly") #Error proof incase they put a string where the percentages have to be.
        grades()

    finally:

        again = str(input("Would you like to run the program again? (Y/N): ")).upper() #asks the user if he would like to run the program again, and an error proof while statement
        while again not in ["N", "Y"]:
            again = str(input("Invalid answer. Would you like to run the program again? (Y/N): ")).upper()

        if (again == "Y"): #runs the program again if the user said yes.
            grades()
        else:
            pass

grades()