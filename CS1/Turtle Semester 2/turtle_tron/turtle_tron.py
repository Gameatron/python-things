from turtle import Turtle, Screen
from time import time, sleep
import json
from math import floor
from random import randint, choice

TARGET_FPS = 60
TURTLE_SPEED = 2.5
GAME_ID = int(time()//1)
JSON_LINK = "/home/takoda/python-things/CS1/Turtle Semester 2/turtle_tron/data.json"


class Light_Turtle(Turtle):
    def __init__(self, color, facing, start_point):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.start_point = start_point
        self.goto(start_point[0], start_point[1])
        self.colorv = color
        self.color(color)
        if facing == "up":
            self.facing = 90
        elif facing == "down":
            self.facing = 270
        elif facing == "left":
            self.facing = 180
        elif facing == "right":
            self.facing = 0
        self.seth(self.facing)
        self.wall = [self.position()]
        self.pendown()
        self.alive = True

    def position(self):
        p = super().position()
        return (round(p[0]), round(p[1]))

    def wall_add(self):
        self.wall.append(self.position())


class Application:
    def __init__(self):
        self.screen_size = (600, 600)
        self.some_randomvalue_idk = 0
        self.window = Screen()
        self.window.setup(height=700, width=700)
        self.window.tracer(0, 0)
        self.window.bgcolor("black")
        self.writer = Turtle()
        self.writer.hideturtle()
        self.writer.color("blue")
        self.gui_maker = Turtle()
        self.gui_maker.hideturtle()
        self.make_gui()
        self.player1 = Light_Turtle(color="red",
                                    facing="right",
                                    start_point=(-100, 0))
        self.player1_score = 0
        self.player2 = Light_Turtle(color="blue",
                                    facing="left",
                                    start_point=(100, 0))
        self.player2_score = 0
        self.window.title("Turtle Tron")
        self.colors = ("green", "yellow", "white")
        self.powerup1 = Turtle(shape="circle")
        self.powerup2 = Turtle(shape='circle')
        self.powerup3 = Turtle(shape='circle')
        self.powerup1.turtlesize(.5)
        self.powerup2.turtlesize(.5)
        self.powerup3.turtlesize(.5)
        self.powerup_t = (self.powerup1, self.powerup2, self.powerup3)
        self.powerup_coords = []
        self.powerups = ("speed", "clear", "invis")
        self.window.update()

    def start(self):
        while True:
            try:
                ans = self.window.textinput("Start",
                                            "Press enter when you are ready to begin, type 'q' to quit.").lower()
            except AttributeError:
                break
            if ans == 'q' or ans == 'quit':
                break
            else:
                self.restart()
                self.run()
                self.writer.penup()
                self.writer.goto(0, 100)
                self.writer.pendown()
                self.window.update()
        self.window.clear()
        self.writer.penup()
        self.writer.goto(0, 0)
        self.writer.pendown()
        self.writer.write(f"Player 1: {self.player1_score}\tPlayer 2: {self.player2_score}",
                        font=("Times New Roman", 36, "bold"),
                        align='center')
        if self.player1_score == self.player2_score:
            try:
                name1 = self.window.textinput("Finish!",
                                            "Please enter a name for the leaderboards, Player 1").lower()
                name2 = self.window.textinput("Finish!",
                                            "Please enter a name for the leaderboards, Player 2").lower()
            except AttributeError:
                return
            with open(JSON_LINK, 'r') as f:
                data = json.load(f)
                data[GAME_ID] = {}
                data[GAME_ID]['player1'] = name1
                data[GAME_ID]['p1score'] = self.player1_score
                data[GAME_ID]['player2'] = name2
                data[GAME_ID]['p2score'] = self.player2_score
            with open(JSON_LINK, 'w') as f:
                json.dump(data, f)
        elif self.player1_score > self.player2_score:
            try:
                name1 = self.window.textinput("Finish!",
                                            "Please enter a name for the leaderboards, Player 1").lower()
                name2 = self.window.textinput("Finish!",
                                            "Please enter a name for the leaderboards, Player 2").lower()
            except AttributeError:
                return 
            with open(JSON_LINK, 'r') as f:
                data = json.load(f)
                data[GAME_ID] = {}
                data[GAME_ID]['player1'] = name1
                data[GAME_ID]['p1score'] = self.player1_score
                data[GAME_ID]['player2'] = name2
                data[GAME_ID]['p2score'] = self.player2_score
            with open(JSON_LINK, 'w') as f:
                json.dump(data, f)
        elif self.player2_score > self.player1_score:
            try:
                name1 = self.window.textinput("Finish!",
                                            "Please enter a name for the leaderboards, Player 1").lower()
                name2 = self.window.textinput("Finish!",
                                            "Please enter a name for the leaderboards, Player 2").lower()
            except AttributeError:
                return 
            with open(JSON_LINK, 'r') as f:
                data = json.load(f)
                data[GAME_ID] = {}
                data[GAME_ID]['player1'] = name1
                data[GAME_ID]['p1score'] = self.player1_score
                data[GAME_ID]['player2'] = name2
                data[GAME_ID]['p2score'] = self.player2_score
            with open(JSON_LINK, 'w') as f:
                json.dump(data, f)

    def run(self):
        self.place_powerups()
        self.writer.clear()
        self.window.update()
        self.some_randomvalue_idk += 1
        self.count_down()
        self.window.onkey(lambda: self.player2.left(90), "Left")
        self.window.onkey(lambda: self.player2.right(90), "Right")
        self.window.onkey(lambda: self.player1.left(90), "a")
        self.window.onkey(lambda: self.player1.right(90), "d")
        self.window.listen()
        t1 = time()
        t2 = time()
        while True:
            elapsed = t2 - t1
            if elapsed > 1 / TARGET_FPS:
                t1 = t2
                self.player1.forward(TURTLE_SPEED)
                self.player2.forward(TURTLE_SPEED)
                self.check_walls()
                self.check_light_walls()
                self.player1.wall_add()
                self.player2.wall_add()
                self.window.update()
                if not self.player1.alive or not self.player2.alive:
                    self.display_winner()
                    self.writer.clear()
                    self.window.update()
                    self.writer.penup()
                    self.writer.goto(0, 100)
                    self.window.update()
                    return
            t2 = time()
        self.window.mainloop()

    def restart(self):
        self.writer.clear()
        self.window.update()
        self.player1.alive = True
        self.player2.alive = True
        self.player1.showturtle()
        self.player2.showturtle()
        self.player1.clear()
        self.player2.clear()
        self.player1.penup()
        self.player2.penup()
        self.player1.goto(self.player1.start_point)
        self.player2.goto(self.player2.start_point)
        self.player1.seth(self.player1.facing)
        self.player2.seth(self.player2.facing)
        self.player1.color(self.player1.colorv)
        self.player2.color(self.player2.colorv)
        self.player1.pendown()
        self.player2.pendown()
        self.player1.wall.clear()
        self.player2.wall.clear()
        self.window.update()

    def gui_goto(self, x, y):
        self.gui_maker.penup()
        self.gui_maker.goto(x, y)
        self.gui_maker.pendown()

    def make_gui(self):
        self.gui_maker.color("red")
        self.gui_maker.pensize(15)
        x, y = self.screen_size
        self.gui_goto(x/2, y/2)
        self.gui_maker.seth(270)
        for _ in range(4):
            self.gui_maker.fd(x)
            self.gui_maker.rt(90)
        self.window.update()

    def count_down(self):
        self.writer.penup()
        self.writer.home()
        self.writer.pendown()
        timer = 3
        for _ in range(4):
            self.writer.write(timer,
                              font=("Times New Roman", 24, "bold"),
                              align="center")
            sleep(1)
            timer -= 1
            self.writer.clear()


    def check_walls(self):
        p1x, p1y = self.player1.position()
        p2x, p2y = self.player2.position()
        wallx, wally = self.screen_size
        wallx /= 2
        wally /= 2
        if p1x >= wallx or p1x <= -wallx or p1y <= -wally or p1y >= wally:
            self.player1.alive = False
        if p2x >= wallx or p2x <= -wallx or p2y <= -wally or p2y >= wally:
            self.player2.alive = False

    def check_light_walls(self):
        p1c = self.player1.position()
        p1w = self.player1.wall
        p2c = self.player2.position()
        p2w = self.player2.wall
        if p1c == p2c:
            self.player1.alive = False
            self.player2.alive = False
        if p1c in p1w or p1c in p2w:
            self.player1.alive = False
        if p2c in p1w or p2c in p2w:
            self.player2.alive = False

    def display_winner(self):
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.goto(0, 245)
        self.writer.pendown()
        if self.player2.alive == False and self.player1.alive == False:
            self.writer.write("Tie!",
                              font=("Times New Roman", 36, "bold"),
                              align="center")
            self.writer.penup()
            self.writer.goto(0, 145)
            self.writer.pendown()
            self.writer.write(f"Player 1: {self.player1_score}\tPlayer 2: {self.player2_score}",
                              font=("Times New Roman", 24),
                              align="center")
            self.explode(self.player1, self.player2)
        elif self.player1.alive == False:
            self.writer.write("Player 2 has won!",
                              font=("Times New Roman", 36, "bold"),
                              align="center")
            self.player2_score += 1
            self.writer.penup()
            self.writer.goto(0, 145)
            self.writer.pendown()
            self.writer.write(f"Player 1: {self.player1_score}\tPlayer 2: {self.player2_score}",
                              font=("Times New Roman", 24),
                              align="center")
            self.explode(self.player1)
        elif self.player2.alive == False:
            self.writer.write("Player 1 has won!",
                              font=("Times New Roman", 36, "bold"),
                              align="center")
            self.player1_score += 1
            self.writer.penup()
            self.writer.goto(0, 145)
            self.writer.pendown()
            self.writer.write(f"Player 1: {self.player1_score}\tPlayer 2: {self.player2_score}",
                              font=("Times New Roman", 24),
                              align="center")
            self.explode(self.player2)

    def explode(self, turtle1, turtle2=None):
        i = 1
        if turtle2 == None:
            turtle1.hideturtle()
            for _ in range(39):
                if i % 20 == 0:
                    i = 0
                    turtle1.seth(270)
                    turtle1.bk(20)
                if i % 2 == 0:
                    turtle1.color("yellow")
                else:
                    turtle1.color("orange")
                turtle1.begin_fill()
                turtle1.seth(270)
                turtle1.forward(1)
                turtle1.seth(0)
                turtle1.circle(i*1)
                turtle1.end_fill()
                sleep(.1)
                self.window.update()
                i += 1
        else:
            turtle1.hideturtle()
            turtle2.hideturtle()
            for _ in range(39):
                if i % 20 == 0:
                    i = 0
                    turtle1.seth(270)
                    turtle2.seth(270)
                    turtle1.bk(20)
                    turtle2.bk(20)
                if i % 2 == 0:
                    turtle1.color("orange")
                    turtle2.color("orange")
                else:
                    turtle1.color("yellow")
                    turtle2.color("yellow")
                turtle1.begin_fill()
                turtle2.begin_fill()
                turtle1.seth(270)
                turtle2.seth(270)
                turtle1.fd(1)
                turtle2.fd(1)
                turtle1.seth(0)
                turtle2.seth(0)
                turtle1.circle(i*1)
                turtle2.circle(i*1)
                turtle1.end_fill()
                turtle2.end_fill()
                sleep(.1)
                self.window.update()
                i += 1

    def place_powerups(self):
        for turtle in self.powerup_t:
            ranx = randint(-250, 250)
            rany = randint(-250, 250)
            turtle.penup()
            turtle.goto(ranx, rany)
            turtle.pendown()
            turtle.color(choice(self.colors))
        self.window.update()

def main():
    app = Application()
    app.start()


if __name__ == "__main__":
    main()
