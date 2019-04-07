from turtle import *
from random import randint, choice

#################################

def move_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown

def draw_fish(t, size, col):
    t.color(col)
    t.dot(size)
    t.left(30)
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.right(120)
    t.end_fill()
    
def draw_all_fish(t):
    fish_colors = ['red', 'orange', 'yellow']
    for i in range(10):
        x = randint(-470, 470)
        y = randint(-100, 350)
        move_to(t, x, y)
        draw_fish(t, 20, choice(fish_colors))
                    
                    
def sand(t):
    move_to(t, -480, -300)
    t.color('yellow')
    t.begin_fill()
    for i in range(2):
        t.forward(480 * 2)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()

def kelp(t):
    t.color('green')
    t.left(90)
    for i in range(3):
        t.circle(50, 60)
        t.circle(-50, 60)
        
def draw_all_kelp(t):
    for i in range(10):
        x = randint(-470, 470)
        y = randint(-100, 350)
        move_to(t, x, y)
        draw_kelp(t, 20)

def draw_ocean(t):
    bgcolor('blue')
    draw_all_fish(t)
    draw_all_kelp(t)

################################

t = Turtle()
t.speed(0)

