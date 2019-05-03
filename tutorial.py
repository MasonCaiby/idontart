"""
This is going to be from a tutorial. https://simpleprogrammer.com/python-generative-art-math/

Maybe I'll make some changes here and there but this will be a starting

I'm kinda just playing around in this file. I would normally have this in a jupy nb, but turtle seems to fail in it.

Instead.... I have like 1000000000 different functions. I'm mainly interested in tracking how the changes I make effect the drawing. Also, in a month when i've forgotten everything I'll be able to sing-along to this file, I guess.
"""

import turtle, time
from helpers import get_screen_and_turtle
import random

def first_turtle():
    """
    Just a little guy that draws an L

    I added the time.sleep because the drawing was generally finished before I could get to the window...
    :return:
    """

    window = turtle.Screen() # initialize a window
    time.sleep(2)
    joe = turtle.Turtle() # init a turtle

    joe.forward(50) # go forward 50... pixels it think?
    joe.left(90) # rotate 90 degrees to the turtles left
    joe.forward(100) # move forward 100 degrees

    turtle.done() # keep window open but don't draw anymore


def recaman1():
    window = turtle.Screen() # init window
    euler = turtle.Turtle() # init turtle

    current = 0 # I'm not really sure what this does I guess, it's part og the recaman algo I guess
    seen = set()

    for step_size in range(1,100):
        backwards = current - step_size

        if backwards > 0 and backwards not in seen:
            euler.backward(step_size) # move the turtle
            current = backwards # reset current
            seen.add(current) # add current to set

        else:
            euler.forward(step_size) # move turtle
            current += step_size # reset current
            seen.add(current) # add current

    turtle.done()


def recaman2():
    window = turtle.Screen() # inti window
    euler = turtle.Turtle() #init turtle

    current = 0
    seen = set()

    for step_size in range(1, 100):
        backwards = current - step_size

        if backwards > 0 and backwards not in seen:
            euler.setheading(90) # orient turtle because circles are drawn from the left
            euler.circle(step_size/2, 180) # now we're doing it with a circle

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
            print('pre_set', atuin.heading())
            atuin.setheading(90)
            print('post_set', atuin.heading())
            atuin.circle(scale*step_size, 180)
            current = backwards

        else:
            print('pre_set', atuin.heading())
            atuin.setheading(270)
            print('post_set', atuin.heading())
            atuin.circle(scale*step_size, 180)
            current += step_size

        print(atuin.pos())

    turtle.done()

"""
hm that was really easy. let's try to make the top half one color and the bottom half a 
different color. gonna go for top blue bottom red"""

def spiral_color():
    atuin = get_screen_and_turtle()

    scale = 2.5

    for step_size in range(1,100):

        if step_size % 2:
            atuin.setheading(90)
            atuin.pen({'pencolor':'blue'})
            atuin.circle(scale*step_size/2, 180)

        else:
            atuin.setheading(270)
            atuin.pen({'pencolor':'red'})
            atuin.circle(scale*step_size/2, 180)


def detail_spiral(atuin=None, size=30):
    if atuin is None:
        atuin = get_screen_and_turtle()

    current = 0
    scale = 2.5
    colors = {0: 'blue',
              1: 'red',
              2: 'green',
              3: 'black'}

    orientations = {0: 90,
                    1: 180,
                    2: 270,
                    3: 0}

    for step_size in range(1,size):
        location = step_size % 4
        color = colors[location]
        orientation = orientations[location]

        atuin.setheading(orientation)
        atuin.pen({'pencolor': color})
        atuin.circle(scale*step_size/2, 90)

    "wowee first try look at me mom! art! or something that loosely resemembles art"


def spiral_recursion():
    atuin = get_screen_and_turtle()

    scale = 5
    colors = {0: 'blue',
              1: 'red',
              2: 'green',
              3: 'black'}

    orientations = {0: 90,
                    1: 180,
                    2: 270,
                    3: 0}

    for step_size in range(10,300):
        location = step_size % 4
        color = colors[location]
        orientation = orientations[location]

        atuin.setheading(orientation)
        atuin.pen({'pencolor': color})
        atuin.circle(scale*step_size, 90)
        position = atuin.pos()
        detail_spiral(atuin)
        atuin.penup()
        atuin.setposition(position)
        atuin.pendown()

def random_spiral():
    atuin = get_screen_and_turtle()

    scale = 5
    colors = {0: 'blue',
              1: 'red',
              2: 'green',
              3: 'black'}

    for step_size in range(5,100):
        location = step_size % 4
        color = colors[location]

        atuin.pen({'pencolor': color})
        travel = random.randint(0,361)
        atuin.circle(scale*step_size, travel)
        position = atuin.pos()
        detail_spiral(atuin, size=random.randint(5,25))
        atuin.penup()
        atuin.setposition(position)
        atuin.pendown()

if __name__ == "__main__":
    random_spiral()
    turtle.done()