from turtle import *
from random import randint, choice

##################################

def make_line(t, length):
    t.forward(length)
    t.backward(length)

def move_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def move_rand(t, x, y, z, v):
    t.penup()
    x = randint(x, y)
    y = randint(z, v)
    t.goto(x, y)
    t.pendown()

def draw_f_star(t, size):
    t.color(choice(star_colors))
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(145)
    t.end_fill()

def draw_hill(t):
    move_to(t, -480, 0)
    t.color('green')
    t.begin_fill()
    for i in range(2):
        t.forward(480 * 2)
        t.right(90)
        t.forward(400)
        t.right(90)
    t.end_fill()

def night_sky(t):
    bgcolor('black')
    
def draw_ocean(t):
    t.color('#0077be')
    move_to(t, -480, 100)
    t.begin_fill()
    for i in range(2):
        t.forward(480 * 2)
        t.right(90)
        t.forward(150)
        t.right(90)
    t.end_fill()

def draw_beach(t):
    t.color('#c2b280')
    move_to(t, -480, 0)
    t.begin_fill()
    for i in range(2):
        t.forward(480 * 2)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()
    
def draw_moon(t):
    t.color('gray')
    move_to(t, 250, 250)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    
def limbs(t, length):
    t.right(22.5)
    make_line(t, length)
    t.left(45)
    make_line(t, length)
    t.right(22.5)
    
def draw_person(t, size):
    t.color('black')
    t.seth(270)
    t.forward(size / 2)
    limbs(t, size / 2)
    t.forward(size / 2)
    limbs(t, size / 2)
    t.right(180)
    t.forward(size / 1.5)
    t.seth(360)
    t.begin_fill()
    t.circle(size / 4)
    t.end_fill()
    
def draw_all_people(t, size):
    for i in range(2):
        move_rand(t, -370, 370, -185, -100)
        draw_person(t, size)

def draw_all_stars(t):
    for i in range (25):
        size = randint(10, 50)
        move_rand(t, -370, 370, 185, 370)
        draw_f_star(t, size)
        
def draw_scene(t):
    night_sky(t)
    draw_hill(t)
    draw_ocean(t)
    draw_beach(t)
    draw_moon(t)
    draw_all_people(t, 50)
    draw_all_stars(t)


##################################

t = Turtle()
t.speed(0)
star_colors = ['gainsboro', 'light gray', 'silver', 'white', 'white smoke']

draw_scene(t)


