from turtle import Turtle
import random as rd


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_food()

    def create_food(self):
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.goto(rd.randint(-280, 280), rd.randint(-280, 280))
        self.color("#FFECEF")

    def new_food(self):
        self.clear()
        self.create_food()






