from turtle import *

def box_spiral(t):
    for j in range(250, 0, -25):
        for i in range(2):
            t.forward(j)
            t.left(90)

def clam_shell(t):
    for i in range(10, 100, 10):
        t.circle(i)

def concentric(t):
    for i in range(30, 100, 20):
        t.circle(i)
        t.penup()
        t.seth(270)
        t.fd(20)
        t.pendown()
        t.seth(360)

def squares(t):
    for j in range(1, 10):
        t.seth(270)
        for _ in range(6):
            t.forward(10*j)
            t.rt(90)
        t.seth(270)


def h(t):
    for _ in range(2):
        t.fd(25)
        t.lt(90)
        t.fd(80)
        t.rt(90)
        t.fd(20)
        t.right(90)
        t.fd(180)
        t.right(90)
        t.fd(20)
        t.right(90)
        t.fd(80)
        t.lt(90)
        t.fd(50)
        

def spirograph(t):
    for _ in range(20):
        t.circle(100)
        t.rt(18)

def rotated_squares(t):
    for i in range(1, 13):
        for _ in range(4):
            t.fd(100)
            t.right(90)
        t.right(30)

def circle_square_diag(t):
    t.circle(50)
    t.penup()
    t.fd(-50)
    t.pendown()
    for _ in range(4):
        t.fd(100)
        t.lt(90)
    t.goto(50, 100)
    t.goto(-50, 100)
    t.goto(50, 0)




# DO NOT EDIT BELOW THIS LINE UNLESS INSTRUCTED #
def main():
    #s = Screen()
    funcs = [box_spiral, clam_shell, concentric, squares,
             h, spirograph, rotated_squares, circle_square_diag]
    
    print("Available functions:")
    for i in range(8):
        print(f"{i+1}. {funcs[i].__name__}")
        
    print()
    while True:
        try:
            choice = int(input("Your choice (1-8): "))
            if choice < 1 or choice > 8:
                print("Choice must be between 1 and 8.")
                continue
            break
        except:
            print("Invalid entry.")
    
    terry = Turtle()
    funcs[choice-1](terry)
    mainloop()
    
    
def draw_all():
    funcs = [box_spiral, clam_shell, concentric, squares,
             h, spirograph, rotated_squares, circle_square_diag]
    
    colors = ['red','orange','yellow','green','blue','purple','black','gray']
    
    terry = Turtle()
    for i, func in enumerate(funcs):
        terry.penup()
        terry.goto(0,0)
        terry.pendown()
        terry.color(colors[i])
        func(terry)
    
    
if __name__ == "__main__":
   main()
   
    