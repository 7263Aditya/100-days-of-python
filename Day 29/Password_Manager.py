import os
import tkinter as tk
from tkinter import messagebox , PhotoImage
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters)for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols)for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers)for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror("Error","Please enter all fields")
    else:
        is_okay = messagebox.askokcancel(title=website,message=f"These are the details:\nEmail: {email}"
                                                               f"\nPassword: {password}\nIs this correct?")
        if is_okay:
            with open("data.txt","a") as password_file:
                password_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,'end')
                password_entry.delete(0,'end')

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "logo.png")
logo_img = tk.PhotoImage(file=image_path)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = tk.Label(text= "Website:")
website_label.grid(row=1, column=0)
email_label = tk.Label(text= "Email/Username:")
email_label.grid(row=2, column=0)
password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = tk.Entry(width=40)
website_entry.grid(row=1, column=1,columnspan=2)
website_entry.focus()
email_entry = tk.Entry(width=40)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0,"gghabade@gmail.com")
password_entry = tk.Entry(width=20)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = tk.Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = tk.Button(text="Add",width=36,command=save_password)
add_button.grid(row=4, column=1,columnspan=2)

window.mainloop()