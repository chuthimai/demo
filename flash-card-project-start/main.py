from tkinter import *
import pandas as pd
import random as rd

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
file = pd.read_csv("data/english-vietnamese.csv")
to_learn = file.to_dict(orient='records')
word = {}
flip_timer = "0"


#-------------------------------------------------------------------------------------


def next_card():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = rd.choice(to_learn)
    flash_card.itemconfig(flash_card_background, image=photo_card_front)
    flash_card.itemconfig(card_title, text="English", fill="black")
    flash_card.itemconfig(card_word, text=word["English"], fill="black")
    flip_timer = window.after(2000, func=flip_card)


def flip_card():
    flash_card.itemconfig(card_title, text="Vietnamese", fill="white")
    flash_card.itemconfig(card_word, text=word["Vietnamese"], fill="white")
    flash_card.itemconfig(flash_card_background, image=photo_card_back)


def is_know():
    to_learn.remove(word)
    next_card()


#-------------------------------------------------------------------------------------


flash_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
photo_card_front = PhotoImage(file="images/card_front_1.gif")
photo_card_back = PhotoImage(file="images/card_back_1.gif")
flash_card_background = flash_card.create_image(400, 263, image=photo_card_front)
flash_card.delete()
card_title = flash_card.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = flash_card.create_text(400, 263, text="Word", font=("Ariel", 50, "bold"))
flash_card.grid(row=0, column=0, columnspan=2)

photo_wrong = PhotoImage(file="images/wrong_1.gif")
wrong = Button(image=photo_wrong, highlightthickness=0, command=next_card)
wrong.grid(row=1, column=0)

photo_right = PhotoImage(file="images/right_1.gif")
right = Button(image=photo_right, highlightthickness=0, command=is_know)
right.grid(row=1, column=1)

next_card()

window.mainloop()

