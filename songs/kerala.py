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
from led_objects.sheep import sheep
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands, \
    single_lifas, single_stands, single_stands_per_stand
from led_objects.stars import stars, star7, single_stars
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=125, beats_per_episode=32, start_offset=3)

# functions

tubes = [sticks3, lifas1, sticks8, lifas5, sticks7, lifas4]
non_tubes = list(set(all)-set(tubes))


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


def fast_string(elem, col):
    elements(elem)
    var_col(col)
    cycle(1.5)
    equalizer(elem)



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
    cycle_beats(0, 2.5)
    FillAnimation(ConstFloatFunc(0.0), StepsFloatFunc(6, 1 / 6, 1 / 6)).apply()
    cycle_beats(2.5, 3.5)
    effect.fill_out(reverse=True)
    cycle_beats(3.5, 4)
    effect.brightness(val=0)


def yeah_round(elem, col):
    cycle(4)
    for b in range(5):
        cycle_beats(b*2.5/5, (b+1)*2.5/5)
        elements(elem.stand(b+1))
        var_col(col)
        effect.blink_repeat(2)

    cycle_beats(2.5, 3.5)
    elements(elem.all)
    var_col(col)
    effect.fill_out(reverse=True)
    cycle_beats(3.5, 4)
    effect.brightness(val=0)


def meduza_shake():
    elements(meduza)
    color.gradient(col7[1], col7[1])
    cycle(4)
    cycle_beats(0, 3)
    effect.brightness(0)
    cycle_beats(3, 3.25)
    effect.fill()
    cycle_beats(3.25, 4)
    effect.hue_breath(col7[0]-col7[1])


def wave():
    elements([group1, group2])
    BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.0, 1)).apply()
    elements([group8, group3])
    BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.25, 1)).apply()
    elements([group6, group7])
    BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.5, 1)).apply()
    elements([group5, group4])
    BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.75, 1)).apply()


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



episodes(2, 3)
elements(cabbages, brains, donuts, papers, flowers)
color.uniform(aquamarine)
cycle(16)
effect.fill_in_out()

episodes(3, 4)

elements_random(list(set(all)-set(stars)))
cycle(1)
color.uniform(turquoise_string)
effect.hue_shift_cycle_target(0, red[0]-turquoise_string[0])
cycle(8)
wave()

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
wave()

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

for n, e in enumerate(tubes):
    episodes(6.125+n/8, 7+n/8)
    cycle(4)
    elements(e)
    c = random.uniform(0, 1)
    color.gradient(c, c + 0.2)
    equalizer(e)

for n, elem in enumerate(tubes):
    episodes(7+n/8, 8+n/8)
    elements(elem.all)
    color.gradient(.9, 1.1)
    yeah_fill()

for n, elem in enumerate([sticks3, lifas1, sticks8, lifas5, sticks7]):
    episodes(8 + n / 8, 9.5)
    yeah_round(elem, [.3,.8])

# separate for lifas4 with only 4 legs
n = 5
elem = lifas4
col = [.3, .8]
episodes(8 + n / 8, 9.5)
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

col7 = [.4, .7]
h_shift = -.6
episodes(7, 10)
elements_random(non_tubes)
color.gradient(col7[0], col7[1])
cycle(96)
effect.fill()
cycle(8)
effect.breath()
episodes(7, 9)
elements_random(non_tubes)
cycle(.5)
effect.hue_shift_cycle_target(end=h_shift)

episodes(9, 10)
elements(non_tubes)
color.gradient(col7[0]+h_shift, col7[1]+h_shift)
cycle(32)
effect.hue_breath()
cycle(4)
effect.saw_tooth()


for elem in tubes:
    episodes(9.5, 11)
    elements(elem.all)
    var_col(col7)
    yeah_fill()

beats(32*10, 32*10+4)
meduza_shake()

beats(32*10-4, 32*10)
meduza_shake()

episodes(10, 12)
elements(non_tubes)
color.gradient(.9, 1.1)
cycle(64)
cycle_beats(0, 32)
effect.fade_in()
for b in range(0, 64, 4):
    cycle_beats(b, b+4)
    effect.snake(tail=b/128)


for elem in tubes:
    beats(380, 384)
    elements(elem.all)
    var_col(purple_strip)
    yeah_fill()
    beats(348, 352)
    elements(elem.all)
    var_col(purple_strip)
    yeah_fill()

episodes(12, 13)
elements_random(all)
color.gradient(.45, .95)
yeah_fill()

episodes(13, 14)
elements_random(all)
color.gradient(.45, .95)
cycle(4)
wave()
cycle(32)
effect.fill()

episodes(14, 15)
elements(single_stands)
color.uniform(turquoise_string)
effect.fill()

episodes(14, 15.125)
elements(non_tubes)
color.uniform(turquoise_string)
cycle(4)
wave()
cycle(36)
effect.fill_out()
effect.fade_out()

episodes(15-1/8, 15.125)
elements(meduza)
color.gradient(.45, .95)
cycle(16)
effect.blink_repeat(128)
effect.fade_in()

# fast strings
beats(48, 51)
fast_string(sticks3, [0.4, 0.7])

beats(80, 83)
fast_string(lifas5, [0.9, 1])

beats(112, 115)
fast_string(sticks8, [0.3, 0.6])

beats(132, 136)
fast_string(lifas4, [0.1, 0.3])

beats(192, 195)
elements_random(all)
color.uniform(white)
cycle(2)
effect.fill_in_out()

send_to_mqtt("kerala")
start_song("kerala", 15*4)


