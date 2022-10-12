from turtle import Turtle, Screen
import random as rd

screen = Screen()
screen.setup(width=600, height=400)
colors = ["#FF1E1E", "#FF7F3F", "#F7D716", "#36AE7C", "#31C6D4", "#293462", "#C70A80"]

line = Turtle()
line.penup()
line.color("red")
line.goto(x=230, y=-250)
line.pendown()
line.left(90)
line.forward(500)

red = Turtle(shape="turtle")
orange = Turtle(shape="turtle")
yellow = Turtle(shape="turtle")
green = Turtle(shape="turtle")
blue = Turtle(shape="turtle")
navyBlue = Turtle(shape="turtle")
purple = Turtle(shape="turtle")

turtle_list = [red, orange, yellow, green, blue, navyBlue, purple]


def check(tur):
    index = turtle_list.index(tur)
    if index==0:
        return "red"
    elif index==1:
        return "orange"
    elif index==2:
        return "yellow"
    elif index==3:
        return "green"
    elif index==4:
        return "blue"
    elif index==5:
        return "navy blue"
    else:
        return "purple"


count = 0
for tur in turtle_list:
    tur.color(colors[count])
    tur.penup()
    tur.goto(x=-200, y=count*50-150)
    count += 1

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for tur in turtle_list:
        tur.forward(rd.choice(range(1,11)))
        if tur.xcor() > 230:
            winning_color = check(tur)

            if user_bet.lower() == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

            is_race_on = False
            break

screen.exitonclick()

