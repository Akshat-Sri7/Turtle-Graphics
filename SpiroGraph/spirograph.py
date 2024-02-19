import turtle
from turtle import Turtle, Screen
import random

arthur = Turtle()
arthur.speed("fastest")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


def draw(size_of_gap):
    for i in range(361 // size_of_gap):
        arthur.pencolor(random_color())
        arthur.circle(100)
        arthur.left(size_of_gap)


draw(5)

screen = Screen()
screen.exitonclick()
