import random

all = []


class LedObject:
    def __init__(self, total_pixels, add_to_all=True):
        self.total_pixels = total_pixels
        self.animations = []
        self.current_mapping = "a"
        self.mapping = {"a": list(range(self.total_pixels))}
        self.create_random_for_all()
        if add_to_all:
            all.append(self)

    def create_random_for_all(self):
        all_copy = self.mapping["a"][:]
        random.shuffle(all_copy)
        self.mapping["r"] = all_copy

    def add_for_segment(self, segments, animation):

        not_found = set(segments).difference(set(self.mapping.keys()))
        if not_found:
            raise Exception(
                "could not find segment with name {} in object".format(not_found)
            )

        self.animations.append(animation)

    def default_mapping(self):
        return self.current_mapping

    @property
    def random(self):
        self.current_mapping = "r"
        return

    @property
    def straight(self):
        self.current_mapping = "a"
        return


class SegmentProxy:
    def __init__(self, led_object, segment_name):
        self._led_object = led_object
        self._segment_name = segment_name

    @property
    def led_object(self):
        return self._led_object

    @property
    def segment_name(self):
        return self._segment_name
