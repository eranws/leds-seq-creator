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

beats(0, 8)
cycle(2)
elements(all)
color.uniform(red)
effect.breath(edge=0.5)

beats(0, 8)
cycle(2)
elements(meduza)
color.uniform(indigo)
effect.breath(edge=0.5)

beats(0, 8)
cycle(2)
elements(sheep)
color.uniform((1.0, 0, 1.0))
effect.breath(edge=0.5)

beats(0, 0.5)
effect.fade_in()

send_to_mqtt("game_audio/win2")
start_song("game_audio/win2", 0)


