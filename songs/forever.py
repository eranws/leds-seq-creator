import random

from animations import brightness
from animations.brightness import BrightnessAnimation
from float_func.sin import SinFloatFunc
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.flood import cup_cakes, cup_cake3, rug4, rug6, rugs
from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles, paper2, flower1, bottle4, bottle5, gloves
from led_objects.meduza import meduza
from led_objects.objects_selector import elements, elements_random
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands, \
    single_lifas, single_stands
from led_objects.stars import stars, star7, single_stars
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=68.8, beats_per_episode=8, start_offset=3.19)


def wave():
    cycle(8)
    elements([group1, group2])
    BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.0, 1)).apply()
    elements([group8, group3])
    BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.25, 1)).apply()
    elements([group6, group7])
    BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.5, 1)).apply()
    elements([group5, group4])
    BrightnessAnimation(SinFloatFunc(0.2, 1.0, 0.75, 1)).apply()


#background
episodes(0,4)
elements_random(list(set(all)-set(stars)-set(papers)))
cycle(1)
color.uniform(turquoise_string)
effect.hue_shift_cycle_target(0, red[0]-turquoise_string[0])
wave()

#Humming
def humming(start_beat):
    beats(start_beat, start_beat+10)
    elements(stars)
    color.uniform(red)

    beats(start_beat, start_beat+1)
    elements(single_stars)
    effect.fill_in_steps(3)

    beats(start_beat+8.5, start_beat+10)
    elements(single_stars)
    effect.fill_out()

    beats(start_beat+2, start_beat+8)
    elements_random(papers)
    cycle(2)
    cycle_beats(0.5,1)
    color.uniform(light_orange_strip)
    effect.brightness(0.5)
    effect.fade_in()
    cycle_beats(1,2)
    color.uniform(light_orange_string)
    effect.brightness(0.5)
    effect.fill_out()

humming(2)
humming(18)




#Episode 4- Shout

beats(31,61)
cycle(4)
cycle_beats(0,2)
elements(single_stands)
color.gradient(white,purple_string)
effect.fill()

###############episode 4##############

beats(33,70)
cycle(8)
cycle_beats(0,1)
elements(list(set(all)-set(stands)-set(cabbages)))
color.alternate(light_purple_string, purple_string)
effect.saw_tooth(medium)
cycle_beats(1,2)
elements(list(set(all)-set(stands)-set(cabbages)))
color.alternate(light_purple_string, purple_string)
effect.saw_tooth(medium)
cycle_beats(2,8)
elements(list(set(all)-set(stands)-set(cabbages)))
color.gradient(indigo[0], purple_strip[0])
effect.hue_breath()



#Weird sound
beats(48.6,49.3)
elements(cabbages)
color.uniform(indigo)
effect.snake(0.2, True)

#Confetti
beats(60,62)
elements_random(cabbages)
color.alternate(turquoise_string,indigo)
effect.fill_in_out()


##drums##
beats(63,63.3)
elements(group1)
color.uniform(red)
effect.hue_blink(medium)

beats(63.5,63.8)
elements(group5)
color.uniform(red)
effect.fill

beats(64,64.3)
elements(group3)
color.uniform(red)
effect.blink(medium)


#Episode8

#Singing

episodes(8,12)
cycle(8)
cycle_beats(0,1)
elements(list(set(all)-set(stands)-set(cabbages)))
color.alternate(light_purple_string, purple_string)
effect.saw_tooth(medium)
cycle_beats(1,2)
elements(list(set(all)-set(stands)-set(cabbages)))
color.alternate(light_purple_string, purple_string)
effect.saw_tooth(medium)
cycle_beats(2,8)
elements(list(set(all)-set(stands)-set(cabbages)))
color.gradient(indigo[0], purple_strip[0])
effect.hue_breath()
wave()
#
# episodes(8,12)
# cycle(8)
# cycle_beats(0,4)
# elements(all)
# color.gradient(indigo[0], purple_strip[0])
# effect.saw_tooth(total)
# wave()
#
# cycle_beats(4,8)
# elements(all)
# color.alternate(light_purple_string, purple_string)
# effect.breath()
# wave()

#piano
beats(67,91)
cycle(4)
cycle_beats(0,0.5)
elements(group1)
color.gradient(red[0], light_pink_strip[0])
effect.blink(medium)
cycle_beats(0.5,1)
elements(group3)
color.gradient(red[0], light_pink_strip[0])
effect.blink(medium)

#Drums

beats(92.5,93.3)
cycle(1)
elements(sticks)
color.uniform(orange_string)
effect.blink(medium)
beats(93.3,94)
cycle(1)
elements(sticks)
color.uniform(orange_string)
effect.blink(medium)

beats(94,95)
cycle(1/4)
elements(sticks)
color.uniform(orange_string)
effect.blink(total)

beats(95,95.5)
cycle(1)
elements(paper2)
color.uniform(red)
effect.blink(total)

beats(95.5,96)
cycle(1)
elements(paper5)
color.uniform(red)
effect.blink(total)

beats(96,96.5)
cycle(1)
elements(all)
color.uniform(white)
effect.blink(total)

#Episode12

#Singing

episodes(12,16)
cycle(8)
cycle_beats(0,1)
elements(list(set(all)-set(stands)-set(cabbages)))
color.alternate(light_purple_string, purple_string)
effect.saw_tooth(medium)
cycle_beats(1,2)
elements(list(set(all)-set(stands)-set(cabbages)))
color.alternate(light_purple_string, purple_string)
effect.saw_tooth(medium)
cycle_beats(2,8)
elements(list(set(all)-set(stands)-set(cabbages)))
color.gradient(indigo[0], purple_strip[0])
effect.hue_breath()
wave()
#
# cycle(8)
# elements(all)
# color.gradient(indigo[0], purple_strip[0])
# effect.hue_saw_tooth(hard)
# wave()



#end of last episode

beats(96,96.5)
cycle(1)
elements(all)
color.uniform(white)
effect.blink(total)


#piano
beats(99,115)
cycle(4)
cycle_beats(0,0.5)
elements(group5,group4)
color.gradient(indigo[0], light_blue[0])
effect.blink(medium)
cycle_beats(0.5,1)
elements(group3,group2,group1)
color.gradient(indigo[0], light_pink_strip[0])
effect.blink(medium)

#piano
beats(115,131)
cycle(4)
cycle_beats(0,0.5)
elements(group1,group6,group8)
color.gradient(indigo[0], light_blue[0])
effect.blink(medium)
cycle_beats(0.5,1)
elements(group4,group6)
color.gradient(indigo[0], light_pink_strip[0])
effect.blink(medium)


#Drums
beats(124.5,125.3)
cycle(1)
elements(sticks)
color.uniform(red)
effect.blink(medium)

beats(125.3,126)
cycle(1)
elements(sticks)
color.uniform(red)
effect.blink(medium)

beats(126,127)
cycle(1/4)
elements(sticks)
color.uniform(red)
effect.blink(total)


beats(127,127.5)
cycle(1)
elements(all)
color.uniform(white)
effect.blink(total)

beats(128,129)
elements(all)
color.uniform(white)
effect.blink_repeat(64)




send_to_mqtt("forever")
start_song("forever", 0)
