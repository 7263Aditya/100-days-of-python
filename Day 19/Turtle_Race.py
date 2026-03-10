from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet.","Which turtle will win the race?Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turt = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turt.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turt:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle wins!")
            else:
                print(f"You lost! The {winning_color} turtle wins!")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()