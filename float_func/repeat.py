from infra.functions_store import float_functions_store


class RepeatFloatFunc:

    def __init__(self, num_of_times, func_to_repeat):
        self.num_of_times = num_of_times
        self.func_to_repeat = func_to_repeat

    @classmethod
    def from_timing(cls, timing, beats_per_cycle, func_to_repeat):
        num_of_cycles = timing.number_of_beats() / beats_per_cycle
        return cls(num_of_cycles, func_to_repeat)

    def to_json_obj(self):
        return {
            "t": "repeat",
            "num": self.num_of_times,
            "func": self.func_to_repeat.to_json_obj()
        }

    def to_compact_json_obj(self):
        return {
            "t": "repeat",
            "num": self.num_of_times,
            "func": float_functions_store.get_index(self.func_to_repeat)
        }
