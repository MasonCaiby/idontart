import turtle


class Fractiles(object):

    def __init__(self, sides=3, reps=1, side_length=60,
                 w_width=800, w_height=800, w_startx=0, w_starty=None):

        # class args
        self.sides = sides
        self.reps = reps
        self.w_width = w_width
        self.w_height = w_height
        self.w_startx = w_startx
        self.w_starty = w_starty
        self.side_length=side_length

        # things we'll calculate
        self.rotation = None
        self.directions = 'rf'
        self.direction_dict = {}

        # things we need to initialize
        self.atuin = turtle.Turtle()
        self.window = turtle.Screen()

        # function we needs on init
        self.startup()

    def startup(self):
        self.window.setup(height=self.w_height, width=self.w_width, startx=self.w_startx,
                          starty=self.w_starty)
        self.rotation = 360 / self.sides

    def get_one_shape(self):
        return 'fl'*self.sides*2 + 'rrr'

    def get_reps(self):
        for rep in range(self.reps):
            print(rep)
            one_shape = self.get_one_shape()
            self.directions = self.directions.replace('f',one_shape)
            print(self.directions)

    def draw_shape(self):
        for letter in self.directions:
            if letter == 'f':
                self.atuin.forward(self.side_length)
            elif letter == 'l':
                self.atuin.left(self.rotation)
            else:
                self.atuin.right(self.rotation)



if __name__ =="__main__":
    a = Fractiles(sides=3)
    a.get_reps()
    a.draw_shape()
    turtle.done()