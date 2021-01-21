#Name: Alex
#Course: ICS3U

#Importing the turtle and setting it up.

import turtle

x = turtle.Turtle()

turtle.screensize(500,500)

x.speed(100)

x.pensize(10)
#Backgrounds

turtle.bgcolor('light sky blue')


#House

#Rectangle


x.penup()
x.sety(-115)
x.setx(-137.5)

x.pendown()
x.fillcolor('sandy brown')
x.begin_fill()

for i in range(1,3):
    x.fd(300)
    x.rt(90)
    x.forward(200)
    x.right(90)
    

x.end_fill()

#Triangle (roof)
x.fillcolor('antique white')

x.begin_fill()
x.bk(46)
x.lt(45)

for i in range(1,2):
    x.fd(275)
    x.rt(90)
    x.fd(275)
    x.rt(135)
    x.fd(345)
x.end_fill()

#Door of the house
x.penup()
x.rt(180)
x.fd(177.5)
x.rt(90)
x.fd(200)
x.lt(90)
x.pendown()
x.fillcolor('tan')
x.begin_fill()
for i in range(1,3):
    x.fd(70)
    x.lt(90)
    x.forward(100)
    x.lt(90)
x.end_fill()

#window
x.fillcolor('dodger blue')

x.penup()
x.rt(180)
x.fd(130)
x.rt(90)
x.fd(80)
x.pendown()
x.begin_fill()
for i in range(1,3):
    x.fd(80)
    x.rt(90)
    x.forward(80)
    x.right(90)

x.end_fill()
#the lines inside window
x.fd(40)
x.rt(90)
x.fd(80)
x.bk(40)
x.lt(90)
x.fd(40)
x.bk(80)

#The sun
x.penup()
x.sety(350)
x.setx(-600)
x.pendown()

x.fillcolor('yellow')
x.begin_fill()
for i in range(1,5):
    x.rt(90)
    x.fd(125)

x.end_fill()

#Mountains in theback
x.penup()
x.sety(200)
x.setx(-125)
x.rt(45)
x.pendown()
x.bk(200)
x.fd(200)

for i in range(1,4):
    x.fd(175)
    x.rt(90)
    x.fd(175)
    x.lt(90)
    
x.rt(90)
x.fd(150)
x.lt(135)
x.penup()
x.fd(200)
x.lt(90)
x.fd(200)

for i in range(1,4):
    x.pendown()
    x.fd(61)
    x.penup()
    x.fd(187)

#trees

#Tree #1
x.fillcolor('peru')

x.sety(-325)
x.setx(-550)
x.rt(90)
x.pendown()
x.begin_fill()
for i in range(1,3):
    x.fd(60)
    x.rt(90)
    x.forward(25)
    x.rt(90)
x.end_fill()

x.fd(60)

x.fillcolor('green')
x.lt(90)
x.fd(45)
x.begin_fill()
x.rt(105)
x.fd(220)
x.bk(220)
x.rt(75)
x.fd(115)
x.lt(105)
x.fd(220)
x.end_fill()
x.rt(15)



#Tree #2
x.fillcolor('peru')
x.penup()
x.sety(-375)
x.setx(-430)
x.pendown()
x.begin_fill()
for i in range(1,3):
    x.fd(60)
    x.rt(90)
    x.forward(25)
    x.rt(90)
x.end_fill()

x.fd(60)

x.fillcolor('green')
x.lt(90)
x.fd(45)
x.begin_fill()
x.rt(105)
x.fd(220)
x.bk(220)
x.rt(75)
x.fd(115)
x.lt(105)
x.fd(220)
x.end_fill()
x.rt(15)

#tree 3
x.fillcolor('peru')
x.penup()
x.sety(-310)
x.setx(-300)
x.pendown()
x.begin_fill()
for i in range(1,3):
    x.fd(60)
    x.rt(90)
    x.forward(25)
    x.rt(90)
x.end_fill()

x.fd(60)

x.fillcolor('green')
x.lt(90)
x.fd(45)
x.begin_fill()
x.rt(105)
x.fd(220)
x.bk(220)
x.rt(75)
x.fd(115)
x.lt(105)
x.fd(220)
x.end_fill()
x.rt(15)

#tree 4
x.fillcolor('peru')
x.penup()
x.sety(-310)
x.setx(300)
x.pendown()
x.begin_fill()
for i in range(1,3):
    x.fd(60)
    x.rt(90)
    x.forward(25)
    x.rt(90)
x.end_fill()

x.fd(60)

x.fillcolor('green')
x.lt(90)
x.fd(45)
x.begin_fill()
x.rt(105)
x.fd(220)
x.bk(220)
x.rt(75)
x.fd(115)
x.lt(105)
x.fd(220)
x.end_fill()
x.rt(15)

#Tree #5
x.fillcolor('peru')
x.penup()
x.sety(-375)
x.setx(430)
x.pendown()
x.begin_fill()
for i in range(1,3):
    x.fd(60)
    x.rt(90)
    x.forward(25)
    x.rt(90)
x.end_fill()

x.fd(60)

x.fillcolor('green')
x.lt(90)
x.fd(45)
x.begin_fill()
x.rt(105)
x.fd(220)
x.bk(220)
x.rt(75)
x.fd(115)
x.lt(105)
x.fd(220)
x.end_fill()
x.rt(15)

#Tree #6
x.fillcolor('peru')
x.penup()
x.sety(-315)
x.setx(550)
x.pendown()
x.begin_fill()
for i in range(1,3):
    x.fd(60)
    x.rt(90)
    x.forward(25)
    x.rt(90)
x.end_fill()

x.fd(60)

x.fillcolor('green')
x.lt(90)
x.fd(45)
x.begin_fill()
x.rt(105)
x.fd(220)
x.bk(220)
x.rt(75)
x.fd(115)
x.lt(105)
x.fd(220)
x.end_fill()
x.rt(15)





    



































