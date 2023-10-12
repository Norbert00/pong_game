import time
from ball import Ball
from paddle import Paddle
from game_screen import GameScreen

LEFT_PADDLE = (-370, 0)
RIGHT_PADDLE = (370, 0)

right_paddle = Paddle(RIGHT_PADDLE)
left_paddle = Paddle(LEFT_PADDLE)

screen = GameScreen()
screen.move_paddles(right_paddle, "right")
screen.move_paddles(left_paddle, "left")
time.sleep(0.1)

ball = Ball()

game_is_on = True
while game_is_on:
    screen.update_screen()
    ball.move()
    if ball.ycor() > screen.top_wall() or ball.ycor() < screen.bottom_wall():
        ball.bounce_y()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
