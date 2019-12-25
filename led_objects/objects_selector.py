import itertools

from led_objects.led_object import LedObject, SegmentProxy

stored_objects = []


def get_elements():
    global stored_objects
    return stored_objects


def should_unapack(elems):
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
    while should_unapack(unpacked):
        unpacked = unpack_elements(unpacked)
    return unpacked


def elements(*args):
    global stored_objects
    unpacked = elements_flatten(args)
    stored_objects = [SegmentProxy(obj, obj.default_mapping()) if isinstance(obj, LedObject) else obj for obj in unpacked]
