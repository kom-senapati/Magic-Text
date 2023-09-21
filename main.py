import turtle


def draw_box(color):

    border_turtle = turtle.Turtle()
    border_turtle.speed(0)

    border_turtle.pensize(8)

    border_turtle.penup()
    border_turtle.goto(-200, -150)
    border_turtle.pendown()

    border_turtle.color(f"{color}")

    for _ in range(2):
        border_turtle.forward(400)
        border_turtle.left(90)
        border_turtle.forward(300)
        border_turtle.left(90)

    border_turtle.hideturtle()
    turtle.done()
