from tkinter import *
import random
from PIL import ImageTk, Image
import pandas


BACKGROUND_COLOR = "#B1DDC6"
timer = None
current_card = {}

# french_words = pandas.read_csv(r"C:\Users\yusuf\PycharmProjects\FlashCardProgram\french_words\french_words.csv")
#
# df = pd.DataFrame({"French": french_words.French, "English": french_words.English})
# df_in_dict = df.to_dict("records")
try:
    data = pandas.read_csv(r"C:\Users\yusuf\PycharmProjects\FlashCardProgram\french_words\words_to_learn.csv")
    to_learn = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv(r"C:\Users\yusuf\PycharmProjects\FlashCardProgram\french_words\french_words.csv")
    to_learn = data.to_dict(orient="records")


def known_words():
    to_learn.remove(current_card)
    print(len(to_learn))
    try:
        data = pandas.DataFrame(to_learn)
        data.to_csv(r"C:\Users\yusuf\PycharmProjects\FlashCardProgram\french_words/words_to_learn.csv", index=False)
    except FileNotFoundError:
        data = pandas.read_csv(r"C:\Users\yusuf\PycharmProjects\FlashCardProgram\french_words\french_words.csv")
    next_word()


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(words_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_card)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(words_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_card)


window = Tk()
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR, highlightthickness=0)
window.title("FlashCard")
flip_timer = window.after(3000, func=flip_card)


# Canvas #
canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = ImageTk.PhotoImage(Image.open(r"C:\Users\yusuf\PycharmProjects\FlashCardProgram\images\card_front.png"))
back_card = ImageTk.PhotoImage(Image.open(r"C:\Users\yusuf\PycharmProjects\FlashCardProgram\images\card_back.png"))
card_background = canvas.create_image(400, 265, image=front_card)
title_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
words_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=1, columnspan=2)


# Buttons #
tick_image = ImageTk.PhotoImage(Image.open(r"C:\Users\yusuf\PycharmProjects\FlashCardProgram\images\right.png"))
tick_button = Button(image=tick_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=known_words)
tick_button.config(borderwidth=0)
tick_button.grid(column=1, row=2)

cross_image = ImageTk.PhotoImage(Image.open(r"C:\Users\yusuf\PycharmProjects\FlashCardProgram\images\wrong.png"))
cross_button = Button(image=cross_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_word)
cross_button.config(borderwidth=0)
cross_button.grid(column=0, row=2)

next_word()


window.mainloop()
