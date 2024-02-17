from turtle import Turtle, Screen

arthur = Turtle()

arthur.shape('turtle')
arthur.color('DarkTurquoise')

for i in range(100):
    for j in ('red', 'blue', 'green'):
        arthur.color(j)
        arthur.forward(i)
        arthur.right(30)


screen = Screen()
screen.exitonclick()