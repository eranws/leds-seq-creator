from led_objects.led_object import LedObject, SegmentProxy
from led_objects.objects_selector import elements_flatten


class Star(LedObject):

    def __init__(self, leds_per_cross, dark_center_len):
        super(Star, self).__init__(total_pixels=6*leds_per_cross)

        self.number_of_rays = 12
        self.ray_length = leds_per_cross // 2 - dark_center_len

        self.add_cross_mapping(0, leds_per_cross, dark_center_len, 0, 6)
        self.add_cross_mapping(1, leds_per_cross, dark_center_len, 7, 1)
        self.add_cross_mapping(2, leds_per_cross, dark_center_len, 2, 8)
        self.add_cross_mapping(3, leds_per_cross, dark_center_len, 9, 3)
        self.add_cross_mapping(4, leds_per_cross, dark_center_len, 4, 10)
        self.add_cross_mapping(5, leds_per_cross, dark_center_len, 11, 5)

        for i in range(0, 12):
            reverse_name = str(i) + "r"
            self.mapping[reverse_name] = list(reversed(self.mapping[str(i)]))

        all_segments = [self.mapping[str(i)] for i in range(0, 12)]
        self.mapping["a"] = [item for sublist in all_segments for item in sublist]
        self.create_random_for_all()

    def add_cross_mapping(self, cross_index, leds_per_cross, dark_center_len, first_index, second_index):
        corss_start_index = cross_index * leds_per_cross
        ray_2_part_offset = leds_per_cross // 2 + dark_center_len

        self.mapping[str(first_index)] = list(range(corss_start_index, corss_start_index + self.ray_length))
        second_ray_start = corss_start_index + ray_2_part_offset
        self.mapping[str(second_index)] = list(reversed(range(second_ray_start, second_ray_start + self.ray_length)))

    def ray_out(self, index):
        if index < 0 or index >= self.number_of_rays:
            raise Exception(f"star ray index {index} not valid")
        return SegmentProxy(self, str(index))

    def ray_in(self, index):
        if index < 0 or index >= self.number_of_rays:
            raise Exception(f"star ray index {index} not valid")
        return SegmentProxy(self, str(index) + "r")

    @property
    def all(self):
        return [SegmentProxy(self, str(i)) for i in range(1, self.number_of_rays + 1)]


star7 = Star(50, 3)

stars = elements_flatten([star7])