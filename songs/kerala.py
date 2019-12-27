import random

from animations import brightness
from animations.brightness import BrightnessAnimation
from animations.hue_shift import hue_shift_jump_on_cycle
from float_func.linear import LinearFloatFunc
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.common import no_stands
from led_objects.flood import cup_cakes, rugs, cup_cake3, rug6, rug4
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles, paper2, flower1, strings, gloves, gloves8, \
    bottle4, bottle5
from led_objects.meduza import meduza
from led_objects.objects_selector import elements, elements_random
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands, \
    single_lifas, single_stands, single_stands_per_stand
from led_objects.stars import stars, star7
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=125, beats_per_episode=32, start_offset=0.025)

# functions

def meitar(elem, col):
    elements(elem)
    color.uniform(col)

    cycle(4)
    cycle_beats(0, 2)
    elements_random(elem)
    effect.fill()
    cycle_beats(2, 4)
    elements(elem)
    effect.fill_out()



episodes(0, 10)
meitar([stars.all, meduza], aquamarine)

episodes(9/16, 10)
meitar([papers, cup_cakes, sticks], purple_strip)

episodes(1, 10)
elements(bottles, donuts)
color.uniform(coral)

cycle(4)
effect.breath()




send_to_mqtt("kerala")
start_song("kerala", 0)


