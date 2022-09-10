from led_objects.led_object import LedObject, SegmentProxy


class Stands(LedObject):
    def __init__(self, last_index_per_stick):
        super(Stands, self).__init__(total_pixels=last_index_per_stick[-1])

        self.num_of_sticks = len(last_index_per_stick)

        last_index_per_stick.insert(0, 0)
        self.mapping.update(
            {
                str(i): list(
                    range(last_index_per_stick[i - 1], last_index_per_stick[i])
                )
                for i in range(1, len(last_index_per_stick))
            }
        )

    def stand(self, index):
        if index < 1 or index > self.num_of_sticks:
            raise Exception("stick index {} not valid".format(index))
        return SegmentProxy(self, str(index))

    @property
    def all(self):
        return [SegmentProxy(self, str(i)) for i in range(1, self.num_of_sticks + 1)]
