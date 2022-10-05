# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
# my_screen.bgcolor("black")
# timmy.color("#87a2fb")
# timmy.speed(50)
#
# timmy.begin_fill()
# for i in range(0,12):
#     timmy.forward(300)
#     timmy.right(150)
# timmy.end_fill()
#
# jemmy = Turtle()
# jemmy.shapesize(5)
# jemmy.goto(-100,-100)
# jemmy.color("#FFF6BF")
# jemmy.speed(50)
#
# jemmy.begin_fill()
# for i in range(0,9):
#     jemmy.forward(200)
#     jemmy.right(160)
# jemmy.end_fill()
#
# may = Turtle()
# may.goto(-100,200)
# may.color("#FFC4C4")
# may.tiltangle(150)
# may.speed(50)
#
# may.circle(30)
# may._go(-100)
#
# for i in range(0,25):
#     may.forward(100)
#     may.right(165)
#
# may._go(-200)
# may.begin_fill()
# for i in range(0,9):
#     may.forward(100)
#     may.right(160)
# may.end_fill()
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name",["Pikachu","Squirtle","Chanrmender"])
table.add_column("Type",["Electic","Water","Fire"])
table.align = "r"
print(table)
