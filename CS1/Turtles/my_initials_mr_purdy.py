# designates a comment --- Python IGNORES comments, they
# are strictly for HUMANS to use!  You should get in
# the habit of ALWAYS commenting your code
# (you WILL NOT remember why/how you did certain things
# so it's best to leave comments for "future YOU")

# import turtle module and create the turtle
from turtle import *
t = Turtle()


# relocate the turtle to its starting position (to center on the screen)
t.penup() # lifts the pen up so the turtle doesn't draw a line
t.goto(-300,-50) # makes the turtle go straight to the specified coordinate
t.pendown() # puts the pen down so the turtle will draw a line as it moves

# draw M - turtle is facing right when finished
t.left(90)
t.forward(100)
t.right(135)
t.forward(50)
t.left(90)
t.forward(50)
t.right(135)
t.forward(100)
t.left(90)

# move to draw next letter
t.penup()
t.forward(25)
t.pendown()

# draw R - turtle is facing right when finished
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.left(135)
t.forward(70)
t.left(45)

# move to draw next letter
t.penup()
t.forward(75)
t.pendown()

# draw P - turtle is facing right when finished
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)

# move to draw next letter
t.penup()
t.forward(75)
t.pendown()

# draw U - turtle is facing right when finished
t.left(90)
t.forward(100)
t.backward(100)
t.right(90)
t.forward(50)
t.left(90)
t.forward(100)
t.backward(100)
t.right(90)

# move to draw next letter
t.penup()
t.forward(25)
t.pendown()

# draw R - turtle is facing right when finished
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.left(135)
t.forward(70)
t.left(45)

# move to draw next letter
t.penup()
t.forward(25)
t.pendown()

# draw D - turtle is facing right when finished
t.left(90)
t.forward(100)
t.right(90)
t.forward(25)
t.right(45)
t.forward(35)
t.right(45)
t.forward(50)
t.right(45)
t.forward(35)
t.right(45)
t.forward(25)
t.right(180)

# move to draw next letter
t.penup()
t.forward(75)
t.pendown()

# draw Y - turtle is invisible when finished
t.penup()
t.forward(25)
t.pendown()
t.left(90)
t.forward(50)
t.left(45)
t.forward(70)
t.backward(70)
t.right(90)
t.forward(70)
t.hideturtle() # hides the turtle






