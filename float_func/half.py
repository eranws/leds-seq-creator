from infra.functions_store import float_functions_store


class HalfFloatFunc:

    def __init__(self, func1, func2):
        self.func1 = func1
        self.func2 = func2

    def to_json_obj(self):
        return {
            "t": "half",
            "f1": self.func1.to_json_obj(),
            "f2": self.func2.to_json_obj(),
        }

    def to_compact_json_obj(self):
        return {
            "t": "half",
            "f1": float_functions_store.get_index(self.func1),
            "f2": float_functions_store.get_index(self.func2),
        }

