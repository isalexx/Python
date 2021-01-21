# Name: U1L1 - eastercalc
# Date: Feb. 4, 2019
# Programmer: Jeff Carron
# Description: The following program will find the day and month
#              of Easter Sunday for any given year.

# Ask user for year
print("Easter Date Calculator\n")
year = int(input("Please enter a year: "))

# Calculations
a = year % 19
b = int(year / 100)
c = year % 100
d = int(b / 4)
e = b % 4
f = int((8 + b) / 25)
g = int((b - f + 1)/3)
h = (19 * a + b - d - g + 15) % 30
i = int(c / 4)
k = c % 4
j = (32 + 2*e + 2*i - h - k)%7
m = int((a + 11*h + 22*j)/451)
month = int((h + j -7*m + 114)/31)
p = (h + j - 7*m + 114)%31
day = p + 1

# determine the month in String format
if month == 3:
    monthStr = "March"
else:
    monthStr = "April"

# Display the results
print("\nEaster will fall on Sunday, ", monthStr, " ", day, ", ", year, sep="")
