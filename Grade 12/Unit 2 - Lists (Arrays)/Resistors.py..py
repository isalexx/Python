# Program Name: Resistors
# Date: March 1st, 2020
# Programmer: Alex Dorodko
# Description: Takes three colours, separated by hyphens, and prints the value of the resistor.

def resistor():
    counter = 0

    #colors
    colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    res1 = 0
    res2 = 0
    res3 = 0

    #input
    rstr_colors = input("What is your resistors colour code?\nSeperate each colour by hyphens (e.g. red-orange-black)\n")
    rstr_colors_lower = rstr_colors.lower()

    #splitting the colors
    rstr_colors_list = rstr_colors_lower.split("-")

    #resistances
    while (counter < len(colors)):
        if (rstr_colors_list[0] == colors[counter]):
            res1 = counter
        if (rstr_colors_list[1] == colors[counter]):
            res2 = counter
        if (rstr_colors_list[2] == colors[counter]):
            res3 = counter
        counter += 1

    #converting to string to join them
    res1 = str(res1)
    res2 = str(res2)

    two_digits_str = res1+res2
    first_two = int(two_digits_str)

    #output
    resistance = first_two*(10**int(res3))
    print("You entered", rstr_colors,"\nThe value of the resistor is", resistance, "ohms")

    #Another resistor?
    again = str(input("\nWould you like to enter another resistor? (Y/N)\n"))
    again = again.upper()
    while (again != "Y" and again != "N"):
        again = str(input("Invalid answer. Would you like to enter another resistor? (Y/N)\n"))
        again = again.upper()

    if (again == "Y"):
        resistor()
    elif (again == "N"):
        pass
resistor()