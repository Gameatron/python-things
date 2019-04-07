from turtle import *
t = Turtle()
bgcolor("black")
t.speed(10)
t.color("blue")
t.shape("turtle")
SCALE = 10

#dividing of each of the four quadrants
t.forward(SCALE * 50)
t.backward(SCALE * 100)
t.goto(SCALE * 0,SCALE * 0)
t.right(90)
t.forward(SCALE * 50)
t.backward(SCALE * 100)
t.left(90)
t.penup()
t.goto(SCALE * -30,SCALE * 30)
t.pendown()
t.color("black")

#creating an octogon
t.color("green")
for _ in range(8):
    t.forward(SCALE * 10)
    t.right(45)
    
#moving to the upper right quadrant
t.penup()
t.goto(SCALE * 30,SCALE * 30)
t.pendown()

#creating a pentagon
t.color("magenta")
for _ in range(5):
    t.backward(SCALE * 10)
    t.left(72)
    
#moving to the lower left quadrant
t.penup()
t.goto(SCALE * -30,SCALE * -30)
t.pendown()

#creating a triangle
t.color("maroon")
for _ in range(3):
    t.forward(SCALE * 10)
    t.left(120)

#moving to the lower right quadrant
t.penup()
t.goto(SCALE * 30,SCALE * -30)
t.pendown()

#creating a hexagon
t.color("grey")
for _ in range(6):
    t.backward(SCALE * 10)
    t.right(60)
    
#its start time
t.penup()
t.goto(SCALE * -7.5,SCALE * 2.5)
t.pendown()
t.color("skyblue")
for _ in range(5):
    t.forward(SCALE * 15)
    t.right(144)
t.hideturtle()