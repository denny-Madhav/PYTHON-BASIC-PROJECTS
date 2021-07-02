# ---------------------------------- IMPORTS -----------------------------------
from tkinter import *
import pandas
import random
# ---------------------------------- CONSTANTS -----------------------------------
BACKGROUND_COLOR = "#B1DDC6"
word = {}
to_learn = {}

# ---------------------------------- FUNCTIONING -----------------------------------
try:
    data = pandas.read_csv("words_to_Learn.csv.csv")
except FileNotFoundError:
    actual_data = pandas.read_csv("french_words.csv")
    to_learn = actual_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global word, change_timer
    window.after_cancel(change_timer)
    word = random.choice(to_learn)
    french_word = word["French"]
    english_word = word["English"]
    print(french_word, english_word)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    canvas.itemconfig(card_background, image=card_front)
    change_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word["English"],  fill="white")
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    to_learn.remove(word)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("words_to_Learn.csv", index=False)
    next_card()

# ---------------------------------- UI -----------------------------------


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
change_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 255, text="word", font=("Arial", 52, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)


wrong_img = PhotoImage(file="wrong.png")
unknown_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.config(bg=BACKGROUND_COLOR)
unknown_button.grid(row=1, column=0)

right_img = PhotoImage(file="right.png")
known_button = Button(image=right_img, highlightthickness=0, command=is_known)
known_button.config(bg=BACKGROUND_COLOR)
known_button.grid(row=1, column=1)
next_card()
# ------------------------------------- MAIN LOOP --------------------------------------------
canvas.mainloop()
