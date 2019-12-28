import random

from animations import brightness
from animations.brightness import BrightnessAnimation
from animations.fill import FillAnimation
from animations.hue_shift import hue_shift_jump_on_cycle
from float_func.const import ConstFloatFunc
from float_func.linear import LinearFloatFunc
from float_func.sin import SinFloatFunc
from float_func.steps import StepsFloatFunc
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.common import no_stands
from led_objects.flood import cup_cakes, rugs, cup_cake3, rug6, rug4
from led_objects.groups import group1, group2, group3, group8, group6, group7, group4, group5
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles, paper2, flower1, strings, gloves, gloves8, \
    bottle4, bottle5
from led_objects.meduza import meduza
from led_objects.objects_selector import elements, elements_random
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands, \
    single_lifas, single_stands, single_stands_per_stand
from led_objects.stars import stars, star7, single_stars
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=125, beats_per_episode=32, start_offset=0.025)

# functions

def var_col(col):
    if len(col) == 3:
        color.uniform(col)
    else:
        color.gradient(col[0], col[1])

def meitar(elem_f, elem_o, col):
    elements(elem_f)
    if len(col) == 2:
        color.gradient(col[0], col[1])
    else:
        color.uniform(col)

    cycle(4)
    cycle_beats(0, 2)
    elements_random(elem_f)
    effect.fill()
    cycle_beats(2, 4)
    elements(elem_o)
    effect.fill_out(reverse=True)

def hue_beat(strength):
    cycle(4)
    cycle_beats(0, .5)
    effect.hue_breath(edge=strength)
    cycle_beats(.5, 1)
    effect.hue_breath(edge=strength)
    cycle_beats(2, 2.5)
    effect.hue_breath(edge=strength)
    cycle_beats(2.5, 3)
    effect.hue_breath(edge=strength)

def single_equalizer(phase, max_val):
    FillAnimation(ConstFloatFunc(0.0), SinFloatFunc(0.1, max_val, phase, 1)).apply()

def equalizer(elem):
    for p, s in enumerate(elem.all):
        elements(s)
        single_equalizer(p/len(elem.all),random.uniform(0.6,1))

def yeah_fill():
    cycle(4)
    cycle_beats(0, 3)
    FillAnimation(ConstFloatFunc(0.0), StepsFloatFunc(6, 1 / 6, 1 / 6)).apply()
    cycle_beats(3, 3.5)
    effect.fill_out(reverse=True)
    cycle_beats(3.5, 4)
    effect.brightness(val=0)

def yeah_round(elem, col):
    cycle(4)
    for b in range(5):
        cycle_beats(b*3/5, (b+1)*3/5)
        elements(elem.stand(b+1))
        var_col(col)
        effect.blink_repeat(2)

    cycle_beats(3, 3.5)
    elements(elem.all)
    var_col(col)
    effect.fill_out(reverse=True)
    cycle_beats(3.5, 4)
    effect.brightness(val=0)


# underlying fill
episodes(0.25, 1)
elements(all)
color.uniform(indigo)
cycle(24)
effect.fill()

episodes(1, 3)
elements(all)
color.uniform(indigo)
cycle(32)
effect.fade_out()



# first episodes
episodes(0, 4)
meitar(stars, single_stars, [.05, 0])

episodes(0.5, 3)
meitar(sticks, single_sticks, [.05, 0])
episodes(0.5, 3)
meitar(lifas, single_lifas,  [.05, 0])


episodes(1, 3)
elements(strings, gloves, cup_cakes)
hue_beat(0.1)

episodes(1, 3)
elements(cabbages, brains, single_stars, single_lifas, single_sticks)
color.gradient(.05, 0)
cycle(4)
effect.fill()

beats(48, 50)
elements(sticks3)
color.gradient(0.4, 0.7)
cycle(2)
equalizer(sticks3)

episodes(2, 3)
elements(cabbages, brains, donuts, papers, flowers)
color.uniform(aquamarine)
cycle(4)
effect.fill_in_out()

beats(80, 82)
elements_random(lifas1)
color.gradient(0.9, 1)
cycle(2)
equalizer(lifas1)

episodes(3, 4)

elements_random(list(set(all)-set(stars)))
cycle(1)
color.uniform(turquoise_string)
effect.hue_shift_cycle_target(0, red[0]-turquoise_string[0])
cycle(8)
elements([group1, group2])
BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.0, 1)).apply()
elements([group8, group3])
BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.25, 1)).apply()
elements([group6, group7])
BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.5, 1)).apply()
elements([group5, group4])
BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.75, 1)).apply()

elements(meduza)
meitar(meduza, meduza, [0, 0.05])
elements(stars, meduza)
hue_beat(0.1)

episodes(4, 5)

elements_random(all)
cycle(1)
color.uniform(red)
effect.hue_shift_cycle_target(0, turquoise_string[0]-red[0])
cycle(8)
elements([group1, group2])
BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.0, 1)).apply()
elements([group8, group3])
BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.25, 1)).apply()
elements([group6, group7])
BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.5, 1)).apply()
elements([group5, group4])
BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.75, 1)).apply()

episodes(5, 6)
elements(all)
color.gradient(0.4, .6)
cycle(8)
effect.saw_tooth()
effect.hue_breath(edge=.3)

episodes(6, 7)
elements_random(stars)
color.gradient(0.9, 1)
cycle(2)
effect.fill_in_out()

for n, e in enumerate(sticks + lifas):
    episodes(6.125+n*.125, 7)
    cycle(2)
    elements(e)
    c = random.uniform(0, 1)
    color.gradient(c, c + 0.2)
    equalizer(e)

beats(6*32, 6*32+2)
elements_random(all)
color.uniform(white)
cycle(2)
effect.fill_in_out()

for n, elem in enumerate([sticks3, lifas1, sticks8, lifas5, sticks7, lifas4]):
    episodes(7+n/8, 8+n/8)
    elements(elem.all)
    c = random.uniform(0.6,1)
    c=.9
    color.gradient(c, c+.2)
    yeah_fill()

for n, elem in enumerate([sticks3, lifas1, sticks8, lifas5, sticks7]):
    episodes(8 + n / 8, 10)
    yeah_round(elem, [.3,.8])

n = 5
elem = lifas4
col = [.3, .8]
episodes(8 + n / 8, 10)
cycle(4)
for b in range(4):
    cycle_beats(b * 3 / 5, (b + 1) * 3 / 5)
    elements(elem.stand(b + 1))
    var_col(col)
    effect.blink_repeat(2)

cycle_beats(3, 3.5)
elements(elem.all)
var_col(col)
effect.fill_out(reverse=True)
cycle_beats(3.5, 4)
effect.brightness(val=0)

episodes(8, 9)
yeah_round(sticks3,[.3,.8])

send_to_mqtt("kerala")
start_song("kerala", 15*0)


