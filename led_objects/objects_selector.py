from led_objects.led_object import LedObject, SegmentProxy

stored_objects = []


def get_elements():
    global stored_objects
    return stored_objects


def should_unpack(elems):
    return any(isinstance(el, list) for el in elems)


def unpack_elements(elems):
    new_elems = []
    for elem in elems:
        if isinstance(elem, list):
            new_elems.extend(elem)
        else:
            new_elems.append(elem)
    return new_elems


def elements_flatten(elems):
    unpacked = unpack_elements(elems)
    while should_unpack(unpacked):
        unpacked = unpack_elements(unpacked)
    return unpacked


def elements(*args):
    global stored_objects
    unpacked = elements_flatten(args)
    stored_objects = [SegmentProxy(obj, obj.default_mapping()) if isinstance(obj, LedObject) else obj for obj in unpacked]

def elements_random(*args):
    global stored_objects
    unpacked = elements_flatten(args)
    if any([obj for obj in unpacked if not isinstance(obj, LedObject)]):
        raise Exception("elements_random(...) can only be called on led objects, not segments")
    stored_objects = [SegmentProxy(obj, "r") for obj in unpacked]








