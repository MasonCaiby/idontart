from PIL import Image, ImageDraw, ImageChops
import numpy as np
import random

def load_image(path_to_image):
    true_image = Image.open(path_to_image)
    data = true_image.getdata()
    width, height = true_image.size
    return true_image, data, width, height


def show_two_pics(pic1, pic2):
    Image.fromarray(np.hstack((np.array(pic1),np.array(pic2)))).show()


class NewImage():
    def __init__(self, width, height, max_variance=0.1, num_children=5):
        self.image = None
        self.width = width
        self.height = height
        self.max_variance = max_variance
        self.rand_var = lambda : random.uniform(-max_variance, max_variance)
        self.num_children = num_children
        self.shapes = []
        self.difference = float('INF')

    def make_new_image(self, color=0):
        self.image = Image.new('RGB', (self.width, self.height), color=color)

    def init_shapes(self, num_shapes, sides):
        for _ in range(num_shapes):
            shape = [(random.randint(0,self.width), random.randint(0,self.height)) for i in range(sides)]
            color = tuple(random.randint(0,255) for i in range(3)) + (125,)
            polygon = (shape, color)
            self.shapes.append(polygon)

    def draw_shapes(self):
        draw = ImageDraw.Draw(self.image, 'RGBA')
        for shape in self.shapes:
            draw.polygon(shape[0], shape[1])
        self.image.show()

    def mutate_shape(self, shape):
        new_shapes = []
        for _ in range(self.num_children):
            new_shape = [(point[0] + point[0]*self.rand_var(),
                          point[1] + point[1]*self.rand_var())
                         for point in shape[0]]
            new_color = tuple(color*self.rand_var() for color in shape[1][:3])+(125,)
            new_shapes.append((new_shape, new_color))



if __name__ == "__main__":
    true_image, data, width, height = load_image("source_images/mona_lisa.jpg")
    new_image = NewImage(width, height)
    new_image.make_new_image()
    new_image.init_shapes(4,3)
    new_image.draw_shapes()
    for _ in range(1000):
        new_image.mutate_shape(new_image.shapes[0])
    new_image.draw_shapes()


