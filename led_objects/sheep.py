from led_objects.led_object import LedObject, SegmentProxy


class Sheep(LedObject):

    def __init__(self):
        super(Sheep, self).__init__(total_pixels=302)

        self.mapping["head"] = list(range(0, 52))

        self.mapping["bp0"] = list(range(56, 70))
        self.mapping["bp1"] = list(range(108, 121))
        self.mapping["bp2"] = list(range(121, 135))
        self.mapping["bp3"] = list(range(175, 187))
        self.mapping["bp4"] = list(range(189, 201))
        self.mapping["bp5"] = list(range(201, 216))
        self.mapping["bp6"] = list(range(216, 231))
        self.mapping["bp7"] = list(range(231, 246))
        self.mapping["bp8"] = list(range(246, 260))
        self.mapping["bp9"] = list(range(260, 275))

        self.mapping["leg_fl"] = list(range(71, 84))
        self.mapping["leg_fr"] = list(range(92, 106))
        self.mapping["leg_bl"] = list(range(138, 151))
        self.mapping["leg_br"] = list(range(159, 173))

        self.mapping["eyes"] = [275, 276]

        all_bp_lists = [self.mapping["bp" + str(i)] for i in range(0, 10)]
        all_bp_flat = [item for sublist in all_bp_lists for item in sublist]
        self.mapping["a"] = self.mapping["head"] + self.mapping["leg_fl"] + self.mapping["leg_fr"] + \
                            self.mapping["leg_bl"] + self.mapping["leg_br"] + self.mapping["eyes"] + all_bp_flat


    def leg_front_left(self):
        return SegmentProxy(self, "leg_fl")

    def leg_front_right(self):
        return SegmentProxy(self, "leg_fr")

    def leg_back_left(self):
        return SegmentProxy(self, "leg_bl")

    def leg_back_right(self):
        return SegmentProxy(self, "leg_br")

    def head(self):
        return SegmentProxy(self, "head")

    def body_part(self, index):
        return SegmentProxy(self, "bp" + str(index))

    def eyes(self):
        return SegmentProxy(self, "eyes")


sheep = Sheep()
