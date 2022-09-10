from animations.animation import Animation
from animations.animations_common import hsv_to_json


class AlternateColoringAnimation(Animation):

    name = "al"

    def __init__(self, c1, c2, number_of_pixels=3):
        super(AlternateColoringAnimation, self).__init__()
        self.c1 = c1
        self.c2 = c2
        self.number_of_pixels = number_of_pixels

    def get_params_json(self):
        return {
            "hsv1": hsv_to_json(self.c1),
            "hsv2": hsv_to_json(self.c2),
            "numPix": self.number_of_pixels,
        }

    def get_compact_params_json(self):
        return {
            "hsv1": hsv_to_json(self.c1),
            "hsv2": hsv_to_json(self.c2),
            "numPix": self.number_of_pixels,
        }
