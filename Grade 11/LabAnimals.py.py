#Name: Alex
#Course: ICS3U
#Unit 4 - Assignment #2

#Setting up the text

print("Lab Animals")
print("===========")
print()
print()
print("At present there are X animals in the lab and enough food for Y animals.")
print("At the end of every hour the population doubles, and enough food is added to")
print("support Z more animals. During any hour the animals will eat enough food for")
print("only themselves.")
print("This program will determine when the population will outgrow the food supply.")
print()
#Getting the vaiable values I need through imput
print()
initial_animals = int(input("Enter the initial animal population (X): "))
while (initial_animals < 0):
       initial_animals = int(input("Invalid. Enter the initial animal population (X): "))

initial_food = int(input("Enter the initial food supply (Y): "))
while (initial_food < 0):
       initial_food = int(input("Invalid. Enter the initial food supply (Y): "))
added_food = int(input("Enter the ammount of food added each hour (Z): "))
while (added_food < 0):
       added_food = int(input("Invalid. Enter the ammount of food added each hour (Z): "))

#test
temp = initial_animals

#xx will be animals at end
end_animals = 0
#yy will be food at end
end_food = 0
#Will count how many times the loop ran
hours = 0
print()
print("Hour    Animals at Start        Food at Start   Food at End     Animals at End")

while (end_food >= end_animals):
       #counts how many times the loop has ran
       hours = hours+1
       #Animals part of loop
       initial_animals = initial_animals*2 #animals x2 each hour
       if (hours == 1):
           initial_animals = initial_animals//2 #fix for an issue where it would say on the 1st hour there are 20 animals insread of 10
           temp = initial_animals #Also used as a fix for later

       end_animals = initial_animals*2 #animals at end
       #Food part of loop
       #This loop is used so on the first our the initial food is not 4000, but 1000.
       if (hours == 1):
           initial_food = initial_food
           end_food = initial_food-initial_animals+added_food

       elif (hours >= 2):
           initial_food = initial_food+added_food-initial_animals
           end_food = initial_food+added_food-temp
       #print("Number of animals beggining:",initial_animals , "Ammount of food at beggining:", initial_food)
       #print("Numer of animals end:", end_animals, "Number of food end", end_food)
       print("{0:<4}\t{1:<18}\t{2:<13}\t{3:<10}\t{4:<10}".format(hours, initial_animals, initial_food, end_food, end_animals))
print()
print("By hour", hours, "the population outgrows the food supply")
