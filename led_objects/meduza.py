from led_objects.led_object import LedObject, SegmentProxy


class Meduza(LedObject):

    def __init__(self):
        super(Meduza, self).__init__(total_pixels=94, add_to_all=False)
        self.mapping["strings"] = list(range(0, 54))
        self.mapping["top"] = list(range(54, 94))

    def strings(self):
        return SegmentProxy(self, "strings")

    def top(self):
        return SegmentProxy(self, "top")


meduza = Meduza()
