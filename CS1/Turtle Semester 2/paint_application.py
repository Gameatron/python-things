from turtle import *


class Application:
    def __init__(self):
        self.brush = Turtle(visible=True)
        self.brush.shape("square")
        self.colors = ("black", "red", "orange", "yellow",
                       "green", "blue", "purple", "maroon",
                       "teal", "brown", "grey", "turquoise")
        self.current_color = "black"
        self.brush.color("black")
        self.brush.turtlesize(.5)
        self.current_turtlesize = .5
        self.brush.pensize(5)
        self.current_pensize = 5
        self.window = Screen()
        self.window.title("Paint Application")
        self.window.tracer(0, 0)  # No animation, buffered
        self.eraser_toggled = False
        self.make_palate()

    def start(self):
        self.make_palate()
        self.window.onclick(self.move)
        self.brush.ondrag(self.paint)
        self.window.onclick(self.choose_color, btn=3)
        self.window.onclick(self.toggle_erase, btn=2)
        self.window.onkey(self.clear, "U")
        self.window.onkey(self.increase_pen, 'plus')
        self.window.onkey(self.decrese_pen, 'minus')
        self.window.listen()
        self.window.mainloop()

    def move(self, x, y):
        if self.check_coords(x, y):
            pass
        else:
            self.brush.penup()
            self.brush.goto(x, y)
            self.brush.pendown()
            self.window.update()

    def paint(self, x, y):
        if self.check_coords(x, y):
            pass
        else:
            self.brush.goto(x, y)
            self.brush.dot(self.current_pensize)
            self.window.update()

    def change_color(self, x, y):
        self.current_color = (self.current_color + 1) % len(self.colors)
        self.brush.color(self.colors[self.current_color])
        self.window.update()

    def make_palate(self):
        y = 225
        x = -((30*len(self.colors))/2)
        self.brush.pensize(5)
        for color in self.colors:
            self.draw_color_square(x, y, color)
            x += 30
        self.brush.penup()
        self.brush.goto(-500, 200)
        self.brush.pendown()
        self.brush.fd(1000)
        self.brush.penup()
        self.brush.home()
        self.brush.pendown()
        self.brush.color(self.current_color)
        self.brush.pensize(self.current_pensize)
        self.window.update()

    def draw_color_square(self, x, y, color):
        self.brush.penup()
        self.brush.goto(x, y)
        self.brush.pendown()
        self.brush.color(color)
        self.brush.begin_fill()
        for _ in range(4):
            self.brush.fd(20)
            self.brush.lt(90)
        self.brush.end_fill()

    def choose_color(self, x, y):
        xval = -((30*len(self.colors))/2)
        for color in self.colors:
            if x >= xval and x <= xval+20 and y >= 225 and y <= 245:
                self.brush.color(color)
                self.current_color = color
                self.window.update()
                return
            else:
                xval += 30

    def check_coords(self, x, y):
        if x > -1000 and x < 1000 and y > 200:
            return True
        else:
            pass

    def toggle_erase(self, x, y):
        if self.eraser_toggled == False:
            self.brush.color("white")
            self.eraser_toggled = True
            self.window.update()
        elif self.eraser_toggled:
            self.brush.color(self.colors[self.current_color])
            self.eraser_toggled = False
            self.window.update()

    def clear(self):
        self.brush.clear()
        self.make_palate()

    def increase_pen(self):
        if self.current_pensize == 10:
            pass
        else:
            self.current_pensize += 1
            self.current_turtlesize += .1
            self.brush.pensize(self.current_pensize)
            self.brush.turtlesize(self.current_turtlesize)
            self.window.update()

    def decrese_pen(self):
        if self.current_pensize == 1:
            pass
        else:
            self.current_pensize -= 1
            self.current_turtlesize -= .1
            self.brush.pensize(self.current_pensize)
            self.brush.turtlesize(self.current_turtlesize)
            self.window.update()


def main():
    app = Application()
    app.start()


if __name__ == "__main__":
    main()
