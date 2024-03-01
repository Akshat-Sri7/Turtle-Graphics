import turtle


def awesome_star_design1():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    arthur = turtle.Turtle()
    arthur.speed(10)
    turtle.bgcolor("black")
    arthur.pensize(2)
    arthur.penup()
    arthur.goto(-100, 0)
    arthur.pendown()

    for i in range(180):
        arthur.color(colors[i % 6])
        arthur.forward(300)
        arthur.right(61)
        arthur.forward(200)
        arthur.right(120)
        arthur.forward(200)
        arthur.right(61)
        arthur.forward(300)
        arthur.right(181)

    arthur.hideturtle()


# Call the function to draw the attractive design with black background
awesome_star_design1()

turtle.done()
