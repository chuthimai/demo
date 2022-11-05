import turtle
import pandas as pd

FONT = ("Courier", 8, "bold")

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
data_state = data["state"].tolist()
data_x = data["x"].tolist()
data_y = data["y"].tolist()


def delete(charecter):
    index = data_state.index(charecter)
    data_state.pop(index)
    data_x.pop(index)
    data_y.pop(index)


game_is_on = True
count = 0
while game_is_on:
    answer = screen.textinput(title=f"{count}/50 Guess the State", prompt="What's another state's name? ").title()
    if answer in data_state:
        x = data_x[data_state.index(answer)]
        y = data_y[data_state.index(answer)]
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.goto(x, y)
        text.write(f"{answer}", font=FONT, align="center")
        count += 1
        delete(answer)

    if count == 50 or answer == "Exit":
        game_is_on = False

new_data = {"State": data_state, "x": data_x, "y": data_y}
export = pd.DataFrame(new_data)
export.to_csv("State can't guess.csv")
screen.exitonclick()
