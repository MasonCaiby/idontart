""" DOCSTRING
In this file I'll try to change each of 50 shapes to see if I can improve make a picture fit the original.

https://rogerjohansson.blog/2008/12/07/genetic-programming-evolution-of-mona-lisa/

I guess the idea is to pop a shape off the list of shapes, alter it a handful of times, and keep the shape that has the
best information gain.
"""

from PIL import Image, ImageDraw
import numpy as np
import random
import time


def load_image(path_to_image):
    true_image = Image.open(path_to_image)
    data = true_image.getdata()
    width, height = true_image.size
    return true_image, data, width, height


def show_two_pics(pic1, pic2):
    Image.fromarray(np.hstack((np.array(pic1), np.array(pic2)))).show()

class NewImage:
    def __init__(self, true_image, width, height, num_sides=3, num_shapes=50, max_variance=0.1, num_children=5):
        self.true_image = true_image
        self.width = width
        self.height = height
        self.num_sides = num_sides
        self.num_shapes = num_shapes
        self.max_variance = max_variance
        self.num_children = num_children

        self.background = Image.new('RGB', (self.width, self.height), color=0)
        self.shapes = []

    def init_shapes(self):
        for _ in range(self.num_shapes):
            self.shapes.append(Shape(self.num_sides, self.height, self.width, self.num_children, self.max_variance))

    def display_image(self):
        image = self.draw_shapes()
        image.show()

    def draw_shapes(self):
        image = self.background.copy()
        draw = ImageDraw.Draw(image, 'RGBA')
        for shape in self.shapes:
            draw.polygon(shape.vertices, shape.color)
        return image

    def one_generation(self):
        start = time.time()
        for i in range(len(self.shapes)):
            shape = self.shapes.pop(i)
            image = self.draw_shapes()
            shape = self.check_mutants(shape, image)
            self.shapes.insert(i, shape)
        print("Time for one generation: {} | Current Error: {}".format(
            (time.time()-start), self.compare_to_true(self.draw_shapes())
        ))

    def check_mutants(self, shape, image):
        mutants = shape.mutate_shape()
        best_diff = float('INF')

        for mutant in mutants:
            check_image = image.copy()
            draw = ImageDraw.Draw(check_image, 'RGBA')
            draw.polygon(mutant[0], mutant[1])
            new_diff = self.compare_to_true(check_image)
            if new_diff < best_diff:
                best_diff = new_diff
                best_mutant = mutant

        shape.vertices = best_mutant[0]
        shape.color = best_mutant[1]

        return shape

    def compare_to_true(self, image):
        return sum(np.fabs(np.subtract(self.true_image.getdata(), image.getdata())).flatten())




class Shape:
    def __init__(self, num_sides, height, width, num_children, max_variance):
        self.num_sides = num_sides
        self.height = height
        self.width = width
        self.num_children = num_children
        self.max_variance = max_variance

        self.vertices = None
        self.color = None

        self.rand_var = lambda: random.uniform(-max_variance, max_variance)
        self.rand_height = lambda: self.rand_var() * height
        self.rand_width = lambda: self.rand_var() * width

        self.init_shape()

    def init_shape(self):
        self.vertices = [(random.randint(0, self.width),
                  random.randint(0, self.height)) for _ in range(self.num_sides)]

        self.color = tuple(random.randint(0, 255) for _ in range(3)) + (125,)

    def mutate_shape(self):
        children = [(self.vertices, self.color)]
        for _ in range(self.num_children):

            vertices = [(int(point[0] + self.rand_width()),
                         int(point[1] + self.rand_height()))
                        for point in self.vertices]
            color = tuple(int(color + color * self.rand_var()) for color in self.color[:3])
            color += (125,)

            children.append((vertices, color))
        return children

if __name__ == "__main__":
    true_image, data, width, height = load_image("source_images/mona_lisa.jpg")
    new_image = NewImage(true_image, width, height)
    new_image.init_shapes()
    new_image.display_image()
    for i in range(1000):
        new_image.one_generation()
        if not i%50:
            new_image.display_image()


