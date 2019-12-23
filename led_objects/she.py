from led_objects.led_object import LedObject, SegmentProxy


class She(LedObject):

    def __init__(self):
        super(She, self).__init__(total_pixels=1006)

        self.mapping["b"] = list(range(100, 291))
        self.mapping["rw"] = list(range(291, 421))
        self.mapping["lw"] = list(range(455, 587))
        self.mapping["h"] = list(range(587, 707))
        self.mapping["o1"] = list(range(707, 861))
        self.mapping["o2"] = list(range(861, 1006))

    def body(self):
        return SegmentProxy(self, "b")

    def right_wing(self):
        return SegmentProxy(self, "rw")

    def left_wing(self):
        return SegmentProxy(self, "lw")

    def hair(self):
        return SegmentProxy(self, "h")

    def orbit1(self):
        return SegmentProxy(self, "o1")

    def orbit2(self):
        return SegmentProxy(self, "o2")


she = She()

