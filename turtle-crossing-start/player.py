from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("#F8FFDB")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)

    def check_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False








