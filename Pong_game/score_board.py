from turtle import Turtle

FONT = ("Times New Roman", 80, "bold")


class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(position)
        self.color("#00ABB3")
        self.hideturtle()
        self.write(self.score, align="center", font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, align="center", font=FONT)

    def end(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Times New Roman", 16, "bold"))






