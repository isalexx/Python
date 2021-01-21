#Name: Alex
#Course Code: ICS3U
#Unit 3 - Assignment #1

#Chess board

print("┏━━━━━━━━━┓")
print("▌  ██  ██  ██  ██ ▌8")
print("▌██  ██  ██  ██   ▌7")
print("▌  ██  ██  ██  ██ ▌6")
print("▌██  ██  ██  ██   ▌5")
print("▌  ██  ██  ██  ██ ▌4")
print("▌██  ██  ██  ██   ▌3")
print("▌  ██  ██  ██  ██ ▌2")
print("▌██  ██  ██  ██   ▌1")
print("┗1-2-3-4-5-6-7-8┛")


#print("Clarification. This software is not to play chess, but rather tell you whether you can move a game piece legaly from one point to another within game rules. You are able to use the chessboard above as a little helping hand to figure out the cordinates.")


    
#Requesting position of the square
column = int(input("Please enter the column of the first square (top to bottom): "))


while (column > 8 or column < 1):
       column = int(input("Invalid coordinate.Please enter the column of the first square: "))

row = int(input("Please enter the row of the first square (left to right): "))

while (row > 8 or row < 1):
       row = int(input("Invalid coordinate. Please enter the row of the first square: "))


#Total of the two
value = column+row


if (value >= 10):
    last_int = value%10

elif (value < 10):
      last_int = value


if (last_int == 0 or last_int == 2 or last_int == 4 or last_int == 6 or last_int == 8):
      print("The square is BLACK")

elif (last_int == 1 or last_int == 3 or last_int == 5 or last_int == 7 or last_int == 9):
    print("The square is WHITE")


column_2 = int(input("Please enter the column of the second square: "))

while (column_2 > 8 or column_2 < 1):
       column_2 = int(input("Invalid cordinate. Please enter the column of the second square: "))

row_2 = int(input("Please enter the row of the second square: "))

while (row_2 > 8 or row_2 < 1):
       row_2 = int(input("Invalid cordinate. Please enter the row of the second square: "))

#Rook Section

if (row == row_2 and column != column_2):
    print("The rook can move")

elif (row != row_2 and column == column_2):
      print("The rook can move")

elif (row == row_2 and column == column_2):
      print("The rook can move")

elif (row != row_2 and column != column_2):
      print("The rook can't move")

#Pawn
#Assuming this is the pawn's 2nd move or later, it can only move up legaly one squre assuming there are no other pieces.

if (row+1 == row_2 and column == column_2):
    print("The pawn can move")

else:
    print("The pawn can't move")


#King

if (row == row_2 and column == column_2):
    print("The king can move")

elif (row+1 == row_2 and column == column_2):
      print("The king can move")

elif (row-1 == row_2 and column == column_2):
      print("The king can move")

elif (column+1 == column_2 and row == row_2):
      print("The king can move")

elif (column-1 == column_2 and row == row_2):
      print("The king can move")

elif (row+1 == row_2 and column+1 == column_2):
      print("The king can move")

elif (row-1 == row_2 and column-1 == column_2):
      print("The king can move")

elif (row+1 == row_2 and column-1 == column_2):
      print("The king can move")

elif (row-1 == row_2 and column+1 == column_2):
      print("The king can move")

else:
      print("The king can't move")


#Knight

if (column_2 == column-1 and row_2 == row+2):
    print("the knight can move")

elif (column_2 == column+1 and row_2 == row+2):
      print("the knight can move")

elif (column_2 == column-1 and row_2 == row-2):
      print("the knight can move")

elif (column_2 == column+1 and row_2 == row-2):
      print("the knight can move")

elif (column_2 == column+2 and row_2 == row+1):
      print("the knight can move")

elif (column_2 == column+2 and row_2 == row-1):
      print("the knight can move")

elif (column_2 == column-2 and row_2 == row+1):
      print("the knight can move")

elif (column_2 == column-2 and row_2 == row-1):
      print("The knight can move")

else:
    print("The knight can't move")


#Bishop

x = abs(row-row_2)

y = abs(column-column_2)

if (x == y):
    print("The bishop can move")

else:
    print("The bishop can't move")


#Queen

#rook sample of code
if (row == row_2 and column != column_2):
    print("The queen can move")

elif (row != row_2 and column == column_2):
      print("The queen can move")

elif (row == row_2 and column == column_2):
      print("The queen can move")

#king sample of code
elif (row == row_2 and column == column_2):
      print("The queen can move")

elif (row+1 == row_2 and column == column_2):
      print("The queen can move")

elif (row-1 == row_2 and column == column_2):
      print("The queen can move")

elif (column+1 == column_2 and row == row_2):
      print("The queen can move")

elif (column-1 == column_2 and row == row_2):
      print("The queen can move")

elif (row+1 == row_2 and column+1 == column_2):
      print("The queen can move")

elif (row-1 == row_2 and column-1 == column_2):
      print("The queen can move")

elif (row+1 == row_2 and column-1 == column_2):
      print("The queen can move")

elif (row-1 == row_2 and column+1 == column_2):
      print("The queen can move")

#bishop sample of code
elif (x == y):
    print("The queen can move")

else:
    print("The queen can't move")

vfxv = input("Press Enter to close the program")





