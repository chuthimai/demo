from Higher_lower_art import *
from Higher_lower_data import data
import random as rd

print(logo)

rd.shuffle(data)
is_game_over = False
user_score = 0

def compare(choose, followerA, followerB):
    global user_score, is_game_over
    if choose == "a" and followerA > followerB:
        data.pop(1)
        user_score += 1
        print(f"You're right. Current score: {user_score}")
    elif choose == "b" and followerA < followerB:
        data.pop(0)
        user_score += 1
        print(f"You're right. Current score: {user_score}")
    else:
        is_game_over = True
        print(f"Sorry, that's wrong. Final score: {user_score}")
    if len(data) == 1:
        is_game_over = True

while not is_game_over:
    A = data[0]
    B = data[1]
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
    choose = input("Who has more followers? Type 'A' or 'B': ").lower()

    compare(choose, A['follower_count'], B['follower_count'])






