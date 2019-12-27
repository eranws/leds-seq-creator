from led_objects import flowers, cabbages
from led_objects.led_object import LedObject
from led_objects.objects_selector import elements_flatten


class Flood(LedObject):

    def __init__(self, num_pixels):
        super(Flood, self).__init__(total_pixels=num_pixels)


cup_cake3 = Flood(100)
cup_cake4 = cabbages.cup_cake4

cup_cakes = elements_flatten([cup_cake4, cup_cake3])

rug6 = Flood(300)
rug4 = Flood(240)

rugs = elements_flatten([rug4, rug6])

floods = elements_flatten([cup_cakes, rugs])
