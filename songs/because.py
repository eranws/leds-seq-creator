from animations import brightness
from animations.brightness import BrightnessAnimation
from animations.hue_shift import hue_shift_jump_on_cycle
from float_func.sin import SinFloatFunc
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

for e in all:
    e.random

beats(9, 21)
elements(all)
color.uniform((0.39, 0.55, 1.0))
cycle(6)
effect.segment_breath(0.5)

beats(9, 11)
effect.fade_in()
beats(15.85, 21)
effect.hue_breath(hard)
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

beats(34.25, 39)
elements(all)
color.gradient(0.8, 1.1)
effect.breath(1.0)

#Second singing
for e in all:
    e.random

beats(39.5, 51)
elements(all)
color.gradient(0.8, 1.1)
cycle(6)
effect.segment_breath(0.5)

beats(39.5, 41.5)
effect.fade_in()
beats(49, 51)
effect.fade_out()




for e in all:
    e.straight


beats(52, 64)
elements(all)
color.gradient(0.8, 1.1)
cycle(6)
effect.segment_breath(0.5)

beats(52, 54)
effect.fade_in()
beats(62, 64)
effect.fade_out()

elements(papers, cabbages)
beats(40.3, 65)
cycle(0.03)
color.uniform((0.045, 0.75, 1.0))
effect.breath(0.25)
beats(40.3, 42)
effect.fade_in()
beats(62, 65)
effect.fade_out()

beats(65, 68.5)
elements(all)
color.uniform((1.05, 0.9, 1.0))
effect.hue_saw_tooth(0.98 - 1.05)
effect.fade_in()

beats(68.5, 82)
color.uniform((0.98, 0.9, 1.0))
effect.fill_out()

beats(83, 107)
elements(all)
color.gradient(indigo[0], aquamarine[0])

cycle(6)
elements([group1, group2])
BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.0, 1)).apply()
elements([group8, group3])
BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.25, 1)).apply()
elements([group6, group7])
BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.5, 1)).apply()
elements([group5, group4])
BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.75, 1)).apply()



elements(all)
beats(83, 87)
effect.fade_in()
beats(103, 107)
effect.fade_out()


beats(78, 83)
elements(bottle4)
color.uniform(light_coral)
effect.breath(medium)

beats(78+4/9, 83)
elements(paper2)
color.uniform(light_coral)
effect.breath(medium)

beats(78+8/9, 83)
elements(sticks7)
color.uniform(light_coral)
effect.breath(medium)

beats(78+12/9, 83)
elements(flower1)
color.uniform(light_coral)
effect.breath(medium)

beats(78+16/9, 83)
elements(brain7)
color.uniform(light_coral)
effect.breath(medium)

beats(78+20/9, 83)
elements(lifas5)
color.uniform(light_coral)
effect.breath(medium)

beats(78+24/9, 83)
elements(donut1)
color.uniform(light_coral)
effect.breath(medium)

beats(78+28/9, 83)
elements(cabbage6)
color.uniform(light_coral)
effect.breath(medium)

beats(78+32/9, 83)
elements(paper2)
color.uniform(light_coral)
effect.breath(medium)

beats(82, 83)
elements(lifas1)
color.uniform(light_coral)
effect.breath(soft)
beats(82.5, 83)
elements(lifas1)
effect.fade_out()


beats(89.5, 94)
elements(sticks3.all)
color.uniform(light_coral)
effect.fill()

beats(91, 94)
elements(sticks8.all)
color.uniform(light_coral)
effect.fill()

beats(92.5, 94)
elements(sticks7.all)
color.uniform(light_coral)
effect.fill()

beats(93.5, 96)
elements(sticks)
color.uniform(light_coral)
effect.fade_out()

beats(96, 98)
elements(sticks)
effect.fade_in()

beats(107.5, 145)
cycle(1.5)
elements(meduza)
color.uniform(indigo)
effect.breath(soft)
effect.random_saturation()

beats(107.5, 110.5)
elements(meduza)
effect.fade_in()

beats(139, 145)
elements(meduza)
effect.fade_out()


beats(107.7, 117)
elements(all)
color.uniform((0.33, 0.8, 1.0))
effect.breath(1.0)
effect.blink_repeat(64, 0.03)

beats(119.5, 128)
elements(all)
color.uniform((0.2, 0.8, 1.0))
effect.breath(1.0)
effect.blink_repeat(64, 0.03)

beats(123.1, 127.45)
elements(lifas1.all)
color.uniform(orange_strip)
effect.saw_tooth(total, False)

beats(124, 127.45)
elements(sticks3.all)
color.uniform(orange_strip)
effect.saw_tooth(total, False)

beats(124.78, 127.45)
elements(lifas4.all)
color.uniform(orange_strip)
effect.saw_tooth(total, False)

beats(125.57, 127.45)
elements(lifas5.all)
color.uniform(orange_strip)
effect.saw_tooth(total, False)

beats(126.3, 127.45)
elements(sticks7.all, sticks8.all)
color.uniform(orange_strip)
effect.saw_tooth(total, False)







beats(132.2, 137.5)
elements(all)
color.uniform((0.1, 0.8, 1.0))
effect.breath(1.0)
effect.blink_repeat(64, 0.03)

beats(138, 145)
elements(all)
color.uniform((0.98, 0.9, 1.0))
effect.breath(1.0)
effect.blink_repeat(64, 0.03)

beats(0, 145)
effect.brightness(0.5)

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
start_song("because", 0)


