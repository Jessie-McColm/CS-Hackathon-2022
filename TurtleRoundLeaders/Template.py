import turtle
import os
##### Config #####
groupname="YourGroupName"
turtle.left(90)
turtle.speed(0) # 0-10, 0 fastest, 10 slowest. Save precious time only running slow if you need to.
turtle.colormode(255) # allows you to use (r, g, b) tuples as colors, with values 0-255
turtle.pendown()
turtle.circle(50,180)
turtle.forward(50)
turtle.left(160)
for i  in range (0,5):
    turtle.right(140)
    turtle.forward(30)
    turtle.left(140)
    turtle.forward(30)
turtle.left(23)
turtle.forward(60)
turtle.penup()
turtle.left(90)
turtle.forward(25)
turtle.pendown()
turtle.circle(10)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.circle(10)


def arc(length,angle,count):
    for x in range(count):
        turtle.forward(length)
        turtle.right(angle)

def rect(length,width,angle1, angle2):
    turtle.left(angle1)
    turtle.forward(length)
    turtle.left(angle2)
    turtle.forward(width)
    turtle.left(180-angle2)
    turtle.forward(length)
    turtle.left(angle2)
    turtle.forward(width)
   
def battlements(length, count):
    for x in range(count):
        turtle.left(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        if x + 1 < count:
            turtle.left(90)
            turtle.forward(length)

turtle.penup()
turtle.goto(-200,-300)
turtle.pendown()
turtle.setheading(0)
rect(20,100,90,90)
turtle.penup()
turtle.goto(-200,-280)
turtle.setheading(0)
turtle.pendown()
rect(20,100,90,90)
turtle.penup()
turtle.goto(-200,-260)
turtle.setheading(0)
turtle.pendown()
rect(20,100,90,90)
turtle.update()
turtle.penup()
turtle.goto(-190,-240)
turtle.setheading(0)
turtle.pendown()
rect(20,120,90,90)
turtle.penup()
turtle.goto(-200,-220)
turtle.setheading(0)
turtle.pendown()
rect(20,100,90,90)
turtle.penup()
turtle.goto(-200,-200)
turtle.setheading(0)
turtle.pendown()
rect(20,100,90,90)
turtle.penup()
turtle.goto(-200,-180)
turtle.setheading(0)
turtle.pendown()
rect(20,100,90,90)
turtle.penup()
turtle.goto(-200,-160)
turtle.setheading(0)
turtle.pendown()
rect(20,100,90,90)
turtle.penup()
turtle.goto(-200,-140)
turtle.setheading(0)
turtle.pendown()
rect(20,100,90,90)







########### export #########
outputpath=os.path.dirname(os.path.abspath(__file__))+os.path.sep+groupname+'.ps'
turtle.getscreen().getcanvas().postscript(file=outputpath)
turtle.done()