from animations.animation import Animation
from infra.functions_store import discrete_float_functions_store


class HueShiftCycleAnimation(Animation):

    name = "hue_shift_c"

    def __init__(self, shift_amount_c):
        super(HueShiftCycleAnimation, self).__init__()
        self.shift_amount_c = shift_amount_c

    def get_params_json(self):
        return {"shiftAmount": self.shift_amount_c.to_json_obj()}

    def get_compact_params_json(self):
        return {
            "shiftAmount": discrete_float_functions_store.get_index(self.shift_amount_c)
        }
