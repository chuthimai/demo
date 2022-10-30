from turtle import Turtle
import random as rd

COLORS = ["#FFABE1", "#ADDDD0", "#FAF4B7", "#319DA0", "#7DE5ED", "#5F9DF7", "#B1B2FF"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = rd.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(rd.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.shape("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.goto((300, rd.randint(-250, 250)))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
            if car.xcor() < -320:
                self.all_cars.pop(self.all_cars.index(car))



