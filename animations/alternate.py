from animations.animation import Animation

import boolean_func.equal_spreads as equal_spreads
from float_func.const import ConstFloatFunc
from float_func.linear import LinearFloatFunc
from float_func.repeat import RepeatFloatFunc
from float_func.sin import SinFloatFunc
from infra.functions_store import float_functions_store


class AlternateAnimation(Animation):

    name = "alternate"

    def __init__(self, timing, number_of_pixels, state_func, hue_shift_func):
        super(AlternateAnimation, self).__init__(timing)
        self.number_of_pixels = number_of_pixels
        self.state_func = state_func
        self.hue_shift_func = hue_shift_func

    def get_params_json(self):
        return {
            "numPix": self.number_of_pixels,
            "stateFunc": self.state_func.to_json_obj(),
            "hueShiftFunc": self.hue_shift_func.to_json_obj()
        }

    def get_compact_params_json(self):
        return {
            "numPix": self.number_of_pixels,
            "stateFunc": self.state_func.to_json_obj(),
            "hueShiftFunc": float_functions_store.get_index(self.hue_shift_func)
        }



def change_on_cycle_adjacent_hues(timing, number_of_pixels = 3):
    return AlternateAnimation(timing, number_of_pixels, equal_spreads.change_on_cycle(timing), ConstFloatFunc(0.1))

def change_on_cycle_oppsite_hues(timing, number_of_pixels = 3):
    return AlternateAnimation(timing, number_of_pixels, equal_spreads.change_on_cycle(timing), ConstFloatFunc(0.5))

def colors_colide(timing, number_of_pixels = 3, cycles_for_colide = 4):
    liner_drop = LinearFloatFunc(0.8, 0.0)
    saw_tooth = RepeatFloatFunc.from_timing(timing, cycles_for_colide, liner_drop)
    return AlternateAnimation(timing, number_of_pixels, equal_spreads.change_on_cycle(timing), saw_tooth)

def alternate_color_move(timing, number_of_pixels = 3):
    return AlternateAnimation(timing, number_of_pixels, equal_spreads.change_on_cycle(timing), SinFloatFunc.from_timing(timing, -0.25, 0.25, 0))
