
class ConstDiscreteFloatFunc:

    def __init__(self, const_value):
        self.const_value = const_value

    def to_json_obj(self):
        return {
            "t": "const",
            "val": self.const_value
        }
