from led_objects.led_object import LedObject

class Flower(LedObject):

    def __init__(self, num_pixels):
        super(Flower, self).__init__(total_pixels=num_pixels)


flower6 = Flower(50)
flower1 = Flower(50)

flowers = [flower1, flower6]

bottle5 = Flower(50)
bottle4 = Flower(50)

bottles = [bottle4, bottle5]

paper5 = Flower(50)
paper2 = Flower(50)

papers = [paper2, paper5]

strings = [flowers, bottles, papers]


