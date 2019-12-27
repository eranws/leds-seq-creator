from animations.animation import Animation
from float_func.linear import LinearFloatFunc
from float_func.steps import StepsFloatFunc


class RandBrightnessAnimation(Animation):

    name = "rand_brightness"

    def __init__(self):
        super(RandBrightnessAnimation, self).__init__()

    def get_params_json(self):
        return {}

    def get_compact_params_json(self):
        return {}
