from led_objects.led_object import LedObject

class Flood(LedObject):

    def __init__(self, num_pixels):
        super(Flood, self).__init__(total_pixels=num_pixels)

cup_cake3 = Flood(100)
# cup_cake4 = cabbages.cup_cake4

rug6 = Flood(300)
rug4 = Flood(240)

