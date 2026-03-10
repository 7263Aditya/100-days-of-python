# import turtle
# import random
# tim = turtle.Turtle()

# from turtle import Turtle, Screen   # Always use this method to import specific function or method
# tim = Turtle()
# tom = Turtle()
# terry = Turtle()

# from turtle import *   # Don't use this method
# from random import *

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# import using aliases
# import turtle as t
# tim = t.Turtle()

# for _ in range (100):
#  tim.forward(10)
#  tim.penup()
#  tim.forward(10)
#  tim.pendown()
# colors = ['CornflowerBlue','DarkOrchid','IndianRed','DeepSkyBlue',"LightSeaGreen","Wheat","SlateGray","SeaGreen"]

# def draw_shape(num_sides):
#  for _ in range(num_sides):
#   angle = 360/ num_sides
#   tim.forward(100)
#   tim.left(angle)
#
# for shape_sides in range(3,11):
#   tim.color(random.choice(colors))
#   draw_shape(shape_sides)


# Random walk program

# t.colormode(255)
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r,g,b)
#     return random_color
# directions = [0,90,180,270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#  tim.color(random_color())
#  tim.forward(30)
#  tim.setheading(random.choice(directions))


import turtle as t
import random
tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()