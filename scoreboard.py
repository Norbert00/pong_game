from turtle import Turtle

SCORE_POSITION = [(-100, 260), (100, 260)]
TEXT_POSITION = "Center"
FONT_NAME = "Courier"
FONT_SIZE = 24
FONT_TYPE = "bold"
FONT_COLOR = "deep pink"



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(FONT_COLOR)
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(SCORE_POSITION[0])
        self.write(self.l_score, align=TEXT_POSITION, font=(FONT_NAME, FONT_SIZE, FONT_TYPE))
        self.goto(SCORE_POSITION[1])
        self.write(self.r_score, align=TEXT_POSITION, font=(FONT_NAME, FONT_SIZE, FONT_TYPE))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
