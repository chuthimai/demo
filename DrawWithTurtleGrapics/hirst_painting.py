import turtle
import colorgram as cg
from turtle import Turtle, Screen
import random as rd

tim = Turtle()
screen = Screen()
turtle.colormode(255)

tim.penup()
tim.goto(-100,-100)
tim.speed("fastest")

colors = cg.extract("2.png", 30)
rbg_color = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rbg_color.append(new_color)

n = 15

def dot():
    tim.pendown()
    tim.dot(10, rd.choice(rbg_color))
    tim.penup()
    tim.forward(30)


def row():
    for i in range(n):
        dot()

for i in range(n):
    row()
    if i%2 == 0:
        tim.left(90)
        tim.forward(30)
        tim.left(90)
        tim.forward(30)
    else:
        tim.right(90)
        tim.forward(30)
        tim.right(90)
        tim.forward(30)

screen.exitonclick()