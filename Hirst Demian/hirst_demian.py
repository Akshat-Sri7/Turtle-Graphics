import turtle
from turtle import Turtle, Screen
from ColorGram import colors_list
import random

arthur = Turtle()
turtle.colormode(255)

x = -250
y = -250
arthur.penup()

for _ in range(10):
    x = -250
    arthur.setpos(x, y)
    for _ in range(10):
        arthur.pendown()
        arthur.dot(20, random.choice(colors_list))
        arthur.setpos(x, y)
        arthur.penup()
        arthur.forward(50)
        x += 50
    y += 50


screen = Screen()
screen.exitonclick()