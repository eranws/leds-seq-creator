
class StepsFloatFunc:

    def __init__(self, num_of_steps, value_diff, initial_value):
        self.num_of_steps = num_of_steps
        self.value_diff = value_diff
        self.initial_value = initial_value

    @classmethod
    def from_timing(cls, timing, diff = 0.25, initial_value = 0.0):
        return cls(timing.number_of_repeats(), diff,initial_value)

    def to_json_obj(self):
        return {
            "t": "steps",

            "num": self.num_of_steps,
            "diff": self.value_diff,
            "init": self.initial_value
        }

    def to_compact_json_obj(self):
        return {
            "t": "steps",

            "num": self.num_of_steps,
            "diff": self.value_diff,
            "init": self.initial_value
        }

