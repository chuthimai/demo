import random as rd
from guess_the_number_art import *

print(logo)
print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100.")

num=rd.randint(1,101)
life=0
is_game_over=False

def check(user_guess):
    global num, life
    global is_game_over
    if user_guess==num:
        print(win_symbol)
        is_game_over=True
    elif user_guess>num:
        print("Too high.")
        life-=1
    else:
        print("Too low.")
        life-=1
    return

difficul=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficul=="easy":
    life=10
else:
    life=5

while is_game_over==False:
    print(f"You have {life} attempts remaining to guess the number.")
    num_guess=int(input("Make a guess: "))
    check(num_guess)
    if life==0:
        is_game_over=True
        print(f"{lose_symbol}\n\n{good_luck}")
        print(f"The correct number is {num}")



