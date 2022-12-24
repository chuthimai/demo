from turtle import Turtle

FONT = ("Academy Engraved LET", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("white")
        self.goto(-240, 270)
        self.write(f"Level: {self.level}", align="center", font=FONT)
        self.hideturtle()

    def up_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def final(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
