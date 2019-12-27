from animations.animation import Animation
from infra.functions_store import float_functions_store


class SnakeAnimation(Animation):

    name = "snake"

    def __init__(self, head_pos, length, dir):
        super(SnakeAnimation, self).__init__()
        self.dir = dir
        self.length = length
        self.head_pos = head_pos

    def get_params_json(self):
        return {
            "headPos": self.head_pos.to_json_obj(),
            "length": self.length.to_json_obj(),
            "dir": self.dir.to_json_obj()
        }

    def get_compact_params_json(self):
        return {
            "headPos": float_functions_store.get_index(self.head_pos),
            "length": float_functions_store.get_index(self.length),
            "dir": self.dir.to_json_obj()
        }
