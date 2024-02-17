import turtle

arthur = turtle.Turtle()


def move_fwd():
    arthur.forward(10)


def move_bwd():
    arthur.backward(10)


def counter_clock():
    arthur.left(10)


def clockwise():
    arthur.right(10)


def clear_screen():
    arthur.reset()


screen = turtle.Screen()
screen.listen()

screen.onkey(key="w", fun=move_fwd)
screen.onkey(key="s", fun=move_bwd)
screen.onkey(key="a", fun=counter_clock)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
