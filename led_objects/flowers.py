from led_objects.led_object import LedObject

class Flower(LedObject):

    def __init__(self, num_pixels, start_index = 0):
        super(Flower, self).__init__(total_pixels=num_pixels)
        self.mapping = {"a": list(range(start_index, self.total_pixels))}
        self.create_random_for_all()
