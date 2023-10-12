from turtle import Turtle
import time

WIDTH = 1
HEIGHT = 1
SHAPE = "circle"
BALL_COLOR = "white"


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.color(BALL_COLOR)
        self.penup()



    def move(self):
        time.sleep(0.1)
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
        if self.ycor() == 280:
            print("hit the wall")
            new_y -= 30
            self.goto(new_x, new_y)

