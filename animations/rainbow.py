
from animations.animation import Animation

from float_func.sin import SinFloatFunc
from float_func.const import ConstFloatFunc
from float_func.linear import LinearFloatFunc
from infra.functions_store import float_functions_store


class Rainbow(Animation):

    name = "rainbow"

    def __init__(self, start_hue, end_hue):
        super(Rainbow, self).__init__()
        self.start_hue = start_hue
        self.end_hue = end_hue

    def get_params_json(self):
        return {
            "startHue": self.start_hue.to_json_obj(),
            "endHue": self.end_hue.to_json_obj()
        }

    def get_compact_params_json(self):
        return {
            "startHue": float_functions_store.get_index(self.start_hue),
            "endHue": float_functions_store.get_index(self.end_hue)
        }



def monochrome_to_colorful(timing, hue, amp = 0.5):
    phase = 0.0
    return Rainbow(timing, SinFloatFunc.from_timing(timing, hue + amp, hue, phase), SinFloatFunc.from_timing(timing, hue - amp, hue, phase))

def static_full_rainbow(timing):
    return Rainbow(timing, ConstFloatFunc(0.0), ConstFloatFunc(1.0))

def moving_full_rainbow(timing):
    return Rainbow(timing, LinearFloatFunc.from_timing(timing, start=0.0), LinearFloatFunc.from_timing(timing, start=1.0))

def very_colorful(timing):
    return Rainbow(timing, SinFloatFunc.from_timing(timing.slower2(), 0.0, 1.0, 0.0), SinFloatFunc.from_timing(timing.slower2(), 1.0, 3.0, 0.0))

def slow_colors_mess(timing):
    return Rainbow(timing, SinFloatFunc.from_timing(timing.change_cycle(0.29), 0.0, 1.0, 0.0), SinFloatFunc.from_timing(timing.change_cycle(0.38), 0.2, 0.8, 0.39))
