
class StepDiffDiscreteFloatFunc:

    def __init__(self, start, dx):
        self.start = start
        self.dx = dx

    def to_json_obj(self):
        return {
            "t": "step_diff",
            "start": self.start,
            "dx": self.dx,
        }
