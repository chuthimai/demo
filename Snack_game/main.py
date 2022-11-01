from turtle import Screen
from snack import Snack
from food import Food
from score import Score
from wall import Wall
import time


screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("#06283D")
screen.title("Snack Game")
screen.tracer(0)

screen.update()

my_snack = Snack()
my_food = Food()
my_score = Score()
wall = Wall()

screen.listen()
screen.onkey(my_snack.up, "Up")
screen.onkey(my_snack.down, "Down")
screen.onkey(my_snack.right, "Right")
screen.onkey(my_snack.left, "Left")

user_level = screen.textinput("Level", "What level do you want play? easy, medium or hard?").lower()

t = 0
if user_level == "easy":
    t = 0.1
elif user_level == "medium":
    t = 0.05
elif user_level == "hard":
    t = 0.01

my_snack.speed = t

game_is_on = True
while game_is_on:
    screen.update()
    t = my_snack.speed
    time.sleep(t)
    my_snack.move()

    # process food
    if my_snack.head.distance(my_food) < 10:
        my_food.new_food()
        my_score.update_score()
        my_snack.extend()
        my_snack.speed *= 0.9

    # process hit the wall
    if abs(my_snack.head.xcor()) > 295 or abs(my_snack.head.ycor()) > 295:
        game_is_on = False
        my_score.game_over()

    # process hit the part of snack
    for segment in my_snack.segments[1:]:
        if segment.distance(my_snack.head) < 5:
            game_is_on = False
            my_score.game_over()

screen.exitonclick()
