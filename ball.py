from turtle import Turtle
import time

WIDTH = 1
HEIGHT = 1
SHAPE = "circle"
BALL_COLOR = "white"
DEFAULT_SPEED = 0.02


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.color(BALL_COLOR)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = DEFAULT_SPEED

    def move(self):
        time.sleep(0.1)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.ball_speed *= 0.2

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.2

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = DEFAULT_SPEED
        self.bounce_x()

