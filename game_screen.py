import time
from turtle import Screen


HEIGHT = 600
WIDTH = 800
BACKGROUND_COLOR = 'black'
TITLE = "Pong Game"


def setup_screen():
    screen = Screen()
    screen = Screen()
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title(TITLE)
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.tracer(0)
    screen.listen()
    return screen


class GameScreen():
    def __init__(self):
        self.screen = setup_screen()

    def update_screen(self):
        self.screen.update()

    def move_paddles(self, paddle, which_paddle):
        if which_paddle.lower() == "right":
            self.screen.onkey(paddle.go_up, "Up")
            self.screen.onkey(paddle.go_down, "Down")
        else:
            self.screen.onkey(paddle.go_up, "w")
            self.screen.onkey(paddle.go_down, "s")

