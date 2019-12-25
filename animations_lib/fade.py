import random

from infra.animations_factory import effect, color
from infra.timing import beats, cycle, get_timing, set_timing
from led_objects.groups import group1, group2, group8, group3, group6, group4, group7, group5
from led_objects.objects_selector import elements

front_to_back = [group1, [group2, group8], [group3, group6], group4, group7, group5]
back_to_front = list(reversed([group1, [group2, group8], [group3, group6], group4, group7, group5]))
right_to_left = [[group3, group4], [group2, group7], [group8], [group1, group5], group6]
left_to_right = list(reversed([[group3, group4], [group2, group7], [group8], [group1, group5], group6]))

spcial_order = [front_to_back, back_to_front, right_to_left, left_to_right]


def fade_out_gradually(fade_order):
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
        effect.fade_out()
        cycle(0.1)
        effect.blink(0.03)

    set_timing(orig_timing)


def fade_out_wave(fade_order, overlap = 0.0):
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
        effect.fade_out()
        cycle(0.1)
        effect.blink(0.03)

        # make the element dark when fade out ends
        beats(elem_timing.end_beat_index, orig_timing.end_beat_index)
        color.uniform((0.0, 0.0, 0.0))

    set_timing(orig_timing)


def fade_out_gradually_rand():
    fade_order = random.choice(spcial_order)
    fade_out_gradually(fade_order)


def fade_out_wave_rand():
    fade_order = random.choice(spcial_order)
    fade_out_wave(fade_order, 3)


