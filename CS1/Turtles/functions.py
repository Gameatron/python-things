from turtle import
def move_to(t, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def draw_square(t):
    for i in range(4):
        t.forward(100)
        t.left(90)

def draw_square(t, side_length):
    for i in range(4):
        t.forward(side_length)
        t.left(90)

t = Turtle()
t.speed(0)

move_to(t,-400,200)

    
move_to(t,-400,100)

for i in range(8):
    draw_square(t,100)
    t.forward(100)