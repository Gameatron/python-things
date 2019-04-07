from turtle import *
t = Turtle()
t.speed(1000)
bgcolor("black")

t.color("skyblue")
for i in range(250):
    t.forward(i * 5)
    t.right(90)
for i in range (1000):
    t.forward(i * 5)
    t.left(90)