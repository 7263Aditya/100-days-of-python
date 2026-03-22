import tkinter as tk

window = tk.Tk()
window.title("My first GUI")
window.minsize(400, 300)
window.config(padx=20, pady=20)

#Label
my_label = tk.Label(text="I am a label",font=("Arial", 25,"italic"))
my_label.pack()

my_label['text'] = "New Text"
my_label.config(text = "New Text")
my_label.grid(column=0,row=0)
my_label.config(padx=50,pady=50)

# Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text = new_text)
    print()
button = tk.Button(text="Click me",command= button_clicked)
button.grid(column=1,row=1)
# button.pack()

# new button
new_button = tk.Button(text="New Button",command=button_clicked)
new_button.grid(column=2,row=0)

# Entry
input = tk.Entry(width=40)
# input.pack()
input.grid(column=3,row=2)
print(input.get())

window.mainloop()