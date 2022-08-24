from led_objects.led_object import LedObject
from led_objects.objects_selector import elements_flatten


class Twist(LedObject):
    def __init__(self, num_pixels):
        super(Twist, self).__init__(total_pixels=num_pixels)

cabbage1 = LedObject(10) # 50
cabbage6 = Twist(10) # 50
cabbage5 = Twist(10) # 50

brain7 = Twist(29) # 299
cup_cake4 = Twist(30) # 300

donut1 = Twist(29) #296
donut3 = Twist(29) #296


