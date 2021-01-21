# Program Name: Car.py
# Date: April 11, 2020
# Programmer: Alex Dorodko
#Class file for Car

import random



class Car:
    makes = [["Toyota", "Camry"], ["Mazda", "RX-7"], ["Nissan", "R34"], ["Honda", "NSX"], ["Dodge", "Viper"]]
    x = random.randint(0, 4)

    #constructor
    def __init__(self, make=makes[x][0], model=makes[x][1], year=random.randint(1980, 2020), speed=random.randint(140, 300), hp=random.randint(80, 750), price=random.randint(10000, 100000), ):
        self.CarMake = make
        self.CarModel = model
        self.CarYear = year
        self.CarSpeed = speed
        self.CarHp = hp
        self.CarPrice = price

    def horn(self):
        print("BEEP!")

    #display all info of the car
    def __str__(self):
        output = "Make: " + self.CarMake + "\n"
        output += "Model: " + self.CarModel + "\n"
        output += "Year: " + str(self.CarYear) + "\n"
        output += "Max speed (km/h): " + str(self.CarSpeed) + "\n"
        output += "Horsepower:" + str(self.CarHp) + "\n"
        output += "Price: $" + str(self.CarPrice) + "\n"
        return output