#Name: Alex Dorodko
#Course: ICS3U
#Unit 2 - Assignment #2

#Welcoming the user to the machine.
print("Hello and Welcome to the Make Change Machine")
 
#Here the user would enter the value of how much cash he has

cash=float(input("Please enter the ammount in dollars and cents:"))

#Rounding the value so it is easier to work with it in the future
round(cash,2)
#Setting the values for the coins
nickel = 0.05
dime = 0.10
quarter = 0.25
loonie = 1.00
toonie = 2.00

#Here the idea is to divide by the value of the coin to see how much of them can
#fit in the cash ammount, and than do the same with the remainders with the other coins

print(int(cash//toonie), "toonies")
cash=cash%toonie
cash = round(cash,2)
print(int(cash//loonie), "loonies")
cash=cash%loonie
cash = round(cash,2)
print(int(cash//quarter), "quarters")
cash=cash%quarter
cash = round(cash,2)
print(int(cash//dime), "dimes")
cash=cash%dime
cash = round(cash,2)
print(int(cash//nickel), "nickels")
