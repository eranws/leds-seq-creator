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

song_settings(bpm=128, beats_per_episode=32)

elements(all)

beats(0, 2)
color.uniform((0.0, 0.9, 1.0))

beats(2, 18)
color.gradient(0.0, 2.0)

cycle(8)
elements(single_stands)
cycle_beats(0, 4)
effect.snake(1.0, True)
cycle_beats(4, 8)
effect.snake(1.0, False)


elements(all)

beats(18, 52)
color.uniform((0.7, 0.9, 1.0))

beats(52, 80)
color.uniform((0.2, 0.9, 1.0))

beats(80, 112)
color.uniform((0.9, 0.9, 1.0))

beats(112, 116)
color.uniform((0.6, 0.9, 1.0))

beats(116, 182)
color.uniform((0.1, 0.9, 1.0))

beats(182, 216)
color.uniform((0.8, 0.9, 1.0))

beats(216, 244)
color.uniform((0.2, 0.9, 1.0))

beats(244, 280)
color.uniform((0.7, 0.9, 1.0))

beats(280, 348)
color.uniform((0.0, 0.9, 1.0))




send_to_mqtt("under")
start_song("under", 0)


