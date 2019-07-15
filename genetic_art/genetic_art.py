from PIL import Image, ImageDraw, ImageChops
import numpy as np
import random
import time

def load_image(path_to_image):
    true_image = Image.open(path_to_image)
    data = true_image.getdata()
    width, height = true_image.size
    return true_image, data, width, height


def show_two_pics(pic1, pic2):
    Image.fromarray(np.hstack((np.array(pic1),np.array(pic2)))).show()


class NewImage():
    def __init__(self, true_image, width, height, max_variance=0.1, num_children=5):
        self.true_image = true_image
        self.width = width
        self.height = height
        self.max_variance = max_variance
        self.num_children = num_children

        self.image = None

        self.rand_var = lambda: random.uniform(-max_variance, max_variance)
        self.rand_height = lambda: self.rand_var()*height
        self.rand_width = lambda : self.rand_var()*width

        self.shapes = []
        self.latest_gen = []
        self.difference = float('INF')

    def make_new_image(self, color=0):
        self.image = Image.new('RGB', (self.width, self.height), color=color)

    def init_shapes(self, num_shapes, sides):
        for _ in range(num_shapes):
            shape = [(random.randint(0, self.width),
                      random.randint(0, self.height)) for _ in range(sides)]

            color = tuple(random.randint(0, 255) for _ in range(3)) + (125,)
            polygon = (shape, color)
            self.shapes.append(polygon)
        self.latest_gen = self.shapes
        self.add_shapes()

    def add_shapes(self):
        draw = ImageDraw.Draw(self.image, 'RGBA')
        for shape in self.shapes:
            draw.polygon(shape[0], shape[1])

    def mutate_shape(self, shape):
        new_shapes = []
        for _ in range(self.num_children):
            new_shape = [(int(point[0] + self.rand_width()),
                          int(point[1] + self.rand_height()))
                         for point in shape[0]]

            new_color = tuple(int(color+color*self.rand_var())
                              for color in shape[1][:3])\
                        +(125,)

            new_shapes.append((new_shape, new_color))
        return new_shapes

    def make_new_shapes(self):
        made_shapes = []
        shapes_to_mutate = self.latest_gen + \
                           random.choices(self.shapes,
                                          k=min(100, int(0.3*len(self.shapes))))
        start = time.time()
        for i, shape in enumerate(shapes_to_mutate):
            new_shapes = self.mutate_shape(shape)
            for new_shape in new_shapes:
                new_image = self.image.copy()
                draw = ImageDraw.Draw(new_image, 'RGBA')
                draw.polygon(new_shape[0], new_shape[1])
                if self.compare_new_images(new_image):
                    print("{:.2f}% done".format(100*i/len(shapes_to_mutate)))
                    made_shapes.append(new_shape)

        print("\n"*2,
              "time per image:", (time.time()-start)/(5*len(shapes_to_mutate)),
              "number of shapes:", len(self.shapes),
              "\n"*2)
        self.shapes += self.latest_gen
        self.latest_gen = made_shapes

    def compare_new_images(self, new_image):
        new_diff = sum(np.fabs(np.subtract(
                                       self.true_image.getdata(),
                                       new_image.getdata())).flatten())

        if new_diff < self.difference:
            self.image = new_image
            self.difference = new_diff
            print(new_diff)
            return True
        return False

if __name__ == "__main__":
    true_image, data, width, height = load_image("source_images/mona_lisa.jpg")
    new_image = NewImage(true_image, width, height)
    new_image.make_new_image()
    new_image.init_shapes(num_shapes=1000, sides=3)
    new_image.image.show()
    while new_image.difference > 108810:
        new_image.make_new_shapes()
        new_image.image.show()
    new_image.image.show()


