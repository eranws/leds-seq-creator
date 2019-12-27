from infra.functions_store import float_functions_store


class Comb2FloatFunc:

    def __init__(self, amount1, func1, amount2, func2):
        self.amount1 = amount1
        self.func1 = func1
        self.amount2 = amount2
        self.func2 = func2

    def to_json_obj(self):
        return {
            "t": "comb2",
            "amount1": self.amount1,
            "f1": self.func1.to_json_obj(),
            "amount2": self.amount2,
            "f2": self.func2.to_json_obj(),
        }

    def to_compact_json_obj(self):
        return {
            "t": "comb2",
            "amount1": self.amount1,
            "f1": float_functions_store.get_index(self.func1),
            "amount2": self.amount2,
            "f2": float_functions_store.get_index(self.func2),
        }
