class LinearFloatFunc:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @classmethod
    def from_timing(cls, timing, start=0.0, diff_per_cycle=1.0):
        return cls(start, start + timing.number_of_repeats() * diff_per_cycle)

    def to_json_obj(self):
        return {"t": "lin", "start": self.start, "end": self.end}

    def to_compact_json_obj(self):
        return {"t": "lin", "start": self.start, "end": self.end}
