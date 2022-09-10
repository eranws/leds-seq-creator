import random

from animations.brightness import BrightnessAnimation
from animations.fill import FillAnimation
from float_func.const import ConstFloatFunc
from float_func.linear import LinearFloatFunc
from infra.animations_factory import effect, color
from infra.timing import beats, cycle, get_timing, set_timing
from led_objects.groups import (
    group1,
    group2,
    group8,
    group3,
    group6,
    group4,
    group7,
    group5,
)
from led_objects.objects_selector import elements

front_to_back = [group1, [group2, group8], [group3, group6], group4, group7, group5]
back_to_front = list(reversed(front_to_back))
right_to_left = [[group3, group4], [group2, group7], [group8], [group1, group5], group6]
left_to_right = list(reversed(right_to_left))

spcial_order = [front_to_back, back_to_front, right_to_left, left_to_right]

fade_out_options = [BrightnessAnimation(LinearFloatFunc(1.0, 0.0))]

fill_out_options = [
    FillAnimation(ConstFloatFunc(0.0), LinearFloatFunc(1.0, 0.0)),
    FillAnimation(LinearFloatFunc(0.0, 1.0), ConstFloatFunc(1.0)),
    FillAnimation(LinearFloatFunc(0.0, 0.5), LinearFloatFunc(1.0, 0.5)),
]

out_options = [fade_out_options, fill_out_options]


def get_random_fade_func():
    func_class = random.choice(out_options)
    return random.choice(func_class)


def out_gradually(fade_order, func):
    """
    does a fade out effect that swipe the objects over time,
    according to the given order.
    all the element will disappear together at the end of the current time frame.
    elements will start to fade gradually, according to the order in fade_order

    :param fade_order: list of elements, which is the order in which they fade out
    """
    orig_timing = get_timing()
    for i, elem in enumerate(fade_order):
        elements(elem)

        # set the timing for the current fade list
        rel_start = i / len(fade_order)
        elem_timing = orig_timing.copy()
        elem_timing.extend(rel_start, 1.0)
        set_timing(elem_timing)

        # do the actual fade
        func.apply()

    set_timing(orig_timing)


def out_wave(fade_order, func, overlap=0.0):
    """
    does a fade out effect that swipe the objects over time,
    according to the given order.
    all the element will disappear together at the end of the current time frame.
    elements will start to fade gradually, according to the order in fade_order

    :param fade_order: list of elements, which is the order in which they fade out
    :param overlap: number of elements to fade together.
    """
    orig_timing = get_timing()

    total_fade_units = len(fade_order) + overlap

    for i, elem in enumerate(fade_order):
        elements(elem)

        # set the timing for the current fade list
        rel_start = i / total_fade_units
        rel_end = (i + 1 + overlap) / total_fade_units
        elem_timing = orig_timing.copy()
        elem_timing.extend(rel_start, rel_end)
        set_timing(elem_timing)

        # do the actual fade
        func.apply()

        # make the element dark when fade out ends
        beats(elem_timing.end_beat_index, orig_timing.end_beat_index)
        color.uniform((0.0, 0.0, 0.0))

    set_timing(orig_timing)


def fade_out_gradually_rand():
    fade_order = random.choice(spcial_order)
    func = random.choice(fill_out_options)
    out_gradually(fade_order, func)


def fade_out_wave_rand():
    fade_order = random.choice(spcial_order)
    func = random.choice(fill_out_options)
    out_wave(fade_order, func, 3)


fade_out_options = [fade_out_gradually_rand, fade_out_wave_rand]
