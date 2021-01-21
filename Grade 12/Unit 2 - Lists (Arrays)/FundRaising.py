# Program Name: Triplets
# Date: March 11, 2020
# Programmer: Alex Dorodko
#Outputs the donations amount in a list, based on the ammount donated per student, and school population

def fundraising():
    # initializing all variables
    rows = 4
    cols = 10
    tempData = 0

    values = []
    for i in range(0, rows):
        values.append([])
        for j in range(0, cols):
            values[i].append(tempData)

    choice = -1
    donation = -1
    population = -1

    real_amount = 0
    total_line = 0
    total_donation = 0

    end_menu = False

    while (end_menu == False):
        school_choice = int(input("Which school is doing fundraising?\n0 - St. Joseph's\n1 - St. Peter's\n2 - St. Joan of Arc\n3 - Holy Trinity\n4 - St. Thomas Aquinas\n5 - Patric Fogarty\n6 - St. Theresa's\n7 - St. Dominics\n8 - Jean Vanier\n9 - Exit\n"))
        while (school_choice > 9 or school_choice < 0):
               school_choice = int(input("Wrong answer. Please chose a school. (0-9)\n"))

        if (school_choice == 9):
            break

        donation_choice = int(input("What is the donation amount?\n0 - 25 cents\n1 - 50 cents\n2 - 1 dollar\n3 - 2 dollars\n"))
        while (donation_choice > 3 or donation_choice < 0):
               donation_choice = int(input("Wrong answer. Please choose the correct donation amount. (0-3)\n"))

        population = int(input("What is the school population?\n"))
        while (population < 0):
               population = int(input("Population cannot be negative. Please enter another number.\n"))

        #calculating donations

        if (donation_choice == 0):
            donation_amount = 0.25 * population
        elif (donation_choice == 1):
            donation_amount = 0.5 * population
        elif (donation_choice == 2):
            donation_amount = population
        elif (donation_choice == 3):
            donation_amount = 2 * population

        values[donation][choice] = real_amount
        total_donation = 0

        print("AMT\t\tSJO\tPET\tJOA\tHTR\tSTS\tPFO\tSTH\tDOM\tJVA\tTOTAL\t")

        for i in range(0, 4):  # prints out the four rows
            print(donation_amount[i], "\t", end="")
            totalLine = 0
            for j in range(0, 9):  # prints out 10 columns per row
                total_donation += values[i][j]
                total_line += values[i][j]
                if values[i][j] > 0:
                    print(
                        f"{values[i][j]:>-4}", "\t\t", end=""
                    )
                else:
                    print(values[i][j], "\t\t", end="")
            print(total_line)
        print("TOTAL DONATIONS: $", total_donation)  # prints the total donations from all schools and all amounts




fundraising()
