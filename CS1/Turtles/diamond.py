from turtle import *
from random import randint, choice

def step(t, side_length):
    for i in range(1):
        t.forward(side_length)
        t.left(90)
        t.forward(side_length)
        t.right(90)

def draw_side(t, side_length):
    for i in range(3):
        step(t, side_length)

    t.forward(side_length)
    t.left(90)

def diamond(t, side_length):
    for i in range(4):
        draw_side(t, side_length)

def move_rand(t):
    t.penup()
    x = randint(-370, 370)
    y = randint(-370, 370)
    t.goto(x, y)
    t.pendown()

############################################

t = Turtle()
t.speed(0)
bgcolor("black")
colors = ['blue', 'red', 'purple', 'green', 'beige', 'yellow']

for i in range(100):
    size = randint(10, 100)
    move_rand(t)
    diamond(t, size)
    t.color(choice(colors))