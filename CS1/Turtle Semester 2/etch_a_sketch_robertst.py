from turtle import *


class Application:
    def __init__(self):
        self.alex = Turtle()
        self.alex.shape("turtle")
        self.alex.speed(9)
        self.window = Screen()
        self.window.title("Turtle Ecth-A-Sketch")
        self.window.bgcolor('grey')
        self.bgcolors = ('grey', 'white', 'maroon')
        self.pensizes = (1, 2, 3, 4, 5)
        self.current_bg = 0
        self.pensize = 1

    def start(self):
        self.window.onkey(self.left, "Left")
        self.window.onkey(self.right, "Right")
        self.window.onkeypress(self.up, "Up")
        self.window.onkeypress(self.down, "Down")
        self.window.onkey(self.toggle_pen, "space")
        self.window.onkey(self.clear, 'C')
        self.window.onkey(self.reset, 'R')
        self.window.onkey(self.change_bgcolor, 'D')
        self.window.onkey(self.undo, 'U')
        self.window.onkey(self.minuspensize, "minus")
        self.window.onkey(self.pluspensize, 'plus')
        self.window.onkey(self.red, "r")
        self.window.onkey(self.green, 'g')
        self.window.onkey(self.black, 'b')
        self.window.onkey(self.yellow, 'y')
        self.window.listen()
        self.window.mainloop()

    def left(self):
        self.alex.lt(90)

    def right(self):
        self.alex.rt(90)

    def up(self):
        if self.alex.xcor() >= 325 or self.alex.xcor() <= -325 or self.alex.ycor() >= 270 or self.alex.ycor() <= -270:
            self.alex.back(5)
        else:
            self.alex.fd(5)

    def down(self):
        if self.alex.xcor() >= 325 or self.alex.xcor() <= -325 or self.alex.ycor() >= 270 or self.alex.ycor() <= -270:
            self.alex.fd(5)
        else:
            self.alex.bk(5)
    
    def toggle_pen(self):
        if self.alex.isdown():
            self.alex.penup()
        else:
            self.alex.pendown()
    
    def clear(self):
        self.alex.clear()
    
    def reset(self):
        self.alex.penup()
        self.alex.goto(0, 0)
        self.alex.pendown()
    
    def undo(self):
        for _ in range(5):
            self.alex.undo()
    
    def change_bgcolor(self):
        self.current_bg = (self.current_bg + 1)%3
        self.window.bgcolor(self.bgcolors[self.current_bg])
    
    def minuspensize(self):
        self.pensize = (self.pensize - 1)%5
        self.alex.pensize(self.pensize)

    def pluspensize(self):
        self.pensize = (self.pensize + 1)%5
        self.alex.pensize(self.pensize)


    def red(self):
        self.alex.color("red")

    def green(self):
        self.alex.color("green")

    def black(self):
        self.alex.color("black")

    def yellow(self):
        self.alex.color("yellow")


def main():
    app = Application()
    app.start()


if __name__ == "__main__":
    main()
