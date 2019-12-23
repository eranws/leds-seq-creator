from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.meduza import meduza
from led_objects.cabbages import cabbage1, cabbage6, brain7, cabbage5, cabbages, brains, donut1, donut3, twists, donuts
from led_objects.flood import floods, cup_cakes, cup_cake3, rug4, cup_cake4, rug6
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, strings, flower1, bottles, papers, paper2, bottle4, bottle5
from led_objects.objects_selector import elements
from led_objects.sheep import sheep
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, lifas, single_lifas, \
    stands, single_stands
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=126, beats_per_episode=32, start_offset=3)
# episode 0 start triolas, last 4 beats are different
episodes(0, 1)
elements(twists, donuts, flowers, floods, strings)
cycle(beats=2.5)
color.uniform(indigo)
effect.saw_tooth()
cycle(None)
effect.fade_out()

# Add drum
episodes(1, 3)

# blings sequence
beats(58, 66)
# additional bling in sequence
beats(62+2/3, 64)

# stop triolas for one beat and static noise
beats(70, 71)

# episode 3 (and all after it) needs 0.476 seconds addition
# stretched out bling sequence
beats(88, 100)



send_to_mqtt("nikki")
start_song("nikki", 0)