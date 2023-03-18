from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("words to learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, fill="black", text="French")
    canvas.itemconfig(word_text, fill="black", text=current_card["French"])
    canvas.itemconfig(card_background, image=front_card)
    timer = window.after(4000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=current_card["English"])
    canvas.itemconfig(card_background, image=back_card)


def is_known():
    to_learn.remove(current_card)
    next_card()
    words_data = pandas.DataFrame(to_learn)
    words_data.to_csv("words to learn.cv", index=False)


window = Tk()
window.title("flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip_card)
# canvas

canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file="card_front.png")
back_card = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=front_card)
title_text = canvas.create_text(400, 150, text="", fill="black", font=("times new roman", 40, "normal"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("times new roman", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=1, row=1, columnspan=2)

# buttons
right_image = PhotoImage(file="right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=2)

wrong_symbol = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_symbol, highlightthickness=0, command=is_known)
wrong_button.grid(column=2, row=2)

next_card()

window.mainloop()

