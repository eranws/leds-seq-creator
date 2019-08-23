from animations.animation import Animation


class FillAnimation(Animation):

    name = "fill"

    def __init__(self, start_pos, end_pos):
        super(FillAnimation, self).__init__()
        self.start_pos = start_pos
        self.end_pos = end_pos

    def get_params_json(self):
        return {
            "fill_start_pos": self.start_pos.to_json_obj(),
            "fill_end_pos": self.end_pos.to_json_obj()
            }
