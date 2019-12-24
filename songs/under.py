import random

from animations import brightness
from animations.brightness import BrightnessAnimation
from animations.hue_shift import hue_shift_jump_on_cycle
from float_func.linear import LinearFloatFunc
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.common import no_stands
from led_objects.flood import cup_cakes, rugs, cup_cake3
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles, paper2, flower1, strings, gloves, gloves8, \
    bottle4, bottle5
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands, \
    single_lifas, single_stands, single_stands_per_stand
from led_objects.stars import stars
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=128, beats_per_episode=32, start_offset=3)

elements(all)

note_to_elem1 = {
    "D": [sticks3.stand(1), sticks7.stand(1), sticks8.stand(1), lifas1.stand(1), lifas4.stand(1), lifas5.stand(1)],
    "Bb": [sticks3.stand(2), sticks7.stand(2), sticks8.stand(2), lifas1.stand(2), lifas4.stand(2), lifas5.stand(2)],
    "F": [sticks3.stand(3), sticks7.stand(3), sticks8.stand(3), lifas1.stand(3), lifas4.stand(3), lifas5.stand(3)],
    "C": [sticks3.stand(4), sticks7.stand(4), sticks8.stand(4), lifas1.stand(4), lifas4.stand(4), lifas5.stand(4)],
    "Eb": [sticks3.stand(5), sticks7.stand(5), sticks8.stand(5), lifas1.stand(5), lifas5.stand(5)],
    "A": [sticks7.stand(6)],
}

note_to_color = {
    "A": (0.0, 1.0, 1.0),
    "C": (0.15, 1.0, 1.0),
    "D": (0.3, 1.0, 1.0),
    "F": (0.5, 1.0, 1.0),
    "Bb": (0.7, 1.0, 1.0),
    "Eb": (0.85, 1.0, 1.0),
}

notes = ["A", "C", "D", "F", "Bb", "Eb"]

beats(2, 20)
#make uniform coloring
for note in notes:
    elements(note_to_elem1[note])
    c = note_to_color[note]
    color.uniform([c[0], 0.9, 0.5])

def play_note(note, t):
    cycle_beats(t, t+0.5)
    elements(note_to_elem1[note])
    effect.brightness(2.0)
    BrightnessAnimation(LinearFloatFunc(1.0, 0.5)).apply()

beats(2, 18)
cycle(8)
play_note("D", 0.0)
play_note("F", 0.25)
play_note("Bb", 0.5)
play_note("Bb", 0.75)
play_note("D", 0.75)
play_note("Bb", 1.25)
play_note("D", 1.25)
play_note("F", 1.75)

play_note("A", 2.0)
play_note("C", 2.0)
play_note("C", 2.5)
play_note("Eb", 2.5)
play_note("Bb", 3.0)
play_note("D", 3.0)
play_note("F", 3.5)
play_note("Bb", 3.5)

play_note("Bb", 4.0)
play_note("D", 4.25)
play_note("F", 4.5)
play_note("F", 4.75)
play_note("Bb", 4.75)
play_note("F", 5.25)
play_note("Bb", 5.25)
play_note("C", 5.75)

play_note("F", 6.0)
play_note("A", 6.0)
play_note("Eb", 6.5)
play_note("C", 6.5)
play_note("Bb", 7.0)
play_note("D", 7.0)

e = [flowers, bottles, cabbages, donuts, brains, rugs, gloves, stars, cup_cakes]
drums_e = papers

# introduce new coloring
beats(17, 20)
elements(e, drums_e)
color.uniform((0.0, 0.0, 0.5))
effect.fade_in()
elements(stands)
effect.fade_out()

# new coloring
beats(20, 80)

posssible_hues = [0.0, 0.2, 0.8, 0.9]

for elem in e:
    elements(elem)
    color.gradient(0.0, 1.0)

beats(20, 52)
elements(e)
cycle(8)
effect.hue_breath(0.3)

def drum(t, length):
    beats(t, t+length)
    color.uniform((0.0, 0.0, 0.7))
    #effect.fade_out()

beats(20, 52)
elements(drums_e)
color.uniform((0.0, 0.0, 0.5))
for t in [34.5, 35, 35.5, 35.75, 39.5, 39.75, 47.5, 49, 50.5, 50.75, 51.5, 51.75]:
    drum(t, 0.1)
for t in [36, 40, 44, 46, 48, 50, 51]:
    drum(t, 0.25)

beats(52, 80)
elements(e)
cycle(1)
effect.saw_tooth(0.3)

beats(78, 80)
elements(stands)
color.uniform((0.0, 0.0, 0.5))
effect.fade_in()
elements(e)
effect.fade_out()

beats(80, 112)
elements(no_stands)
color.gradient(0.0, 1.0)
effect.brightness(0.2)

beats(80, 96)
elements(single_stands)
color.gradient(0.0, 1.0)
elements(no_stands)
cycle(1)
effect.saw_tooth(0.2)

beats(96, 104)
elements(single_stands)
color.gradient(0.0, 1.5)
elements(no_stands)
cycle(0.5)
effect.saw_tooth(0.5)

beats(96, 116)
elements(single_stands)
color.gradient(0.0, 2.0)
elements(no_stands)
cycle(0.25)
effect.saw_tooth(0.5)

beats(80, 112)
elements(single_stands)
cycle(8)
cycle_beats(0, 4)
effect.snake(switch_direction = False)
cycle_beats(4, 8)
effect.snake(switch_direction = True)

beats(112, 116)
elements(stands)
effect.brightness(0.5)
cycle(4)
play_note("D", 0.0)
play_note("F", 0.25)
play_note("Bb", 0.5)
play_note("Bb", 0.75)
play_note("D", 0.75)
play_note("Bb", 1.25)
play_note("D", 1.25)
play_note("F", 1.75)

play_note("A", 2.0)
play_note("C", 2.0)
play_note("C", 2.5)
play_note("Eb", 2.5)
play_note("Bb", 3.0)
play_note("D", 3.0)
play_note("F", 3.5)
play_note("Bb", 3.5)


# energy part!!!!!
dotted = [paper2, paper5, gloves8, flower1, flower6, bottle4, bottle5, cup_cake3]
not_dotted = [donuts, stands, rugs, brains, stars, cabbages]
for elem in dotted:
    elem.random
beats(116, 180)
elements(all)
color.gradient(0.0, 2.0)

beats(116, 124)
cycle(2)
effect.segment_breath(0.5)

beats(124, 132)



send_to_mqtt("under")
start_song("under", 50)


