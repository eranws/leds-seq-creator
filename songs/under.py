import random

from led_objects.instances import *
from led_objects.groups import *

from animations.brightness import BrightnessAnimation
from float_func.linear import LinearFloatFunc
from infra.animations_factory import color, effect
from led_objects.led_object import all
from led_objects.objects_selector import elements
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, cycle, cycle_beats, beats
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

note_to_elem2 = {
    "D": [flower1, rug6, brain7],
    "Bb": [donut1, flower6, star7],
    "F": [cabbage1, rug4, bottle5],
    "C": [gloves8, cabbage6],
    "G": [cup_cake3, bottle4],
    "A": [donut3, cup_cake4, cabbage5],
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
    color.uniform([c[0], 0.4, 0.5])

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
elements(drums_e)
color.uniform((0.0, 0.0, 1.0))
effect.fade_in()
elements(stands)
effect.fade_out()

# new coloring
beats(18, 80)
elements(e)
color.uniform((0.0, 0.0, 0.5))

def play_note_elem(note, t):
    cycle_beats(t, t+0.5)
    elements(note_to_elem2[note])
    BrightnessAnimation(LinearFloatFunc(2.0, 1.0)).apply()

beats(18, 34)
cycle(8)
play_note_elem("Bb", 0.5)
play_note_elem("Bb", 0.75)
play_note_elem("Bb", 1.25)
play_note_elem("Bb", 1.5)
play_note_elem("A", 2.0)
play_note_elem("C", 2.5)
play_note_elem("Bb", 3.0)
play_note_elem("F", 3.5)
play_note_elem("D", 4.5)
play_note_elem("F", 4.75)
play_note_elem("F", 5.25)
play_note_elem("D", 5.75)
play_note_elem("C", 6.0)
play_note_elem("F", 6.5)
play_note_elem("D", 7.0)

beats(34, 50)
cycle(8)
play_note_elem("G", 0.5)
play_note_elem("Bb", 0.75)
play_note_elem("Bb", 1.25)
play_note_elem("G", 1.75)
play_note_elem("F", 2.0)
play_note_elem("Bb", 2.5)
play_note_elem("F", 3.0)
play_note_elem("Bb", 3.5)
play_note_elem("A", 4.5)
play_note_elem("C", 4.75)
play_note_elem("C", 5.25)
play_note_elem("Bb", 5.75)
play_note_elem("D", 6.0)
play_note_elem("C", 6.5)
play_note_elem("Bb", 7.0)

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
color.uniform((0.0, 0.0, 0.2))

beats(80, 96)
elements(single_stands)
color.uniform((0.0, 0.0, 1.0))
elements(no_stands)
cycle(1)
effect.saw_tooth(0.2)

beats(96, 104)
elements(single_stands)
color.uniform((0.0, 0.0, 1.0))
elements(no_stands)
cycle(0.5)
effect.saw_tooth(0.5)

beats(96, 116)
elements(single_stands)
color.uniform((0.0, 0.0, 1.0))
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
cycle(2)
effect.hue_breath(0.3)

beats(132, 140)
cycle(2)
effect.segment_saw_tooth()

beats(140, 148)
cycle(2)
effect.fill_out_in(0.7)

beats(148, 156)
cycle(1)
effect.hue_blink()

beats(156, 164)
cycle(2)
effect.snake_down_up()

beats(164, 172)
cycle(2)
effect.blink_repeat(48)

beats(172, 180)
cycle(2)
elements(dotted)
effect.breath(edge=0.4, reverse=True)
elements(not_dotted)
effect.breath(edge=0.4, reverse=False)




############################################################
############################################################
# second part
############################################################
############################################################








beats(182, 244)
elements(e)
color.gradient(0.0, 1.0)

beats(182, 214)
elements(e)
cycle(8)
effect.hue_saw_tooth(0.5)


def drum(t, length):
    beats(t, t+length)
    effect.brightness(2.0)
    #effect.fade_out()

beats(182, 216)
elements(drums_e)
color.uniform((0.0, 0.0, 0.5))
for t in [34.5, 35, 35.5, 35.75, 39.5, 39.75, 47.5, 49, 50.5, 50.75, 51.5, 51.75]:
    drum(160 + t, 0.1)
for t in [36, 40, 44, 46, 48, 50, 51]:
    drum(160 + t, 0.25)

beats(216, 242)
elements(e)
cycle(1)
effect.saw_tooth(0.3)




beats(242, 244)
elements(stands)
color.uniform((0.0, 0.0, 0.5))
effect.fade_in()
elements(e)
effect.fade_out()

beats(244, 276)
elements(no_stands)
color.gradient(0.0, 1.0)
effect.brightness(0.2)

beats(244, 260)
elements(single_stands)
color.gradient(0.0, 1.0)
elements(no_stands)
cycle(1)
effect.saw_tooth(0.2)

beats(260, 268)
elements(single_stands)
color.gradient(0.0, 1.5)
elements(no_stands)
cycle(0.5)
effect.saw_tooth(0.5)

beats(268, 276)
elements(single_stands)
color.gradient(0.0, 2.0)
elements(no_stands)
cycle(0.25)
effect.saw_tooth(0.5)

beats(244, 276)
elements(single_stands)
cycle(8)
cycle_beats(0, 4)
effect.snake(switch_direction = False)
cycle_beats(4, 8)
effect.snake(switch_direction = True)



beats(280, 344)
for elem in all:
    elem.straight
    elements(elem)
    color.uniform((random.random(), 1.0, 1.0))

elements(all)

beats(280, 288)
cycle(2)
effect.segment_breath(0.5)

beats(288, 296)
cycle(2)
effect.hue_breath(0.3)

beats(296, 304)
cycle(2)
effect.segment_saw_tooth()

beats(304, 312)
cycle(2)
effect.fill_out_in(0.7)

beats(312, 320)
cycle(1)
effect.hue_blink()

beats(320, 328)
cycle(2)
effect.snake_down_up()

beats(328, 336)
cycle(2)
effect.blink_repeat(48)

beats(336, 344)
cycle(2)
elements(dotted)
effect.breath(edge=0.4, reverse=True)
elements(not_dotted)
effect.breath(edge=0.4, reverse=False)

beats(344, 348)
elements(stands)
color.uniform((0.0, 0.0, 0.5))
cycle(4)
play_note("Bb", 0.0)
play_note("D", 0.25)
play_note("F", 0.5)
play_note("F", 0.75)
play_note("Bb", 0.75)
play_note("F", 1.25)
play_note("Bb", 1.25)
play_note("C", 1.75)

play_note("F", 2.0)
play_note("A", 2.0)
play_note("Eb", 2.5)
play_note("C", 2.5)
play_note("Bb", 3.0)
play_note("D", 3.0)

send_to_mqtt("under")
start_song("under", 0)


