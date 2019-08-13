
class ConstBooleanFunc:

    def __init__(self, val):
        self.val = val

    def to_json_obj(self):
        return {
            "t": "const",
            "v": self.val
        }


