from led_objects.led_object import LedObject, SegmentProxy
from led_objects.objects_selector import elements_flatten


class Stands(LedObject):

    def __init__(self, last_index_per_stick):
        super(Stands, self).__init__(total_pixels=last_index_per_stick[-1])

        self.num_of_sticks = len(last_index_per_stick)

        last_index_per_stick.insert(0, 0)
        self.mapping.update({ str(i): list(range(last_index_per_stick[i-1], last_index_per_stick[i])) for i in range(1, len(last_index_per_stick))})

    def stand(self, index):
        if index < 1 or index > self.num_of_sticks:
            raise Exception("stick index {} not valid".format(index))
        return SegmentProxy(self, str(index))

    @property
    def all(self):
        return [SegmentProxy(self, str(i)) for i in range(1, self.num_of_sticks + 1)]


sticks8 = Stands([12, 31, 46, 56, 72])
sticks7 = Stands([16, 29, 51, 68, 87, 103])
sticks3 = Stands([55, 106, 150, 190, 227])


lifas5 = Stands([38, 72, 106, 147, 193])
lifas1 = Stands([45, 84, 103, 131, 164])
lifas4 = Stands([55, 122, 178, 228])

