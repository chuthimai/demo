import turtle
import colorgram as cg
from turtle import Turtle, Screen
import random as rd

tim = Turtle()
screen = Screen()
turtle.colormode(255)

tim.penup()
tim.goto(-100, -100)
tim.speed("fast")

colors = cg.extract("2.png", 3)
rgb_color = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)

n = 100


def dot():
    global rgb_color
    tim.pendown()
    tim.dot(5, rd.choice(rgb_color))
    tim.penup()
    tim.forward(5)


def row():
    for j in range(n):
        dot()


for i in range(n):
    row()
    if i % 2 == 0:
        tim.left(90)
        tim.forward(5)
        tim.left(90)
        tim.forward(5)
    else:
        tim.right(90)
        tim.forward(5)
        tim.right(90)
        tim.forward(5)

screen.exitonclick()
