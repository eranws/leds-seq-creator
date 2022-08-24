import random

from infra.animations_factory import color, effect
from infra.length import total
from led_objects.led_object import all
from led_objects.objects_selector import elements
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, cycle
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
effect.hue_breath("medium")

send_to_mqtt("background")
start_song("background", 0)