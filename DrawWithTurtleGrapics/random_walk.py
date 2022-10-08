import turtle
from turtle import Turtle, Screen
import random as rd

tim = Turtle()
screen = Screen()

tim.pensize(5)
tim.speed("fast")

turtle.colormode(255)

def colors():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    color = (r, g, b)
    return color

turn = [0, 90, 180, 270]
color = [ "#533E85", "#488FB1", "#4FD3C4", "#B958A5"]

for i in range(200):
    tim.color(rd.choice(color))
    tim.forward(10)
    tim.right(rd.choice(turn))

screen.exitonclick()