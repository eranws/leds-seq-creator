from led_objects.led_object import LedObject

cabbages = []


class Twist(LedObject):

    def __init__(self, num_pixels):
        super(Twist, self).__init__(total_pixels=num_pixels)
        #cabbages.append(self)


cabbage1 = Twist(260)
cabbage6 = Twist(300)
cabbage5 = Twist(300)

cabbages = [cabbage1, cabbage6, cabbage5]

brain7 = Twist(299)
cup_cake4 = Twist(300)

brains = [brain7]

twists = [cabbages, brains]


donut1 = Twist(296)
donut3 = Twist(296)

donuts = [donut1, donut3]
