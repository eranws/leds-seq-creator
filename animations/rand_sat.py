from animations.animation import Animation
from float_func.linear import LinearFloatFunc
from float_func.steps import StepsFloatFunc


class RandSaturationAnimation(Animation):

    name = "rand_sat"

    def __init__(self):
        super(RandSaturationAnimation, self).__init__()

    def get_params_json(self):
        return {}

    def get_compact_params_json(self):
        return {}
