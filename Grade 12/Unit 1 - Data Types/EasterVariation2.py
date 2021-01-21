# Program Easter Variation
# Date: February 5th, 2020
# Programmer: Alex Dorodko
# Description: By entering the year, the program calculates for you what day easter will be.

#input
year = int(input("Please enter the year: "))

#calculations
a = int(year/100)
b = year%100
c = int((3*(a+25))/4)
d = (3*(a+25))%4
q = int((8*(a+11))/25)
f = (5*a+b)%19
g = (19*f+c-q)%30
h = int((f+11*g)/319)
j = int((60*(5-d)+b)/4)
k = (60*(5-d)+b)%4
n = (2*j-k-g+h)%7
month = (g-h+n+114)/31
p = (g-h+n+114)%31
day = (p+1)

#output
if month == 3:
    monthname = "March"

else:
    monthname = "April"
print()
print("Easter will fall on Sunday, ", monthname, day, year)
