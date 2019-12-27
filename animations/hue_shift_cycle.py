from animations.animation import Animation

class HueShiftCycleAnimation(Animation):

    name = "hue_shift_c"

    def __init__(self, shift_amount_c):
        super(HueShiftCycleAnimation, self).__init__()
        self.shift_amount_c = shift_amount_c

    def get_params_json(self):
        return {"shiftAmount": self.shift_amount_c.to_json_obj() }


