from led_objects.led_object import LedObject
from led_objects.objects_selector import elements_flatten

class Flower(LedObject):

    def __init__(self, num_pixels, start_index = 0):
        super(Flower, self).__init__(total_pixels=num_pixels)
        self.mapping = {"a": list(range(start_index, self.total_pixels))}
        self.create_random_for_all()

flower1 = Flower(30)
flower6 = Flower(15)

bottle4 = Flower(5)
bottle5 = Flower(5)

paper2 = Flower(5, 2)
paper5 = Flower(5, 3)

gloves8 = Flower(5)
