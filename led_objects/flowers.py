from led_objects.led_object import LedObject
from led_objects.objects_selector import elements_flatten

class Flower(LedObject):

    def __init__(self, num_pixels, start_index = 0):
        super(Flower, self).__init__(total_pixels=num_pixels)
        self.mapping = {"a": list(range(start_index, self.total_pixels))}
        self.create_random_for_all()

flower1 = Flower(200)
flower6 = Flower(150)

bottle4 = Flower(50)
bottle5 = Flower(50)

paper2 = Flower(50, 9)
paper5 = Flower(50, 12)

gloves8 = Flower(50)
