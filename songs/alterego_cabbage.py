import random

from animations.fill import FillAnimation
from float_func.const import ConstFloatFunc
from float_func.sin import SinFloatFunc
from infra.animations_factory import color, effect

from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.groups import flowers, cabbages

# from led_objects.led_object import all
from led_objects.objects_selector import elements
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import beats_in_episode, song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_offset=60
song_settings(bpm=123, beats_per_episode=32, start_offset=3)

# all.append(cabbages)
# all.append(flowers)
groups = [group1, group2, group3, group4, group5, group6, group7, group8]

all = [cabbages, flowers]

episode(0)
elements(all)

cycle(4)
cycle_beats(2,4)
color.alternate(pink_string,purple_string)
effect.snake()

cycle_beats(0,1);color.uniform(pink_string);effect.blink()
cycle_beats(1,2);color.uniform(magenta);effect.blink()

episode(1)
elements(cabbages)
color.alternate(blue,green)
effect.fill_in_steps(32)

episode(1)
elements(flowers)
color.uniform(green)
effect.fill()


episode(2)
elements(cabbages)

beats_in_episode(2, 0, 24)
color.gradient(red, yellow_string)
cycle(.01)
effect.hue_shift_cycle_target(0.1)

beats_in_episode(2, 24, 32)
color.gradient(red, yellow_string)
cycle(.5)
effect.hue_shift_cycle_target(0.1)


episode(3)
elements(cabbages)
color.uniform(blue)
effect.fill_in_out()

episodes(4,7)
elements(cabbages)

cycle(8)
cycle_beats(0,1)
color.uniform(pink_string)
effect.blink()
cycle_beats(1,2)
color.uniform(pink_string)
effect.blink()

cycle_beats(2,4)
color.uniform(blue)
effect.fill()

send_to_mqtt("alterego")
start_song("alterego", song_offset)