from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

score = ScoreBoard()

screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

game_is_on = True
sleep_t = 0.07
while game_is_on:
    time.sleep(sleep_t)
    screen.update()
    ball.move()

    # Detect ball collision with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.y_bounce()

    # Detect ball collision with paddle
    if r_paddle.distance(ball) < 50 and ball.xcor() > 320 or l_paddle.distance(ball) < 50 and ball.xcor() < -320:
        ball.x_bounce()
        sleep_t -= 0.005

    # Detect R paddle misses:
    if ball.xcor() > 400:
        ball.goal()
        score.l_score_up()
        sleep_t = 0.07

    # Detect L paddle misses:
    if ball.xcor() < -400:
        ball.goal()
        score.r_score_up()
        sleep_t = 0.07

screen.exitonclick()
