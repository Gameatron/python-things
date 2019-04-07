from turtle import *
t = Turtle()
t.shape("turtle")
SCALE = 10


#Use command for _ in range(value): then block of indented code to repeat a process according to the value you put in 
for _ in range(100):
    t.forward(SCALE * 10)
    t.right(90)