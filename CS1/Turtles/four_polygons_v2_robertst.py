from turtle import *

def move_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_line(t):
    t.forward(500)
    t.backward(1000)
    t.penup()
    t.goto(0, 0)
    t.pendown()

def draw_octogon(t, side_length):
    for i in range(8):
        t.forward(side_length)
        t.right(45)
        
def draw_pentagon(t, side_length):
    for i in range(5):
        t.backward(side_length)
        t.left(72)
        
def draw_triangle(t, side_length):
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
        
def draw_hexagon(t, side_length):
    for _ in range(6):
        t.backward(side_length)
        t.right(60)
        
def draw_star(t, side_length):
    for _ in range(5):
        t.forward(side_length)
        t.right(144)

def draw_cont_star(t, side_length, times):
    for side_length in range(times):
        t.forward(side_length * 20)
        t.right(144)

def draw_8star(t, side_length):
    for i in range(8):
        t.forward(50)
        t.left(135)
        t.forward(75)
        t.left(90)

t = Turtle()
t.speed(0)
bgcolor("black")
t.shape("turtle")

t.color("maroon")
for i in range(24):
    draw_triangle(t, 100)
    t.right(15)

move_to(t, 200, 200)

t.color("skyblue")
for i in range(30):
    draw_star(t, 125)
    t.right(12)
    
move_to(t, -200, 200)

t.color("red")
for i in range(32):
    draw_octogon(t, 50)
    t.right(11.25)

move_to(t, -200, -200)

t.color("magenta")
for i in range(16):
    draw_pentagon(t, 75)
    t.right(23)
    
move_to(t, 200, -200)

t.color("grey")
for i in range(48):
    draw_hexagon(t, 75)
    t.right(7.5)
    
t.color("black")
t.pensize(6)

t.penup()
t.home()
t.pendown()

for i in range(24):
    draw_triangle(t, 100)
    t.right(15)
    
move_to(t, 200, 200)

for i in range(30):
    draw_star(t, 125)
    t.right(12)
    
move_to(t, -200, 200)

for i in range(32):
    draw_octogon(t, 50)
    t.right(11.25)

move_to(t, -200, -200)

for i in range(18):
    draw_pentagon(t, 75)
    t.right(23)
    
move_to(t, 200, -200)

for i in range(48):
    draw_hexagon(t, 75)
    t.right(7.5)
    
t.penup()
t.home()
t.pendown()
t.color("yellow")
t.pensize(1)
draw_cont_star(t, 100, 100)

t.penup()
t.home()
t.pendown()
t.color("black")
draw_cont_star(t, 100, 100)

t.color("green")
for i in range(100):
    draw_line(t)
    t.right(2)


t.home()
t.right(180)
t.color("black")
for i in range(46):
    draw_line(t)
    t.left(4)
    
t.left(2)
for i in range(46):
    draw_line(t)
    t.left(4)
    
t.clear()
