from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def guess_number():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


class Number:
    def __init__(self):
        self.correct_num = 7
        self.check_low = False
        self.check_high = False
        self.check_correct = False


@app.route('/<int:number>')
def show(function):
    def wrapper(num, number):
        if number == num.correct_num:
            num.check_correct = True
            num.check_low = False
            num.check_high = False

        if number < num.correct_num:
            num.check_correct = False
            num.check_low = True
            num.check_high = False

        if number > num.correct_num:
            num.check_correct = False
            num.check_low = False
            num.check_high = True

        function(num)
        return wrapper


@show
def guess_too_low(num):
    if num.check_low:
        return '<h1>Too low, try again!</h1>' \
               '<img scr="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'


@show
def guess_too_high(num):
    if num.check_high:
        return '<h1>Too high, try again!</h1>' \
               '<img scr="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'


@show
def correct(num):
    if num.check_correct:
        return '<h1>You got it!</h1>' \
               '<img scr="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


app.run(debug=True)

