from animations import brightness
from animations.hue_shift import hue_shift_jump_on_cycle
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.common import no_stands
from led_objects.flood import cup_cakes, rug4, rugs, cup_cake3, rug6
from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles, paper2, flower1, bottle4, bottle5
from led_objects.meduza import meduza
from led_objects.objects_selector import elements
from led_objects.sheep import sheep
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands, \
    single_lifas, single_stands
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=60, beats_per_episode=1, start_offset=0)

#AHHHHHH
beats(3.7, 6.75)
elements(papers)
color.uniform((0.39, 0.55, 0.5))
effect.breath(edge=0.5)

beats(6.75, 9)
elements(papers)
color.uniform((0.39, 0.55, 1.0))
effect.breath(edge=0.5)

beats(7, 9)
effect.fade_out()

half_all_1 = all[0: len(all) / 2]
half_all_2 = all[len(all) / 2: len(all)]

for e in all:
    e.random

beats(9, 21)
elements(all)
color.uniform((0.39, 0.55, 1.0))
cycle(6)
effect.segment_breath(0.5)

beats(9, 11)
effect.fade_in()
beats(19, 21)
effect.fade_out()

for e in all:
    e.straight

beats(21.73, 33.5)
elements(all)
color.uniform((0.39, 0.55, 1.0))
cycle(6)
effect.segment_breath(0.5)

beats(21.73, 23.73)
effect.fade_in()
beats(31.5, 33.5)
effect.fade_out()


# def note(start, end, elem):
#     beats(start, end)
#     elements(elem)
#     color.uniform((0.39, 0.55, 1.0))
#     effect.fade_out()
#
# def note_list(start_vec, end, elem_vec, change_color = False):
#     for i in range(0, len(start_vec)):
#         elem_index = elem_vec[i] % len(all)
#         elem = all[elem_index]
#         note(start_vec[i], end, elem)
#
#         if change_color:
#             effect.hue_shift(i / 10.0)
#
# def note_list_groups(start_vec, end, elem_vec, change_color = False):
#     for i in range(0, len(start_vec)):
#         note(start_vec[i], end, elem_vec[i])
#         if change_color:
#             effect.hue_shift(i / 6.0)
#
# note_list([9.1, 9.87, 10.86, 11.43, 12, 12.89], 13.72, range(0, 6))
#
# note_list([14.08, 14.39, 15.13], 20.7, range(6, 9))
#
# note_list([15.85, 17.31, 17.75, 18.1, 18.45, 18.8, 19.2], 20.7, range(9, 16), True)
#
#
# note_list_groups([21.7, 22.13], 24.69, [flowers, sticks])
#
# note_list_groups([24.69, 25.24], 27, [papers, lifas])
#
# note_list_groups([27.45, 28.13], 33.55, [bottles, cup_cakes])
# note_list_groups([30.85, 31.12, 31.47], 33.55, [cabbage1, cabbage5, cabbage6], True)






send_to_mqtt("because")
start_song("because", 3)


