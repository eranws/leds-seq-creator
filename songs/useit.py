from infra.animations_factory import color, effect
from led_objects.instances import *
from led_objects.groups import *
from led_objects.led_object import all
from led_objects.meduza import meduza
from led_objects.objects_selector import elements
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=125, beats_per_episode=32, start_offset=3)


"""
Episode 0: intro, bobjects enter the scene graduately
"""
def fade_in_blink_0(e, start_beat):
    episodes(0 + start_beat / 32, 1)
    elements(e)
    color.uniform((0.72, 1.0, 1.0))
    episodes(0 + start_beat / 32, 0 + (start_beat + 4) / 32)
    effect.blink_repeat(16, 0.3)
    effect.fade_in()

fade_in_blink_0([flowers, rugs], 0)
fade_in_blink_0([papers, bottles], 8)
fade_in_blink_0([cup_cakes, donuts], 16)
fade_in_blink_0([cabbages, brains], 24)

def snake_on_sticks(e, start_beat):
    beats(start_beat, start_beat + 8)

episode(0)
cycle(16)
cycle_beats(2, 8)
elements(single_stands)
color.uniform((0.72, 0.7, 1.0))
effect.snake(4.0, True)
effect.snake(4.0, False)

"""
episodes 1, 2, 3, 4
"""
elements(no_stands)

c1 = (0.72, 1.0, 0.6)
c2 = (0.82, 1.0, 0.6)

episode(1)
cycle(4)
cycle_beats(0, 2)
color.uniform(c1)
cycle_beats(2, 4)
color.uniform(c2)

episode(2)
cycle(4)
cycle_beats(0, 2)
color.alternate(c1, c2, 5)
cycle_beats(2, 4)
color.alternate(c2, c1, 5)

episode(3)
cycle(4)
cycle_beats(0, 2)
color.alternate(c1, c2, 25)
cycle_beats(2, 4)
color.alternate(c2, c1, 25)

episode(4)
cycle(4)
cycle_beats(0, 2)
color.gradient(0.72, 0.82)
cycle_beats(2, 4)
color.gradient(0.82, 0.72)



episodes(1, 5)
cycle(16)
cycle_beats(12, 16)
elements(single_stands)
color.uniform((0.72, 0.7, 1.0))
effect.fade_in()

elements(all)
effect.blink_repeat(32, 0.2)

"""
episode 5 melody
"""
def melody_on_sticks_6(stand, cycle_beat_index, length, c):
    e = [sticks3.stand(stand), sticks7.stand(stand), sticks8.stand(stand)]
    episodes(5 + cycle_beat_index / 32.0, 6)
    elements(e)
    cycle(4)
    cycle_beats(0, length)
    color.uniform(c)
    effect.snake(length)

    episodes(6, 7)
    elements(e)
    color.uniform(c)
    cycle(8)
    effect.breath()

melody_on_sticks_6(1, 0, 2.0, (0.72, 1.0, 1.0))
melody_on_sticks_6(2, 0.75, 2.0, (0.72, 1.0, 1.0))
melody_on_sticks_6(3, 1.5, 2.0, (0.72, 1.0, 1.0))
melody_on_sticks_6(4, 2.75, 1.0, (0.82, 1.0, 1.0))
melody_on_sticks_6(5, 3, 1.0, (0.82, 1.0, 1.0))

episodes(6, 10)
cycle(32)

def snake_on_object_7(o, beat_start, length, c):
    episodes(6 + beat_start / 32.0, 7)
    cycle(4)
    cycle_beats(0, length)
    o.random
    elements(o)
    color.uniform(c)
    effect.snake(4.0)

snake_on_object_7(cabbage1, 0, 2.0, (0.72, 1.0, 1.0))
snake_on_object_7(cabbage5, 0.75, 2.0, (0.72, 1.0, 1.0))
snake_on_object_7(cabbage6, 1.5, 2.0, (0.72, 1.0, 1.0))
snake_on_object_7(paper2, 2.75, 1.0, (0.82, 1.0, 0.5))
snake_on_object_7(paper5, 3.0, 1.0, (0.82, 1.0, 0.5))

episodes(7, 8)
for e in all:
    e.straight
elements(all)
color.gradient(0.72, 0.82)
cycle(8)

cycle_beats(0, 4)
effect.snake()

for e in all:
    e.random
elements(all)
cycle_beats(4, 8)
effect.snake()


episode(8)
elements([donut1, flower1, cabbage1, cup_cake3, donut3, sticks3, bottle4, paper5, cabbage5, rug6, cabbage6, flower6])
color.uniform((0.72, 1.0, 0.25))
elements([lifas1, paper2, rug4, lifas4, lifas5, bottle5, brain7, sticks7])
color.uniform((0.82, 1.0, 0.25))

def ligth_on_beat(beat_start, length, e, c):
    cycle(16)
    cycle_beats(beat_start, beat_start + length)
    elements(e)
    color.uniform(c)
    effect.saw_tooth(0.75)

ligth_on_beat(0, 2.0, donut1, (0.72, 1.0, 1.0))
ligth_on_beat(0.75, 2.0, flower1, (0.72, 1.0, 1.0))
ligth_on_beat(1.5, 2.0, cabbage1, (0.72, 1.0, 1.0))
ligth_on_beat(2.75, 1.0, lifas1, (0.82, 1.0, 1.0))
ligth_on_beat(3.0, 1.0, paper2, (0.82, 1.0, 1.0))

ligth_on_beat(4.0 + 0, 2.0, cup_cake3, (0.72, 1.0, 1.0))
ligth_on_beat(4.0 + 0.75, 2.0, donut3, (0.72, 1.0, 1.0))
ligth_on_beat(4.0 + 1.5, 2.0, sticks3, (0.72, 1.0, 1.0))
ligth_on_beat(4.0 + 2.75, 1.0, rug4, (0.82, 1.0, 1.0))
ligth_on_beat(4.0 + 3.0, 1.0, lifas4, (0.82, 1.0, 1.0))

ligth_on_beat(8.0 + 0, 2.0, bottle4, (0.72, 1.0, 1.0))
ligth_on_beat(8.0 + 0.75, 2.0, paper5, (0.72, 1.0, 1.0))
ligth_on_beat(8.0 + 1.5, 2.0, cabbage5, (0.72, 1.0, 1.0))
ligth_on_beat(8.0 + 2.75, 1.0, lifas5, (0.82, 1.0, 1.0))
ligth_on_beat(8.0 + 3.0, 1.0, bottle5, (0.82, 1.0, 1.0))

ligth_on_beat(12.0 + 0, 2.0, rug6, (0.72, 1.0, 1.0))
ligth_on_beat(12.0 + 0.75, 2.0, cabbage6, (0.72, 1.0, 1.0))
ligth_on_beat(12.0 + 1.5, 2.0, flower6, (0.72, 1.0, 1.0))
ligth_on_beat(12.0 + 2.75, 1.0, brain7, (0.82, 1.0, 1.0))
ligth_on_beat(12.0 + 3.0, 1.0, sticks7, (0.82, 1.0, 1.0))

"""
Episode 9
"""

def alternate_change_9(start_beat, e):
    episodes(9 + start_beat / 32.0, 10)
    elements(e)
    cycle(4)
    cycle_beats(0, 0.75)
    color.alternate((0.72, 1.0, 1.0), (0.82, 1.0, 1.0))
    cycle_beats(0.75, 1.5)
    color.alternate((0.82, 1.0, 1.0), (0.72, 1.0, 1.0))
    cycle_beats(1.5, 2.75)
    color.alternate((0.72, 1.0, 1.0), (0.82, 1.0, 1.0))
    cycle_beats(2.75, 3.0)
    color.alternate((0.82, 1.0, 1.0), (0.72, 1.0, 1.0))
    cycle_beats(3.0, 4.0)
    color.alternate((0.72, 1.0, 1.0), (0.82, 1.0, 1.0))

alternate_change_9(0, flowers)
alternate_change_9(8, bottles)
alternate_change_9(16, donuts)
alternate_change_9(24, papers)

"""
episode 10 - DARK
"""

"""
episode 11 - sing - color crazy
"""
episode(11)
elements(all)
color.uniform((0.72, 1.0, 0.3))

episode(12)
elements(all)
color.uniform((0.9, 1.0, 0.3))
effect.hue_saw_tooth(0.1 + 1.0/12.0)

episodes(11.0, 11.125)
effect.fade_in()

def breath_elements_11_13(elem, cycle_amount, beat_offset, edge):
    episodes(11.5 + beat_offset / 32, 13.0)
    elements(elem)
    cycle(cycle_amount)
    effect.breath(edge, True)

breath_elements_11_13([flower1, cup_cake3], 4, 0, 0.3)
breath_elements_11_13([brain7, rug4, sticks7], 8, 0, 0.4)

breath_elements_11_13([cabbage1, bottle5, donut1], 4, 1, 0.5)
breath_elements_11_13([bottle4, flower6, sticks7], 16, 1, 0.6)

breath_elements_11_13([paper5, sticks8, cabbage5], 4, 2, 0.3)
breath_elements_11_13([donut3, lifas5], 8, 2, 0.8)

breath_elements_11_13([lifas1, sticks3, lifas4], 4, 3, 0.3)
breath_elements_11_13([cabbage6, paper2], 8, 3, 0.8)

episode(13)
elements(all)
color.uniform((1.0/12.0, 1.0, 1.0))

episodes(13 + 9/32.0, 13 + 11/32.0)
effect.saw_tooth(0.7)
episodes(13 + 11/32.0, 13 + 15/32.0)
effect.brightness(0.3)
episodes(13 + 15/32.0, 13 + 15.5/32.0)
effect.saw_tooth(0.7, True)
episodes(13+31/32.0, 14)
color.uniform(black)

elements(meduza)
color.uniform((0.72, 1.0, 1.0))

for e in all:
    e.straight

def snake_group_14(g, start_beat):
    episodes(14 + start_beat / 32.0, 15 + start_beat / 32.0)
    cycle(8)
    cycle_beats(0, 4)
    elements(g)
    color.uniform((0.72, 1.0, 1.0))
    effect.snake(3)

snake_group_14(group1, 0)
snake_group_14(group2, 1)
snake_group_14(group3, 2)
snake_group_14(group4, 3)
snake_group_14(group5, 4)
snake_group_14(group6, 5)
snake_group_14(group7, 6)
snake_group_14(group8, 7)


def turn_off_on_15(e, beat_index, c):
    episodes(15 + beat_index / 32.0, 16 + beat_index / 32.0)
    elements(e)
    cycle(4)
    cycle_beats(0, 2)
    color.uniform(c)
    effect.saw_tooth(edge=1.0, reverse=False)


turn_off_on_15(group1, 0, (0.72, 1.0, 1.0))
turn_off_on_15(group3, 0.75, (0.72, 1.0, 1.0))
turn_off_on_15(group4, 1.5, (0.72, 1.0, 1.0))
turn_off_on_15(group5, 2.75, (0.82, 1.0, 1.0))
turn_off_on_15(group6, 3.0, (0.82, 1.0, 1.0))

episode(16)
elements(single_stands)
color.uniform((0.72, 1.0, 1.0))

cycle(4)
cycle_beats(0.0, 0.75)
effect.segment_up(0.2)
cycle_beats(0.75, 1.5)
effect.segment_down(0.2)
cycle_beats(1.5, 2.75)
effect.segment_up(0.2)
cycle_beats(2.75, 3.0)
effect.segment_down(0.1)
cycle_beats(3.0, 3.25)
effect.segment_up(0.1)
cycle_beats(3.25, 4.0)
color.uniform(black)

cycle_beats(3.25, 4.0)
elements(cabbages)
color.uniform((0.72, 1.0, 1.0))


episodes(17 - 4/32.0, 17)
elements(all)
color.uniform((0.72, 1.0, 1.0))
effect.fill()

episodes(17, 18)
elements(all)
color.uniform((0.72, 1.0, 1.0))

final_hue_shift = 0.1
cycle(4)
cycle_beats(0, 0.75)
effect.hue_shift(1.0 * final_hue_shift / 5.0)
cycle_beats(0.75, 1.5)
effect.hue_shift(2.0 * final_hue_shift / 5.0)
cycle_beats(1.5, 2.75)
effect.hue_shift(3.0 * final_hue_shift / 5.0)
cycle_beats(2.75, 3.0)
effect.hue_shift(4.0 * final_hue_shift / 5.0)
cycle_beats(3.0, 4.0)
effect.hue_shift(5.0 * final_hue_shift / 5.0)

cycle(16)
cycle_beats(8, 13)
elements(meduza)
color.uniform(yellow_string)
cycle(1)
effect.saw_tooth()

episodes(18, 18 + 0.5/32.0)
elements(all)
color.uniform((0.82, 1.0, 1.0))
effect.fill_out()

send_to_mqtt("useit")
start_song("useit", 0)


