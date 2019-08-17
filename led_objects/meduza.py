from led_objects.led_object import LedObject

class Meduza(LedObject):

    def __init__(self):
        super(Meduza, self).__init__(total_pixels=302)
        # self.mapping = {"a": list(range(self.total_pixels)), "r": random_index}


meduza = Meduza()
