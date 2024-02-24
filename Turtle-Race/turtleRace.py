import turtle
from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(height=320, width=900)
user_bet = screen.textinput(title="Make your Bet!", prompt="Who will win the race? Enter a color:")
colors = ['blue', 'red', 'yellow', 'green', 'orange', 'purple']

j = -120
all_turtles = []
for i in range(6):
    arthur = Turtle(shape='turtle')
    arthur.color(colors[i])
    arthur.penup()
    arthur.goto(x=-430, y=j)
    j += 30
    all_turtles.append(arthur)

if user_bet in colors:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() > 430:
            is_race_on = False
            winning_color = turtles.pencolor()
            if user_bet == winning_color:
                print("You win ")
            else:
                print("You lose ")
        steps = random.randint(1, 10)
        turtles.forward(steps)


screen.exitonclick()
