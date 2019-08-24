import random

from animations import brightness
from animations.hue_shift import hue_shift_jump_on_cycle
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.flood import cup_cakes, rug4, rugs, cup_cake3, rug6
from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles, paper2, flower1, strings, bottle5, bottle4
from led_objects.meduza import meduza
from led_objects.objects_selector import elements
from led_objects.sheep import sheep
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands, \
    single_lifas, single_stands
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=123, beats_per_episode=32, start_offset=3)

all.append(meduza)
groups = [group1, group2, group3, group4, group5, group6, group7, group8]

def full_wave(cyc,col_grad):
    cycle(cyc)
    steps = 20

    elements(flower1)
    cycle_beats(0, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0],col_grad[1])

    elements(lifas1, cabbage1)
    cycle_beats(1/steps, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0],col_grad[1])

    elements(donut1)
    cycle_beats(2/steps, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0],col_grad[1])

    elements(sticks8, paper2, flower6)
    cycle_beats(3/steps, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0],col_grad[1])

    elements(cup_cake3, cabbage6, rug6)
    cycle_beats(4/steps, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0],col_grad[1])

    elements(sticks3, donut3, brain7)
    cycle_beats(5/steps, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0],col_grad[1])

    elements(sticks7, lifas4, rug4)
    cycle_beats(6/steps, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0],col_grad[1])

    elements(bottle4,cabbage5)
    cycle_beats(7 / steps, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0], col_grad[1])

    elements(paper5)
    cycle_beats(8/steps, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0],col_grad[1])

    elements(cabbage6, bottle5)
    cycle_beats(9/steps, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0],col_grad[1])

    elements(paper5, lifas5, bottle5)
    cycle_beats(10/steps, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0],col_grad[1])

    elements(cabbage6, bottle5)
    cycle_beats(11/steps, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0],col_grad[1])

    elements(paper5)
    cycle_beats(12/steps, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0],col_grad[1])

    elements(sticks7, lifas4, rug4)
    cycle_beats(13/steps, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0],col_grad[1])

    elements(sticks3, donut3, brain7)
    cycle_beats(14/steps, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0],col_grad[1])

    elements(cup_cake3, cabbage6, rug6)
    cycle_beats(14/steps, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0],col_grad[1])

    elements(sticks8, paper2, flower6)
    cycle_beats(15/steps, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0],col_grad[1])

    elements(donut1)
    cycle_beats(16/steps, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0],col_grad[1])

    elements(lifas1, cabbage1)
    cycle_beats(17/steps, cyc)
    effect.breath(0.1)
    color.gradient(col_grad[0],col_grad[1])

episode(0)
cycle(32)
cycle_beats(0,16)
elements(all)
color.uniform(aquamarine)
effect.fill()
cycle_beats(16,32)
elements(all)
color.uniform(aquamarine)
effect.hue_saw_tooth(red[0]-aquamarine[0])
cycle_beats(31,32)
elements(all)
color.uniform(red)
effect.saw_tooth()

episodes(1,3)
cycle(32)
col = [red,coral,orange_string]
for b in range(0,32,2):
    cycle_beats(b,b+2)
    elements(random.choice(groups),random.choice(groups),random.choice(groups))
    color.uniform(random.choice(col))
    effect.saw_tooth()

meduza.random
cycle(1)
elements(meduza)
color.gradient(0,1)
effect.snake()

episodes(2,3)
cycle(2)
elements(single_stands)
color.uniform(indigo)
effect.snake(3)

episodes(3,5)
cycle(4)
elements(strings,cup_cakes)
color.uniform(red)
effect.snake()
cycle(2)
elements(papers,rugs)
color.uniform(purple_strip)
effect.saw_tooth()
cycle(1)
elements(meduza)
color.uniform(red)
effect.breath()

beats(32*3+2,32*5+2)
cycle(4)
elements(cabbages,brains,sticks,lifas)
color.uniform(orange_string)
effect.snake()

episode(4)
cycle(32)
elements(all)
effect.fill_out()

episode(5)
cycle(2)
elements(all,sheep)
color.gradient(-0.2,0.2)
effect.hue_saw_tooth(0.6)

episodes(6,9)
cycle(2)
elements(all)
color.gradient(-0.2,0.2)
effect.hue_saw_tooth(0.1)
cycle(64)
elements(all)
effect.fade_out()
cycle(4)
elements(strings,cup_cakes)
effect.snake()

beats(32*6+2,32*9+2)
cycle(4)
elements(cabbages,brains,sticks,lifas)
effect.snake()

for e in all:
    e.random
episodes(6.5,9)
cycle(0.5)
elements(bottles)
color.gradient(coral[0],red[0])
effect.snake()

episodes(6.75,9)
cycle(0.5)
elements(flowers)
color.gradient(coral[0],red[0])
effect.snake()

episodes(7,9)
cycle(0.5)
elements(papers)
color.gradient(coral[0],red[0])
effect.snake()

episodes(7.25,9)
cycle(0.5)
elements(rugs)
color.gradient(coral[0],red[0])
effect.snake()

episodes(7.5,9)
cycle(0.5)
elements(cup_cakes)
color.gradient(coral[0],red[0])
effect.snake()

episodes(7.75,9)
cycle(0.5)
elements(donuts)
color.gradient(coral[0],red[0])
effect.snake()

episodes(7.75,9)
cycle(0.5)
elements(meduza)
color.gradient(coral[0],red[0])
effect.snake()

episode(8)
cycle(32)
elements(all)
effect.fill_out()
effect.fade_out()

episodes(9,9.5)
cycle(16)
elements(sticks,lifas)
color.uniform(indigo)
effect.fill()

episodes(9.5,12)
cycle(1)
elements(sticks,lifas)
color.uniform(indigo)
effect.snake(0.5)

episodes(9.5,10)
cycle(16)
elements(flowers,cup_cakes,rugs)
color.uniform(purple_strip)
effect.fill()

episodes(10,12)
cycle(1)
elements(flowers,cup_cakes,rugs)
color.uniform(purple_strip)
effect.snake(0.5)

episodes(10,12)
cycle(2)
elements(papers,bottles,donuts)
color.uniform(red)
effect.saw_tooth()

for e in all:
    e.straight
episodes(11,12)
cycle(4)
elements(cabbages,brains,donuts,meduza)
color.uniform(blue)
effect.fill_in_out()

episode(12)
cycle(8)
elements(all)
color.uniform(red)
effect.breath()

episodes(12.5,14)
cycle(0.5)
elements(all)
color.uniform(red)
effect.random_brightness()
cycle(4)
elements(all)
effect.hue_shift_steps(6,0.1)

episodes(14,17)
for e in all:
    e.random
full_wave(4, [0,0.07])

episodes(15,17)
cycle(8)
elements(all)
effect.hue_shift_steps(6,0.2)

send_to_mqtt("alterego")
start_song("alterego",  15.6*14)


