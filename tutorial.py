"""
This is going to be from a tutorial. https://simpleprogrammer.com/python-generative-art-math/

Maybe I'll make some changes here and there but this will be a starting

I'm kinda just playing around in this file. I would normally have this in a jupy nb,
but turtle seems to fail in it.

Instead.... I have like 1000000000 different functions. I'm mainly interested in tracking how
the changes I make effect the drawing. Also, in a month when i've forgotten everything
I'll be able to sing-along to this file, I guess.
"""

import turtle, time
from helpers import get_screen_and_turtle

def first_turtle():
    """
    Just a little guy that draws an L
    :return:
    """

    window = turtle.Screen()
    time.sleep(2)
    joe = turtle.Turtle()

    joe.forward(50)
    joe.left(90)
    joe.forward(100)

    turtle.done()


def recaman1():
    window = turtle.Screen()
    euler = turtle.Turtle()

    current = 0
    seen = set()

    for step_size in range(1,100):
        backwards = current - step_size

        if backwards > 0 and backwards not in seen:
            euler.backward(step_size)
            current = backwards
            seen.add(current)

        else:
            euler.forward(step_size)
            current += step_size
            seen.add(current)

    turtle.done()


def recaman2():
    window = turtle.Screen()
    euler = turtle.Turtle()

    current = 0
    seen = set()

    for step_size in range(1, 100):
        backwards = current - step_size

        if backwards > 0 and backwards not in seen:
            euler.setheading(90)
            euler.circle(step_size/2, 180)

            current = backwards
            seen.add(current)

        else:
            euler.setheading(270)
            euler.circle(step_size/2, 180)
            current += step_size
            seen.add(current)

    turtle.done()


def recaman3():
    window = turtle.Screen()
    window.setup(width=800, height=600, startx=10, starty=0.5)

    euler = turtle.Turtle()

    scale = 5

    euler.penup()
    euler.setpos(-390, 0)
    euler.pendown()

    current = 0
    seen = set()

    for step_size in range(1,100):
        backwards = current - step_size

        if backwards > 0 and backwards not in seen:
            euler.setheading(90)
            euler.circle(scale*step_size/2, 180)
            current = backwards
            seen.add(current)

        else:
            euler.setheading(270)
            euler.circle(scale*step_size/2, 180)
            current += step_size
            seen.add(current)

    turtle.done()

"""
Ok cool. That's not super complex... Gonna play around with it now...
I think the obvious thing to do is figure out how to draw a spiral.

And right some helper functions so I don't have to initialize everything every time"""

def spiral():
    atuin = get_screen_and_turtle()

    current = 0
    scale = 2.5

    for step_size in range(1, 100):
        backwards = current - step_size

        if step_size % 2:
            atuin.setheading(90)
            atuin.circle(scale*step_size, 180)
            current = backwards

        else:
            atuin.setheading(270)
            atuin.circle(scale*step_size, 180)
            current += step_size

        print(atuin.pos())

    turtle.done()

"""
hm that was really easy. let's try to make the top half one color and the bottom half a 
different color. gonna go for top blue bottom red"""

def spiral_color():
    atuin = get_screen_and_turtle()

    current = 0
    scale = 2.5

    for step_size in range(1,100):
        backwards = current - step_size

        if step_size % 2:
            atuin.setheading(90)
            atuin.pen({'pencolor':'blue'})
            atuin.circle(scale*step_size, 180)
            current = backwards

        else:
            atuin.setheading(270)
            atuin.pen({'pencolor':'red'})
            atuin.circle(scale*step_size, 180)
            current = backwards

    turtle.done()


if __name__ == "__main__":
    spiral_color()