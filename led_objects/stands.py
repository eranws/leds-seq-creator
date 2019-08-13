from led_objects.led_object import LedObject, SegmentProxy


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


sticks8 = Stands([11, 30, 45, 55, 67])
sticks7 = Stands([17, 31, 53, 70, 91, 107])
sticks3 = Stands([55, 107, 151, 191, 228])

sticks = [sticks3, sticks7, sticks8]
single_sticks = [stick.all for stick in sticks]

lifas5 = Stands([46, 84, 125, 159, 193])
lifas1 = Stands([19, 47, 80, 119, 164])
lifas4 = Stands([78, 145, 201, 256, 306]) # missing 7 - 307

lifas = [lifas1, lifas4, lifas5]
single_lifas = [lifa.all for lifa in lifas]

stands = [sticks, lifas]
single_stands = [single_lifas, single_sticks]