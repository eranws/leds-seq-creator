import random

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
    single_stands, single_lifas
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=60, beats_per_episode=60)

episodes(0, 2)
cycle(3)
elements(all)
color.uniform((0.5, 1.0, 1.0))

for elem in all:
    start_beat = -(random.random() * 3.0)
    print(start_beat)
    episodes(start_beat / 60.0, 2.0)
    elements(elem)
    cycle(5)
    #cycle(2.0 + random.random() * 1.0)
    effect.segment_breath(0.05)

    cycle(3.0 + random.random() * 3.0)
    elements(elem)
    effect.breath(total)

cycle(4)
elements(all)
effect.hue_breath(medium)

send_to_mqtt("background")
start_song("background", 0)