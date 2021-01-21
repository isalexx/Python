# Program Name: ATM.py
# Date: April 11, 2020
# Programmer: Alex Dorodko
#Class file for ATM

class atm:
    def __init__(self, name="Unknown", balance=0,):

        self.atmName = name
        self.atmBalance = balance

    #Depositing
    def deposit(self, amount, balance):
        amount = float(input("How much would you like to deposit?"))
        while (amount < 0):
            amount = int(input("Invalid ammount, cannot be less then 0. How much would you like to deposit?: "))
        self.atmBalance += amount
        print("\nYour new balance is $"+ str(round(self.atmBalance)),"\n")

    #current balance
    def balance(self, balance):
        print("\nYour current balance is $"+ str(round(self.atmBalance)),"\n")

    #Withdrawing
    def withdraw(self, balance):
        amount = int(input("How much would you like to withdraw?"))
        while (amount < 0):
            amount = int(input("Invalid ammount, cannot be less then 0. How much would you like to withdraw?: "))
        while (amount > balance):
            amount = int(input("Insufficient funds. How much would you like to withdraw?: "))
        self.atmBalance -= amount
        print("\nYour new balance is $" + str(round(self.atmBalance)), "\n")

    #Interest thing
    def interest(self, balance):

        i = int(input("\nWhat is the interest rate as a percentage?: "))
        while (i < 0):
            i = int(input("Percentage cannot be less then 0. What is the interest rate as a percentage?: "))

        i = i / 100 / 365

        n = int(input("What is the number of days you will leave the balance invested?"))
        while (n < 0):
            n = int(input("Cannot be less then 0. What is the number of days you will leave the balance invested?"))

        self.atmBalance = self.atmBalance * ((1 + i) ** n)

        print("\nYour new balance is $" + str(round(self.atmBalance,2)), "\n")
