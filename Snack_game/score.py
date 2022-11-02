from turtle import Turtle

ALIGN = "center"
FONT = ("Times New Roman", 16, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=310)
        self.write_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGN, font=FONT)

    # def reset(self):
    #     if self.score > self.high_score:
    #         self.high_score = self.score
    #     self.score = 0
    #     self.update_score()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)




