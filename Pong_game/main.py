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
sub_paddle = Paddle(0, -300)
subl_paddle = Paddle(-200, -200)
subr_paddle = Paddle(200, 200)
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

    # process if hit sub paddle
    if abs(ball.xcor()) == 0 and ball.distance(sub_paddle) < 54.5:
        ball.bounce_x()
    # process sub paddle
    if sub_paddle.ycor() > 300:
        sub_paddle.y_move *= -1
    elif sub_paddle.ycor() < -300:
        sub_paddle.y_move *= -1
    sub_paddle.go()

    # process if hit subl paddle
    if (ball.xcor() == -200) and ball.distance(subl_paddle) < 54.5:
        ball.bounce_x()
    # process subl paddle
    if subl_paddle.ycor() > 300:
        subl_paddle.y_move *= -1
    elif subl_paddle.ycor() < -300:
        subl_paddle.y_move *= -1
    subl_paddle.go()

    # process if hit subr paddle
    if (ball.xcor() == 200) and ball.distance(subr_paddle) < 54.5:
        ball.bounce_x()
    # process subr paddle
    if subr_paddle.ycor() > 300:
        subr_paddle.y_move *= -1
    elif subr_paddle.ycor() < -300:
        subr_paddle.y_move *= -1
    subr_paddle.go()

    # process if hit the paddle
    if abs(ball.xcor()) >= 360 and (ball.distance(right_paddle) < 54.5 or ball.distance(left_paddle) < 54.5):
        ball.bounce_x()
        if ball.distance(right_paddle) < 54.5:
            right_score.add_score()
        if ball.distance(left_paddle) < 54.5:
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
