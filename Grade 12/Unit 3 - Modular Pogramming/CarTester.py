# Program Name: CarTester.py
# Date: April 11, 2020
# Programmer: Alex Dorodko
#Main file to display objets

from Car import Car

car1 = Car()
car2 = Car("Mini", "F56", 2019, 201)
car3 = Car("Mini", "F56", 2019, 201, 139, 36000)

# Print the details of each dog
print("\n------The First Car------")
print(car1)

print("\n------The Second Car------")
print(car2)

print("\n------The Third Car------")
print(car3)

print("\nThe third car says:")
car3.horn()

