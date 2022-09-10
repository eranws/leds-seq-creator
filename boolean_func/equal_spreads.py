class EqualSpreadsBooleanFunc:
    def __init__(self, num_of_spreads, initial_state=True):
        self.num_of_spreads = num_of_spreads
        self.initial_state = initial_state

    def to_json_obj(self):
        return {
            "t": "equalSpreads",
            "num": self.num_of_spreads,
            "init": self.initial_state,
        }

    def to_compact_json_obj(self):
        return {
            "t": "equalSpreads",
            "num": self.num_of_spreads,
            "init": self.initial_state,
        }


def change_on_cycle(timing, initial_state=True):
    return EqualSpreadsBooleanFunc(timing.number_of_repeats(), initial_state)
