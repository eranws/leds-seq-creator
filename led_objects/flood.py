from led_objects.led_object import LedObject

class Flood(LedObject):

    def __init__(self, num_pixels):
        super(Flood, self).__init__(total_pixels=num_pixels)

cup_cake3 = Flood(10)
rug6 = Flood(30)
rug4 = Flood(24)

