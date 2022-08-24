from led_objects.led_object import LedObject
from led_objects.objects_selector import elements_flatten


class Twist(LedObject):
    def __init__(self, num_pixels):
        super(Twist, self).__init__(total_pixels=num_pixels)

cabbage1 = Twist(200)
cabbage6 = Twist(50)
cabbage5 = Twist(50)

brain7 = Twist(299)
cup_cake4 = Twist(300)

donut1 = Twist(296)
donut3 = Twist(296)

