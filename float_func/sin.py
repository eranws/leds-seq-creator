
class SinFloatFunc:

    def __init__(self, min_value, max_value, phase, repeats):
        """ Initialize sin function with explicit paramters """
        self.min_value = min_value
        self.max_value = max_value
        self.phase = phase
        self.repeats = repeats

    @classmethod
    def from_timing(cls, timing, beats_per_cycle, min_value, max_value, phase):
        num_of_cycles = timing.number_of_beats() / beats_per_cycle
        return cls(min_value, max_value, phase, num_of_cycles)

    def to_json_obj(self):
        return {
            "t": "sin",

            "min": self.min_value,
            "max": self.max_value,
            "phase": self.phase,
            "rep": self.repeats
        }

    def to_compact_json_obj(self):
        return {
            "t": "sin",

            "min": self.min_value,
            "max": self.max_value,
            "phase": self.phase,
            "rep": self.repeats
        }
