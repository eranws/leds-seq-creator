import random

from animations import brightness
from animations.brightness import BrightnessAnimation
from animations.fill import FillAnimation
from animations.hue_shift import hue_shift_jump_on_cycle
from float_func.const import ConstFloatFunc
from float_func.linear import LinearFloatFunc
from float_func.sin import SinFloatFunc
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.common import no_stands
from led_objects.flood import cup_cakes, rug4, rugs, cup_cake3, rug6, floods
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

def single_equalizer(phase, max_val):
    FillAnimation(ConstFloatFunc(0.0), SinFloatFunc(0.1, max_val, phase, 1)).apply()

def equalizer(elem):
    for p, s in enumerate(elem.all):
        elements(s)
        single_equalizer(p/len(elem.all),random.uniform(0.6,1))


episode(0)
cycle(32)
cycle_beats(0,16)
elements(all,sheep)
color.uniform(aquamarine)
effect.fill()
cycle_beats(16,32)
elements(all,sheep)
color.uniform(aquamarine)
effect.hue_saw_tooth(red[0]-aquamarine[0])
cycle_beats(31,32)
elements(all,sheep)
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

episode(1)
cycle(1)
elements(all)
effect.random_brightness()

episode(2)
cycle(0.5)
elements(all)
effect.random_brightness()

meduza.random

episodes(2,3)
cycle(2)
elements(single_stands)
color.uniform(indigo)
effect.snake(3)

episodes(3,5)
cycle(4)
elements(strings,cup_cakes,donuts)
color.uniform(red)
effect.snake()
cycle(1)
elements(papers)
color.uniform(purple_strip)
effect.saw_tooth()

beats(32*3+2,32*5+2)
cycle(4)
elements(cabbages,brains,sticks,lifas)
color.uniform(orange_string)
effect.snake()

episode(4)
cycle(32)
elements(all)
effect.fill_out()

cycle(4)
cycle_beats(0,1)
elements(rugs)
color.uniform(purple_strip)
effect.blink_repeat(1)
cycle_beats(2,4)
elements(rugs)
color.uniform(purple_strip)
effect.blink_repeat(2)

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
color.uniform(purple_strip)
effect.fill()

episodes(9.5,12)
cycle(1)
elements(sticks,lifas)
color.uniform(purple_strip)
effect.snake(0.5)

episodes(9.375,10)
cycle(20)
elements(flowers,cup_cakes,rugs,bottles)
color.uniform(indigo)
effect.fill()

episodes(10,12)
cycle(1)
elements(flowers,cup_cakes,rugs,bottles)
color.uniform(indigo)
effect.snake(0.5)

episodes(9.875,12)
cycle(2)
elements(papers,donuts)
color.uniform(coral)
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

episodes(14,16)
for e in all:
    e.random
cycle(6)
color.gradient(0.4,0.57)
elements([group1, group2])
BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.0, 1)).apply()
elements([group8, group3])
BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.25, 1)).apply()
elements([group6, group7])
BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.5, 1)).apply()
elements([group5, group4])
BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.75, 1)).apply()

episodes(14,16)
cycle(2)
elements(donuts,meduza)
color.uniform(coral)
effect.saw_tooth()

episodes(15,16)
cycle(8)
elements(all)
effect.hue_breath(0.4)

episodes(16,17)
cycle(2)
for e in lifas+sticks:
    e.straight
    elements(e.all)
    c = random.uniform(0, 1)
    color.gradient(c, c+0.2)
    equalizer(e)
cycle(32)
cycle_beats(16,32)
elements(cup_cakes,donuts, lifas, sticks, rugs,strings,meduza)
effect.hue_saw_tooth(1)

episodes(17,18)
cycle(0.5)
for e in lifas+sticks:
    elements(e.all)
    c = random.uniform(0, 1)
    color.gradient(c, c+0.2)
    equalizer(e)
cycle(32)
cycle_beats(16,32)
elements(cup_cakes,donuts, lifas, sticks, rugs,strings,meduza)
effect.hue_saw_tooth(1)

episodes(16,18)
cycle(2)
cycle_beats(0, 0.5)
elements(cup_cakes,donuts, rugs,strings)
color.gradient(coral[0]-0.1,coral[0])
cycle_beats(1,1.5)
elements(cup_cakes,donuts, rugs,strings)
color.gradient(coral[0]-0.1,coral[0])
effect.breath()
cycle_beats(1.5,2)
elements(cup_cakes,donuts, rugs,strings)
color.gradient(coral[0]-0.1,coral[0])
effect.saw_tooth()

episodes(17,18)
cycle(2)
cycle_beats(1,1.5)
elements(meduza)
color.gradient(coral[0]-0.1,coral[0])
effect.breath()
cycle_beats(1.5,2)
elements(meduza)
color.gradient(coral[0]-0.1,coral[0])
effect.saw_tooth()

episodes(17.5,18)
cycle(16)
elements(cup_cakes,donuts, rugs,strings)
effect.fill_out()

episodes(17.75,18)
cycle(8)
elements(cup_cakes,donuts, rugs,strings)
effect.fade_out()

episodes(17,19)
cycle(0.5)
for e in lifas+sticks:
    e.straight
    elements(e.all)
    c = random.uniform(0, 1)
    color.gradient(c, c+0.2)
    equalizer(e)

cycle(8)
elements(brains, cabbages, cup_cakes, flowers)
color.gradient(aquamarine[0],purple_strip[0])
effect.fill_in_out()

cycle(32)
cycle_beats(16,32)
elements(cup_cakes,donuts, lifas, sticks, rugs,strings,meduza)
effect.hue_saw_tooth(1)

for e in all:
    e.straight
episodes(17.5,18)
cycle(1)
for e in lifas+sticks:
    # e.straight
    elements(e.all)
    c = random.uniform(0, 1)
    color.gradient(c, c+0.2)
    equalizer(e)
    episodes(17.5, 18)
    cycle(1)

episodes(18,19)
cycle(2)
for e in lifas + sticks:
    # e.straight
    elements(e.all)
    c = random.uniform(0, 1)
    color.gradient(c, c + 0.2)
    equalizer(e)

episodes(19,19.5)
cycle(1)
for e in lifas + sticks:
    # e.straight
    elements(e.all)
    c = random.uniform(0, 1)
    color.gradient(c, c + 0.2)
    equalizer(e)

episodes(19.5,20)
cycle(0.5)
for e in lifas + sticks:
    # e.straight
    elements(e.all)
    c = random.uniform(0, 1)
    color.gradient(c, c + 0.2)
    equalizer(e)

episodes(19, 20)
cycle(4)
elements(strings, cup_cakes)
color.gradient(0, 0.07)
effect.snake()
cycle(2)
elements(papers, rugs)
color.uniform(purple_strip)
effect.saw_tooth()
cycle(1)
elements(meduza)
color.gradient(0, 0.07)
effect.breath()

# beats(32*19+2, 32*20+2)
# cycle(2)
# elements(cabbages, brains)
# color.gradient(0.1, 0.7)
# effect.snake()

episodes(18,19)
cycle(32)
elements(brains, cabbages, cup_cakes, flowers)
effect.fill()

episodes(20,21)
cycle(0.25)
for e in lifas + sticks:
    # e.straight
    elements(e.all)
    c = random.uniform(0, 1)
    color.gradient(c, c + 0.2)
    equalizer(e)

# beats(32*20+2, 32*21+2)
# cycle(1)
# elements(cabbages, brains)
# color.gradient(0.1, 0.7)
# effect.breath()

episodes(19.5,21)
elements(all)
effect.blink_repeat(64)

episodes(21,21.125)
elements(all)
color.uniform(red)
effect.saw_tooth()

episode(21)
cycle(32)
cycle_beats(0,2)
elements(cup_cakes,donuts, lifas, sticks, rugs, strings, meduza)
color.uniform(red)
effect.saw_tooth()

episodes(21,24)
cycle(2)
elements(lifas, sticks, meduza)
color.gradient(-0.05,0)
effect.hue_saw_tooth()

cycle(1)
elements(cup_cakes,donuts, bottles, rugs, strings, meduza)
color.gradient(0,0.05)
effect.breath()

episodes(22,23)
cycle(1)
elements(cup_cake3)
color.gradient(0.14,0.8)
effect.blink()

episodes(22.25,23)
cycle(1)
elements(paper5)
color.gradient(0.14,0.8)
effect.blink()

episodes(22.5,23)
cycle(1)
elements(flower1)
color.gradient(0.14,0.8)
effect.blink()

episodes(22.75,25)
cycle(1)
elements(meduza)
color.gradient(0.14,0.8)
effect.blink()

episodes(23, 24)
cycle(4)
elements(donuts, bottles, rugs, strings)
color.gradient(0.14,0.8)
effect.breath()

for e in all:
    e.random
cycle(4)
elements(cabbages,brains,cup_cakes)
color.gradient(magenta[0],turquoise_string[0])
effect.snake()

for e in all:
    e.straight
cycle(32)
elements(lifas, sticks)
effect.fill_out()

episodes(23.25, 25)
cycle(8)
elements(bottles, rugs)
color.uniform(magenta)
effect.breath()

episodes(23.5, 25)
cycle(8)
elements(papers)
color.uniform(turquoise_string)
effect.breath()

episodes(23.5, 25)
cycle(8)
elements(rugs)
color.uniform([(magenta[0]+turquoise_string[0])/2, 0.5, 0.5])
effect.breath()

episodes(23.75, 25)
cycle(8)
elements(flowers)
color.uniform(turquoise_string)
effect.breath()

episode(24)
cycle(32)
elements(all)
effect.fill_out()

episodes(24,28)
cycle(0.5)
elements(meduza)
effect.hue_blink(1/3)

episodes(25,27)
cycle(0.5)
elements(all)
color.uniform(indigo)
effect.random_brightness()
cycle(4)
elements(all)
effect.hue_shift_steps(4,0.25)

episode(25)
cycle(32)
elements(strings,stands)
effect.fill_out()
effect.fade_out()

episodes(26,27)
cycle(32)
elements(floods,twists,donuts)
effect.fill_out()
effect.fade_out()
elements(strings)
color.uniform(black)

c = dict()
for n, e in enumerate(lifas+sticks):
    elements(e.all)
    c[n] = random.uniform(0, 1)
    color.gradient(c[n], c[n]+0.2)
    effect.fill()

episodes(27,28)
cycle(8)
for n, e in enumerate(lifas+sticks):
    elements(e.all)
    color.gradient(c[n], c[n]+0.2)
    equalizer(e)

cycle(32)
cycle_beats(31,32)
elements(all)
effect.fill_out()

send_to_mqtt("alterego")
start_song("alterego", 15.6*0)


