from turtle import *


class Application:
    def __init__(self):
        self.brush = Turtle()
        self.brush.shape("circle")
        self.window = Screen()
        self.window.tracer(0, 0)
        self.window.title("Click to Draw")

    def start(self):
        self.window.onclick(self.paint)
        self.window.onclick(self.move, btn=3)
        self.window.onkey(self.clear, "n")
        self.window.onkey(self.circle, "c")
        self.window.onkey(self.square, "s")
        self.window.listen()
        self.window.mainloop()

    def paint(self, x, y):
        self.brush.goto(x, y)
        self.window.update()

    def move(self, x, y):
        self.brush.penup()
        self.brush.goto(x, y)
        self.brush.pendown()
        self.window.update()

    def clear(self):
        self.brush.clear()
        self.brush.penup()
        self.brush.home()
        self.brush.pendown()
        self.window.update()

    def circle(self):
        self.brush.circle(100)
        self.window.update()

    def square(self):
        for _ in range(4):
            self.brush.fd(50)
            self.brush.rt(90)
        self.window.update()


def main():
    app = Application()
    app.start()


if __name__ == "__main__":
    main()
