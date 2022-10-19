from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle(-380, 0)
right_paddle = Paddle(380, 0)
ball = Ball()
left_score = ScoreBoard((-100, 200))
right_score = ScoreBoard((100, 200))

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.speed)

    # process hit the wall
    if abs(ball.ycor()) >= 280:
        ball.bounce_y()
    # process hit the paddle
    if abs(ball.xcor()) >= 360 and (ball.distance(right_paddle) < 50 or ball.distance(left_paddle) < 50):
        ball.bounce_x()
        if ball.distance(right_paddle) < 50:
            right_score.add_score()
        if ball.distance(left_paddle) < 50:
            left_score.add_score()
    # process if not hit the paddle
    if abs(ball.xcor()) > 360:
        ball.reset()

    if right_score.score == 24 or left_score.score == 24:
        game_is_on = False
        if right_score.score == 24:
            print("Right user win!")
        else:
            print("Left user win!")
        right_score.end()

    ball.move()

screen.exitonclick()
