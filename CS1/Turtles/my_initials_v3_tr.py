from turtle import *
SCALE = 10
t = Turtle()
bgcolor("red")
t.shape("turtle")

t.penup()
t.goto(SCALE * -20,SCALE * 0)
t.pendown()

#T
t.left(90)
t.forward(SCALE * 10)
t.left(90)
t.forward(SCALE * 5)
t.backward(SCALE * 10)

t.penup()
t.left(90)
t.forward(SCALE * 10)
t.left(90)
t.forward(SCALE * 2.5)

#A
t.pendown()
t.left(90)
t.forward(SCALE * 10)
t.right(90)
t.forward(SCALE * 5)
t.right(90)
t.forward(SCALE * 5)
t.right(90)
t.forward(SCALE * 5)
t.backward(SCALE * 5)
t.left(90)
t.forward(SCALE * 5)

t.penup()
t.left(90)
t.forward(SCALE * 2.5)
t.pendown()

#K
t.left(90)
t.forward(SCALE * 10)
t.backward(SCALE * 5)
t.right(45)
t.forward(SCALE * 6)
t.backward(SCALE * 6)
t.right(90)
t.forward(SCALE * 7.5)
t.backward(SCALE * 7.5)
t.right(45)
t.forward(SCALE * 5)
t.left(90)

t.penup()
t.forward(100)
t.pendown()

#O
t.circle(SCALE * 5)

t.penup()
t.forward(SCALE * 7.5)
t.pendown()

#D
t.left(90)
t.fd(SCALE * 10)
t.right(90)
t.fd(SCALE * 2.5)
t.right(45)
t.forward(SCALE * 2.5)
t.right(45)
t.forward(SCALE * 6.5)
t.right(45)
t.forward(SCALE * 2.5)
t.right(45)
t.forward(SCALE * 2.5)
t.right(180)

t.penup()
t.forward(SCALE * 7.5)
t.pendown()

#A
t.left(90)
t.forward(SCALE * 10)
t.right(90)
t.forward(SCALE * 5)
t.right(90)
t.forward(SCALE * 5)
t.right(90)
t.forward(SCALE * 5)
t.backward(SCALE * 5)
t.left(90)
t.forward(SCALE * 5)