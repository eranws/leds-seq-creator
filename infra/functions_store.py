import json


class FunctionsStore:

    def __init__(self):
        self.reset()

    def reset(self):

        # the index in the list is the index of the func
        # the value is the json obj
        self.saved_func_by_index = list()

        # maps json str to the index in the above list
        self.json_str_to_index = dict()

    def get_index(self, func_obj):
        """
        gets an index for object representing rendering function

        :param func_obj:
        :return: an index for this function
        """

        json_obj = func_obj.to_compact_json_obj()
        json_str = json.dumps(json_obj, separators=(',',':'))
        if json_str in self.json_str_to_index:
            return self.json_str_to_index[json_str]

        self.saved_func_by_index.append(json_obj)
        index = len(self.saved_func_by_index)
        self.json_str_to_index[json_str] = index


float_functions_store = FunctionsStore()
boolean_functions_store = FunctionsStore()
discrete_float_functions_store = FunctionsStore()