from turtle import *
from random import randint, choice

##############################

#a way of going to the home point with out making marks

def go_home(t):
    t.penup()
    t.home()
    t.pendown()

def rand_walk(t, steps):
    
    for i in range(steps):
        #generate randome number
        direction = randint(0, 3)
        #have turtle face a random direction
        if direction == 0:
            t.seth(0)
            t.color('blue')
            
        if direction == 1:
            t.seth(90)
            t.color('green')
            
        if direction == 2:
            t.seth(180)
            t.color('white')
        
        if direction == 3:
            t.seth(270)
            t.color('yellow')
        
        #move forward
        t.fd(50)
        
        #making the turtle stay inside the margins
        
        if t.xcor() > 350:
            go_home(t)
        
        if t.xcor() < -350:
            go_home(t)
            
        if t.ycor() > 350:
            go_home(t)
        
        if t.ycor() < -350:
            go_home(t)
        
    
#############################################

colors = ('red', 'blue', 'green', 'white')

bgcolor('black')
t= Turtle()
t.speed(0)

rand_walk(t, 1000)