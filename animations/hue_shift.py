from animations.animation import Animation
from float_func.linear import LinearFloatFunc
from float_func.steps import StepsFloatFunc


class HueShiftAnimation(Animation):

    name = "hue_shift"

    def __init__(self, shift_amount):
        super(HueShiftAnimation, self).__init__()
        self.shift_amount = shift_amount

    def get_params_json(self):
        return {"shiftAmount": self.shift_amount.to_json_obj() }


def hue_shift_smooth(timing):
    return HueShiftAnimation(timing, LinearFloatFunc.from_timing(timing, 0.0, 1.0))


def hue_shift_jump_on_cycle(timing, cycles_for_restart = 4):
    diff_per_cycle = 1.0 / cycles_for_restart
    return HueShiftAnimation(timing, StepsFloatFunc.from_timing(timing, diff_per_cycle, 0.0))
