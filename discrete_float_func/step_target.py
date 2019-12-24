
class StepTargetDiscreteFloatFunc:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def to_json_obj(self):
        return {
            "t": "step_target",
            "start": self.start,
            "end": self.end,
        }
