from animations import brightness
from animations.hue_shift import hue_shift_jump_on_cycle
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.flood import cup_cakes
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles, paper2, flower1
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands, \
    single_lifas, single_stands
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=123, beats_per_episode=32)

flower1.random
flower6.random

episodes(0, 5)
elements(flowers)
color.gradient(0.0, 0.1)

episode(0)
cycle(4)

cycle_beats(0, 1)
effect.hue_breath(0.02)

cycle_beats(1.5, 2)
elements(flower1)
effect.breath(0.2, True)

cycle_beats(2.5, 3)
elements(flower6)
effect.breath(0.2, True)


# bring in the beat
beats(29.5, 32)
elements(papers)
color.uniform((0.0, 0.3, 1.0))
cycle(None)
effect.saw_tooth(total, True)


# episode 1

paper2.random
paper5.random
episodes(1, 5)
elements(papers)
color.gradient(0.0, 0.1)

episodes(1, 3)
elements([flowers, papers])

cycle(2)
elements([flower6, paper5])
effect.blink(0.5, False)
elements([flower1, paper2])
effect.blink(0.5, True)

episode(2)
elements(cup_cakes)
color.uniform(light_purple_strip)
cycle(1)
effect.random_brightness()
effect.breath(total)

episodes(0, 30)
elements(lifas4)
cycle(8)
color.gradient(0.0, 1.0)
effect.hue_breath(1.0)

send_to_mqtt("alterego")
start_song("alterego", 0)


