import random
import tkinter as tk
import pandas
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv('data/french_words.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/french_words.csv')
    print(original_data)
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text ="French",fill= "black")
    canvas.itemconfig(card_word,text =current_card["French"],fill = "black")
    canvas.itemconfig(card_background,image =card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text ="English",fill = "white")
    canvas.itemconfig(card_word,text =current_card["English"],fill= "white")
    canvas.itemconfig(card_background,image = card_back_img)
    
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/french_words.csv',index=False)
    next_card()

window = tk.Tk()
window.title("The Flash Card Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = tk.Canvas(width=800, height=526)
card_front_img = tk.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image = card_front_img)
card_back_img = tk.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image = card_front_img)
card_title = canvas.create_text(400, 150, text ="", font=("Arial", 40,"italic"))
card_word = canvas.create_text(400, 263, text ="", font=("Arial", 68,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0, column=0,columnspan=2)

cross_image =tk.PhotoImage(file="images/wrong.png")
unknown_button = tk.Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_image = tk.PhotoImage(file="images/right.png")
known_button = tk.Button(image=check_image,highlightthickness=0,command=next_card)
known_button.grid(row=1,column=1)

next_card()
window.mainloop()