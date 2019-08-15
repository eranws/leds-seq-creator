from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.flood import cup_cakes, cup_cake3, rug6, rugs
from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles, flower1, paper2, bottle5, bottle4
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands, \
    single_stands
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=124, beats_per_episode=64)


#main_beat
episodes(0, 1)
cycle(2)
#cycle_beats(0,1)
elements(group1)
color.uniform(light_coral)
effect.blink(medium)
#cycle_beats(1,2)
elements(group4)
color.uniform(turquoise_strip)
effect.blink(medium, True)


#siren
episodes (0+8/64, 1)
cycle(16)
cycle_beats(0,4)
elements(sticks)
color.gradient(0.0,0.11)
effect.breath(medium)

#main_beat
episodes(1, 3)
cycle(2)
cycle_beats(0,1)
elements(paper2,cup_cake3,bottles,donuts)
color.uniform(light_blue)
cycle_beats(1,2)
elements(paper5,flowers,cup_cake4,)
color.uniform(indigo)
effect.random_saturation()

#drums
episodes(2, 3)
elements(cabbages)
cycle(1/3)
color.uniform(light_pink_strip)
effect.breath(soft)

#siren
episodes(1, 3)
elements(single_sticks,single_stands)
cycle(32)
cycle_beats(0,6)
color.alternate(red,orange_strip,10)
effect.snake_up_down()
cycle_beats(16,20)
color.alternate(red,orange_strip,10)
effect.snake()


# episode3-4
#drama
wanted_elements = [group1, group2, group3, group4, group5, group6, group7, group8]
current_elements = []
current_beat = 192
for element in wanted_elements:
    current_elements.append(element)
    beats(current_beat, current_beat + 8)
    cycle(1/2)
    elements(current_elements)
    color.uniform(indigo)
    effect.saw_tooth(soft)
    current_beat += 8

color.uniform(red)
effect.saw_tooth(total)

#slow_effect
beats(256,257)
elements(single_stands)
color.uniform(red)
effect.snake(1,switch_direction=True)

beats(256,262)
elements(cup_cake4,cup_cake4,cabbages,paper2)
color.uniform(yellow_string)
effect.snake(1,switch_direction=True)


#main_beat
episodes (4.125,4.5)

def light_one(start_beat, element, c):
    cycle_beats(start_beat, start_beat + 1)
    elements(element)
    color.uniform(c)
    effect.saw_tooth(edge=soft)

cycle(8)
light_one(0, cabbage1, blue)
light_one(1, cabbage5, green)
light_one(2, brain7, yellow_string)
light_one(3, cup_cake3, blue)
light_one(4, donut3, blue)
light_one(5, cup_cake4, blue)
light_one(6, paper2, blue)
light_one(7, flower1, blue)

elements(all)

for i in range(1, 16):
    episodes(4 + i / 8.0, 4 + (i+1) / 8.0)
    effect.hue_shift(i / 6.0)

episodes (4.5,5)
elements(sticks8)
cycle(1/3)
color.uniform((0.98, 0.45, 1))
effect.blink()
cycle(8)

light_one(0, [cabbage1, flower6,cup_cake4], blue)
light_one(1, [cabbage5,paper5,donut3], blue)
light_one(2, [brain7,flower6,flower1], blue)
light_one(3, [cup_cake3,paper2,bottle5], blue)
light_one(4, [donut3,cabbage1,brain7], blue)
light_one(5, [cup_cake4,bottle4,cabbage5], blue)
light_one(6, [paper2,rug6,flower6], blue)
light_one(7, [flower1,brain7,cup_cake4], blue)

elements(all)

for i in range(1, 16):
    episodes(4.5 + i / 8.0, 4 + (i+1) / 8.0)
    effect.hue_shift(i / 6.0)

episodes (5,5.5)
elements(sticks8)
cycle(1/3)
color.uniform(light_pink_strip)
effect.blink()
cycle(8)

light_one(0, [cabbage1, flower6,cup_cake4,bottle4], blue)
light_one(1, [cabbage5,paper5,donut3,rug6], blue)
light_one(2, [brain7,flower6,flower1,paper5], blue)
light_one(3, [cup_cake3,paper2,bottle5, cabbage1], blue)
light_one(4, [donut3,cabbage1,brain7,paper2], blue)
light_one(5, [cup_cake4,bottle4,cabbage5,cabbage1], blue)
light_one(6, [paper2,rug6,flower6,bottle5], blue)
light_one(7, [flower1,brain7,cup_cake4,cabbage5], blue)

elements(all)

for i in range(1, 16):
    episodes(5 + i / 8.0, 4 + (i+1) / 8.0)
    effect.hue_shift(i / 6.0)

episodes (5.5,6)
elements(sticks8)
cycle(1/3)
color.uniform(light_pink_strip)
effect.blink()
cycle(8)

light_one(0, [group1,group4], blue)
light_one(1, [group6,group7,group8], blue)
light_one(2, [group2,group3], blue)
light_one(3, [group5,group7], blue)
light_one(4, [group1,group3], blue)
light_one(5, [group5,group2], blue)
light_one(6, [group1,group3], blue)
light_one(7, [group5,group8,group2], blue)

elements(all)

for i in range(1, 16):
    episodes(5.5 + i / 8.0, 4 + (i+1) / 8.0)
    effect.hue_shift(i / 6.0)

#drama


beats(384,385)
elements(single_stands)
color.uniform(red)
effect.snake(0.5,switch_direction=True)

#main_beat
episode(6)
cycle(8)
elements(paper2,cup_cakes,flowers,paper5)
color.uniform(turquoise_string)
effect.breath(total)

beats(424,440)
cycle(1)
elements(cabbages)
color.uniform(orange_strip)
effect.snake()

#drama
beats(440,448)
cycle(1)
elements(all)
color.uniform(light_pink_strip)
effect.blink(medium)

beats(448,456)
cycle(1)
elements(group1)
color.uniform(light_purple_string)
effect.saw_tooth()

beats(456,457)
cycle(1)
elements(group1)
color.uniform([0.7, 1.0, 1.0])
effect.snake()

beats(456,464)
cycle(1)
elements(group2,group3)
color.uniform([0.7, 1.0, 1.0])
effect.blink(soft)

beats(464,465)
cycle(1)
elements(group2,group3)
color.uniform(turquoise_string)
effect.snake()

beats(464,472)
cycle(1)
elements(bottle4,group5)
color.uniform(turquoise_string)
effect.blink(soft)

beats(472,473)
cycle(1)
elements(bottle4,group5)
color.uniform(indigo)
effect.snake()

beats(472,480)
cycle(1)
elements(group6,group7,group8)
color.uniform(indigo)
effect.blink(total)

beats(479,480)
cycle(1)
elements(all)
color.uniform(light_pink_strip)
effect.snake()


episode(7)
beats(480,490)
elements(sticks8)
cycle(1.5)
color.gradient(0.46,0.55)
effect.snake_down_up(1.0)

beats(490,500)
elements(sticks8,sticks7)
cycle(1.5)
color.gradient(0.46,0.55)
effect.snake_down_up(1.0)

beats(500,544)
elements(sticks)
cycle(1.5)
color.gradient(0.46,0.55)
effect.snake_down_up(1.0)

# beats(544,734)734
beats(536,552)
cycle(2/3)
elements(group1,group2,cup_cakes,donut3,group4,group5,group6,cabbages,brains)
color.uniform(red)
effect.breath(hard)
cycle(16)
effect.saw_tooth(total, True)
# *****************************************************************************
# beats(552,564)
# cycle(4)
# cycle_beats(0,2)
# elements(group1,group2,group3,group8,flower6)
# color.alternate(light_green,green,10)
# effect.blink_repeat(6)
# cycle_beats(2,4)
# elements(group4,group5,group7,rug6,cabbage6)
# color.alternate(light_pink_strip,orange_strip,10)
# effect.blink_repeat(6)

beats(552,564)
elements(all)
color.gradient(magenta[0],orange_strip[0])
effect.blink_repeat(6)

beats(564,576)

cycle(2)
cycle_beats(0,1)
elements(group1,group2,group3,group8,flower6)
color.alternate(magenta,orange_strip,10)
effect.blink_repeat(3)
cycle_beats(1,2)
elements(group4,group5,group7,rug6,cabbage6)
color.alternate(light_pink_strip,orange_strip,10)
effect.blink_repeat(3)


cycle(24)
effect.saw_tooth(total, True)

beats(576,592)
cycle(4)
cycle_beats(0,2)
elements(group1,group2,group3,group8,flower6)
color.alternate(yellow_string,coral,10)
effect.blink_repeat(6)
cycle_beats(2,4)
elements(group4,group5,group7,rug6,cabbage6)
color.alternate(purple_string,light_purple_string,10)
effect.blink_repeat(6)

beats(592,608)

cycle(2)
cycle_beats(0,1)
elements(group1,group2,group3,group8,flower6)
color.alternate(yellow_string,coral,10)
effect.blink_repeat(3)
cycle_beats(1,2)
elements(group4,group5,group7,rug6,cabbage6)
color.alternate(purple_string,light_purple_string,10)
effect.blink_repeat(3)

beats(608,624)
cycle(4)
cycle_beats(0,2)
elements(group1,group2,group3,group8,flower6)
color.alternate(indigo,turquoise_string,10)
effect.blink_repeat(6)
cycle_beats(2,4)
elements(group4,group5,group7,rug6,cabbage6)
color.alternate(light_aquamarine,green,10)
effect.blink_repeat(6)

beats(624,640)

cycle(2)
cycle_beats(0,1)
elements(group1,group2,group3,group8,flower6)
color.alternate(indigo,turquoise_string,10)
effect.blink_repeat(3)
cycle_beats(1,2)
elements(group4,group5,group7,rug6,cabbage6)
color.alternate(light_aquamarine,green,10)
effect.blink_repeat(3)

beats(640,656)

cycle(2)
cycle_beats(0,1)
elements(group1,group2,group3,group8,flower6)
color.alternate(light_green,green,10)
effect.blink_repeat(3)
cycle_beats(1,2)
elements(group4,group5,group7,rug6,cabbage6)
color.alternate(light_pink_strip,orange_strip,10)
effect.blink_repeat(3)

cycle(24)
effect.saw_tooth(total, True)

beats(656,671)
cycle(4)
cycle_beats(0,2)
elements(group1,group2,group3,group8,flower6)
color.alternate(yellow_string,coral,10)
effect.blink_repeat(6)
cycle_beats(2,4)
elements(group4,group5,group7,rug6,cabbage6)
color.alternate(purple_string,light_purple_string,10)
effect.blink_repeat(6)
#*********************************************************************

beats(672,673)
elements(stands,cabbages)
color.uniform(light_pink_strip)
effect.saw_tooth()
#*********************************************************************

def light_8_beats(beats_start, e):
    beats(beats_start, beats_start + 8)
    cycle(1)
    elements(e)


light_8_beats(672, all)
color.uniform(blue)
effect.snake()

light_8_beats(680, [group1,group3,group7])
color.uniform(blue)
effect.snake()

episodes (10.625,10.75)
cycle(1)
elements()
color.uniform(red)
effect.snake()

episodes (10.75,10.875)
cycle(1)
elements(group2,group5,group3)
color.uniform(purple_string)
effect.snake()

episodes (11.25,11.5)
cycle(1)
elements(cup_cakes,lifas,bottles,donuts,brains)
color.gradient(0,1)
effect.snake()


# episodes(10.75,11.5)
# elements(sticks8)
# cycle(8)
# color.uniform((0.98, 0.45, 1))
# effect.blink()
# cycle(8)
# def light_one(start_beat, element):
#     cycle_beats(start_beat, start_beat + 1)
#     elements(element)
#     color.gradient(1,0)
#     effect.snake()
#
# light_one(0, [cabbage1, flower6,cup_cake4,bottle4])
# light_one(1, [cabbage5,paper5,donut3,rug6])
# light_one(2, [brain7,flower6,flower1,paper5])
# light_one(3, [cup_cake3,paper2,bottle5,cabbage1])
# light_one(4, [donut3,cabbage1,brain7,paper2])
# light_one(5, [cup_cake4,bottle4,cabbage5,cabbage1])
# light_one(6, [paper2,rug6,flower6,bottle5])
# light_one(7, [flower1,brain7,cup_cake4,cabbage5])


#drums


beats (736,808)
cycle(32)
cycle_beats(0,12)
elements(paper2,flowers,paper5)
color.uniform(turquoise_string)
effect.breath(total)
cycle_beats(12,32)
elements(paper2,flowers, paper5)
color.uniform(pink_string)
effect.breath(total)

beats(736,828)
elements(cup_cake3)
cycle(2)
cycle_beats(0,1/3)
color.uniform(light_coral)
effect.breath()
cycle_beats(1/3,2/3)
color.uniform(light_coral)
effect.breath()
cycle_beats(2/3,1)
color.uniform(light_coral)
effect.breath()
cycle_beats(1,1+1/3)
color.uniform(coral)
effect.breath()
cycle_beats(1+1/3,1+2/3)
color.uniform(light_coral)
effect.breath()
cycle_beats(1+2/3,2)
color.uniform(light_coral)
effect.breath()
effect.saw_tooth(60)

send_to_mqtt("millenium")
start_song("millenium",320)

#shift+fn f10-