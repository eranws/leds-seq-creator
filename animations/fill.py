from animations.animation import Animation
from infra.functions_store import float_functions_store


class FillAnimation(Animation):

    name = "fill"

    def __init__(self, start_pos, end_pos):
        super(FillAnimation, self).__init__()
        self.start_pos = start_pos
        self.end_pos = end_pos

    def get_params_json(self):
        return {
            "fill_start_pos": self.start_pos.to_json_obj(),
            "fill_end_pos": self.end_pos.to_json_obj(),
        }

    def get_compact_params_json(self):
        return {
            "fill_start_pos": float_functions_store.get_index(self.start_pos),
            "fill_end_pos": float_functions_store.get_index(self.end_pos),
        }
