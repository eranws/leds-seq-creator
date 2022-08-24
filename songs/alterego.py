import random

from animations.fill import FillAnimation
from float_func.const import ConstFloatFunc
from float_func.sin import SinFloatFunc
from infra.animations_factory import color, effect

from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.groups import flowers
from led_objects.groups import papers
from led_objects.groups import bottles
from led_objects.groups import strings
from led_objects.groups import cabbages
from led_objects.groups import brains
from led_objects.groups import donuts
from led_objects.groups import cup_cakes
from led_objects.groups import rugs
from led_objects.groups import sticks
from led_objects.groups import lifas
from led_objects.groups import single_stands

from led_objects.led_object import all
from led_objects.objects_selector import elements
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=123, beats_per_episode=32, start_offset=3)

# all.append(meduza)
groups = [group1, group2, group3, group4, group5, group6, group7, group8]

def single_equalizer(phase, max_val):
    FillAnimation(ConstFloatFunc(0.0), SinFloatFunc(0.1, max_val, phase, 1)).apply()

def equalizer(elem):
    for p, s in enumerate(elem.all):
        elements(s)
        single_equalizer(p/len(elem.all),random.uniform(0.6,1))

episodes(0,10)
cycle(32)
cycle_beats(0,16)
elements(all)
color.uniform(red)
effect.fill()

episode(0)
cycle(32)
cycle_beats(0,16)
# elements(all,sheep)
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

episode(1)
cycle(1)
elements(all)
effect.random_brightness()

episode(2)
cycle(0.5)
elements(all)
effect.random_brightness()

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
elements(all)
color.gradient(-0.2,0.2)
effect.hue_saw_tooth(0.6)

episodes(6,9)
cycle(2)
elements(all)
color.gradient(-0.2,0.2)
effect.hue_saw_tooth(1)
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

send_to_mqtt("alterego")
start_song("alterego", 16)


