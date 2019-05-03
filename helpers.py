import turtle

def get_screen_and_turtle(height=600, width=800, startx=0, starty=None):
    window = turtle.Screen()
    window.setup(height=height, width=width, startx=startx, starty=starty)

    atuin = turtle.Turtle()

    return atuin