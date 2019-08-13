from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.flood import cup_cakes, cup_cake3
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
cycle_beats(0,1)
elements(group1)
color.uniform(light_coral)
effect.breath(soft)
cycle_beats(1,2)
elements(group4)
color.uniform(turquoise_strip)
effect.breath(total)


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
episodes (4.125,6)
cycle(8)

def light_one(start_beat, element):
    cycle_beats(start_beat, start_beat + 1)
    elements(element)
    color.uniform(blue)
    if start_beat == 7:
        color.uniform(light_blue)
    effect.saw_tooth(edge=soft)

light_one(0, cabbage1)
light_one(1, cabbage5)
light_one(2, brain7)
light_one(3, cup_cake3)
light_one(4, donut3)
light_one(5, cup_cake4)
light_one(6, paper2)
light_one(7, flower1)

elements(all)

for i in range(1, 16):
    episodes(4 + i / 8.0, 4 + (i+1) / 8.0)
    effect.hue_shift(i / 6.0)

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
color.alternate(blue,light_pink_strip,40)
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

beats(500,540)
elements(sticks)
cycle(1.5)
color.gradient(0.46,0.55)
effect.snake_down_up(1.0)

beats(540,552)
elements(cup_cake3)
cycle(1)
color.uniform(red)
effect.hue_saw_tooth()
#episodes (8,10)
beats(552,560)
elements(flower6)
color.uniform(blue)
effect.saw_tooth(total)

beats(560,568)
elements(flower6,cabbage6, brain7)
color.uniform(blue)
effect.saw_tooth(total)

beats(568,576)
elements(flower6,cabbage6,sticks7,sticks8,brain7)
color.uniform(blue)
effect.saw_tooth(total)

beats(576,584)
elements(flower6,cabbage6,sticks7,sticks8,brain7,donut1,cabbage1,cabbage5)
color.uniform(blue)
effect.saw_tooth(total)

beats(584,592)
elements(flower6,cabbage6,sticks7,sticks8,brain7,donut1,cabbage1,cabbage5,flower1,bottle5)
color.uniform(blue)
effect.saw_tooth(total)

beats(592,600)
elements(flower6,cabbage6,sticks7,sticks8,brain7,donut1,cabbage1,cabbage5,flower1,bottle5,lifas1,lifas5,paper5)
color.uniform(blue)
effect.saw_tooth(total)

beats(600,608)
elements(flower6,cabbage6,sticks7,sticks8,brain7,donut1,cabbage1,cabbage5,flower1,bottle5,lifas1,lifas5,paper5,paper2,bottle4)
color.uniform(blue)
effect.saw_tooth(total)

beats(608,616)
elements(all)
color.uniform(blue)
effect.saw_tooth(total)

beats(576,584)
elements(all)
color.uniform(blue)
effect.saw_tooth(total)

#drums /conffeti
beats(672,673)
elements(cabbages)
cycle(1/3)
color.uniform(light_pink_strip)
effect.breath(soft)

#siren
beats(750,768)
cycle(1)
elements(single_sticks,single_stands)
color.alternate(red,orange_strip,10)
effect.snake_up_down()
beats(768,780)
cycle(1)
elements(single_sticks,single_stands)
color.alternate(red,orange_strip,10)
effect.snake()
beats(782,800)
cycle(1)
elements(single_sticks,single_stands)
color.alternate(red,orange_strip,10)
effect.snake_up_down()
beats(800,810)
cycle(1)
elements(single_sticks,single_stands)
color.alternate(red,orange_strip,10)
effect.breath(medium)
#
send_to_mqtt("millenium")
start_song("millenium",210)

#shift+fn f10-