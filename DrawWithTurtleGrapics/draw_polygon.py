from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape('turtle')
tim.penup()
tim.goto(-50, 200)
tim.pendown()

def polygon (side):
    for j in range(side):
        tim.forward(100)
        tim.right(360/side)

colors = ["#A10035", "#3FA796", "#FEC260", "#2A0944", "#781C68", "#A6D1E6", "#AF7AB3"]
index_color = 0

for i in range(3, 9):
    tim.color(colors[index_color])
    polygon(i)
    index_color += 1

screen.exitonclick()