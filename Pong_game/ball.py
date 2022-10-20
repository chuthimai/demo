from turtle import Turtle
import random as rd


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#CFFF8D")
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.1
        self.direction = [0, 30, 45, 60, 120, 135, 150, 180, 210, 225, 240, 300, 215, 330]

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.setheading(rd.choice(self.direction))
        self.x_move *= -1
        self.speed = 0.1











