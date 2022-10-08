from turtle import Turtle, Screen
import random as rd

tim = Turtle()
screen = Screen()

tim.pensize(2)
tim.speed("fastest")
color = ["#533E85", "#488FB1", "#4FD3C4", "#B958A5"]
size = range(50, 100, 2)
n = 60

for i in range(0, 360, int(360/n)):
    tim.color(rd.choice(color))
    tim.circle(rd.choice(size))
    tim.right(360/n)

screen.exitonclick()