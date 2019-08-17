from led_objects.led_object import LedObject


class Sheep(LedObject):

    head = range(0, 51)

    def __init__(self):
        super(Sheep, self).__init__(total_pixels=302)
        # self.mapping = {"a": list(range(self.total_pixels)), "r": random_index}
        self.mapping



sheep = Sheep()
