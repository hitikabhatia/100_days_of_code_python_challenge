#-----------------------------------------Imports -----------------------------------------------------------------#
from tkinter import *
import pandas as pd
import random
#-------------------------------------------------Globals and Constants------------------------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
wait_time = None
current_card = {}
#--------------------------------------------------Loading data from a csv file-----------------------------------------------------#
try:
    words_to_learn = pd.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    words_to_learn = pd.read_csv("data/french_words.csv").to_dict(orient="records")
# --------------------------------------------------Pick a new word-----------------------------------------------------#
def next_card():
    global wait_time, current_card
    flashgame_window.after_cancel(wait_time)
    current_card = random.choice(words_to_learn)
    word_in_french = current_card.get("French")
    flash_card_canvas.itemconfig(flash_card_image, image=card_front_image)
    flash_card_canvas.itemconfig(card_title, text="French", fill="black")
    flash_card_canvas.itemconfig(card_word_text, text=word_in_french, fill="black")
    wait_time = flashgame_window.after(3000, flip_the_card)

#----------------------------------------------------Flip the card-----------------------------------------------------#
def flip_the_card():
    english_translation = current_card.get("English")
    flash_card_canvas.itemconfig(flash_card_image, image= card_back_image)
    flash_card_canvas.itemconfig(card_title, text="English", fill="white")
    flash_card_canvas.itemconfig(card_word_text, text=english_translation, fill="white")

#---------------------------------------------------Saving the data to the new file------------------------------------#
#saving unknown words to another file for next run
def save_unknown_words():
    unknown_words_df = pd.DataFrame(words_to_learn)
    unknown_words_df.to_csv("data/words_to_learn.csv", index=False)
#----------------------------------------------------Word is known-----------------------------------------------------#
def is_word_known():
    words_to_learn.remove(current_card)
    save_unknown_words()
    next_card()

#--------------------------------------------------------UI SETUP------------------------------------------------------#
flashgame_window = Tk()
flashgame_window.title("Flashy")
flashgame_window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

wait_time = flashgame_window.after(3000, flip_the_card, )


card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

flash_card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_image = flash_card_canvas.create_image(400,263, image=card_front_image)

card_title = flash_card_canvas.create_text(400, 150, font=("Arial", 40, "italic"))
card_word_text = flash_card_canvas.create_text(400, 263, font=("Arial", 60, "bold"))
flash_card_canvas.grid(column=0, row=0, columnspan=2)

#Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=is_word_known)
right_button.grid(column=1, row=1)

next_card()

flashgame_window.mainloop()