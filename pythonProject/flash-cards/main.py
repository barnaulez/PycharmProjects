#----------------Imports-------------------------#
from tkinter import *
import time
import pandas
from random import choice, randint
#----------------Constants-----------------------#
BACKGROUND_COLOR = "#B1DDC6"

try:
    words = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    words = pandas.read_csv("./data/turkish_words.csv")
turkish_words = words.to_dict(orient="records")
word = {}

def delete_word():
    global word
    turkish_words.remove(word)
    df = pandas.DataFrame(turkish_words)
    df.to_csv("data/words_to_learn.csv", index=False)
    get_word()

def get_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = choice(list(turkish_words))
    canvas.itemconfig(canvas_image, image=face_card)
    canvas.itemconfig(card_title, text="Turkish", fill="black")
    canvas.itemconfig(card_word, text=word['turkish'], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global word
    canvas.itemconfig(canvas_image, image=back_card)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word['english'], fill="white")

#----------------UI Setup------------------------------#

window = Tk()
window.title("Language Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
face_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=face_card)
card_title = canvas.create_text(400, 150, text="Türkçe", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)
#---------------Buttons--------------------------------#

no_img = PhotoImage(file="./images/wrong.png")
no_btn = Button(image=no_img, highlightthickness=0, border=0, command=get_word)

yes_img = PhotoImage(file="./images/right.png")
yes_btn = Button(image=yes_img, highlightthickness=0, border=0, command=delete_word)

no_btn.grid(row=1, column=0)
yes_btn.grid(row=1, column=1)


get_word()
window.mainloop()
