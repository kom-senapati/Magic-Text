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

def draw_text(text, size):
    text_turtle = turtle.Turtle()
    text_turtle.penup()
    text_turtle.goto(0, 0)
    text_turtle.pendown()
    text_turtle.color("yellow")
    text_turtle.write(text, align="center", font=("Arial", size, "bold"))
    text_turtle.hideturtle()
