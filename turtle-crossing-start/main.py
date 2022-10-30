import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

tim = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(tim.move, "Up")

speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()

    car_manager.create_cars()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(tim) < 20:
            game_is_on = False
            score.final()

    if tim.check_finish_line():
        tim.reset()
        score.up_level()
        speed *= 0.5


screen.exitonclick()
