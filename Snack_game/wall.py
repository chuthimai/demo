from turtle import Turtle


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("#CDFCF6")
        self.goto(-300, -300)
        self.pendown()
        self.pensize(10)
        self.create_wall()

    def create_wall(self):
        for wall in range(4):
            self.forward(600)
            self.left(90)








