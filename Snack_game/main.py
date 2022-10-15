from turtle import Turtle, Screen
from snack import Snack
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snack Game")
screen.tracer(0)

screen.update()

my_snack = Snack()

screen.listen()
screen.onkey(my_snack.up, "Up")
screen.onkey(my_snack.down, "Down")
screen.onkey(my_snack.right, "Right")
screen.onkey(my_snack.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snack.move()

screen.exitonclick()
