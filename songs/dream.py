from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.flood import cup_cakes, cup_cake3, rug4, rug6, rugs
from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles, paper2, flower1, bottle4, bottle5, gloves
from led_objects.meduza import meduza
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands, \
    single_lifas
from led_objects.stars import stars, star7
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=65, beats_per_episode=8, start_offset=1.44)

def turqouise_opening():

    elements(flowers)
    beats(0, 2)
    color.uniform(turquoise_string)
    effect.fade_in()

    elements(flowers)
    beats(2, 7)
    color.uniform(turquoise_string)

    elements(sticks)
    beats(2, 4)
    color.uniform(turquoise_string)
    effect.fade_in()

    elements(sticks)
    beats(4, 7)
    color.uniform(turquoise_string)

    elements(cabbages)
    beats(4, 6)
    color.uniform(turquoise_string)
    effect.fade_in()

    elements(cabbages)
    beats(6, 7)
    color.uniform(turquoise_string)

    elements(papers)
    beats(6, 7)
    color.uniform(turquoise_string)
    effect.fade_in()


episode(0)
turqouise_opening()

episode(1)

elements(sticks, cabbages, papers, flowers)
beats(7, 7.25)
color.uniform(indigo)
beats(7.25, 7.5)
color.uniform(purple_string)
beats(7.5, 7.75)
color.uniform(pink_string)
beats(7.75, 16)
color.uniform(coral)


beats(8, 10)
elements(lifas)
color.uniform(coral)
effect.fade_in()

beats(10, 16)
elements(lifas)
color.uniform(coral)

beats(10, 12)
elements(rugs)
color.uniform(coral)
effect.fade_in()

beats(12, 16)
elements(rugs)
color.uniform(coral)

beats(12, 13)
elements(cup_cakes)
color.uniform(coral)
effect.fade_in()

beats(13, 16)
elements(cup_cakes)
color.uniform(coral)

beats(13, 14)
elements(bottles, brain7)
color.uniform(coral)
effect.fade_in()

beats(14, 16)
elements(bottles, brain7)
color.uniform(coral)

beats(14, 15)
elements(donuts, gloves)
color.uniform(coral)
effect.fade_in()

beats(15, 16)
elements(donuts, gloves)
color.uniform(coral)

beats(15, 16)
elements(star7.all)
color.gradient(0.6, 1.0)
effect.snake(0.1)

beats(16, 17)
elements(all)
color.uniform(red)

beats(17, 18)
elements(all)
color.uniform(coral)

beats(18, 19)
elements(all)
color.uniform(red)

beats(19, 20)
cycle(0.5)
elements(all)
color.gradient(purple_string[0], coral[0])
effect.hue_blink(medium)


beats(20, 24)
elements(all)
color.uniform([1.0, 0.0, 0.3])

beats(20, 21)
elements( sticks, bottles, stars, donuts, papers)
color.gradient(purple_string[0], coral[0])

beats(20, 22)
elements(flowers, rugs, cup_cakes, gloves, rugs, lifas)
color.gradient(purple_string[0], coral[0])


beats(23, 24)
cycle(0.5)
elements(cabbages)
color.gradient(purple_string[0], coral[0])
effect.hue_blink(medium)

episodes(3, 4)
beats(24, 27)
elements(papers, sticks, lifas, rugs, cup_cakes, bottles, cabbages, donuts, gloves, flowers)
color.gradient(turquoise_string[0], purple_string[0])
effect.snake(0.3, True)

episodes(3, 4)
beats(28, 31)
elements(papers, sticks, lifas, rugs, cup_cakes, bottles, cabbages, donuts, gloves, flowers, brain7)
color.gradient(pink_string[0], purple_string[0])
effect.snake(0.7)

beats(24, 32)
elements(star7.all)
color.gradient(turquoise_string[0], purple_string[0])
effect.fill()

beats(31, 32)
cycle(0.25)
elements(star7.all)
effect.hue_breath(medium)

episode(4)
beats(32, 33)
elements(all)
color.uniform([0.88, 0.7, 0.25])

beats(33, 34)
elements(all)
color.uniform([0.88, 0.7, 0.5])


beats(34,34.33)
elements(all)
color.uniform([0.88, 0.7, 0.75])

beats(34.33, 34.66)
elements(all)
color.uniform([0.88, 0.7, 1.0])

beats(34.66, 35)
elements(all)
color.uniform([0.85, 0.75, 1.0])

beats(35, 35.33)
elements(all)
color.uniform([0.8, 0.8, 1.0])

beats(35.33, 35.66)
elements(all)
color.uniform([0.76, 0.85, 1.0])

beats(35.66, 36)
elements(all)
color.uniform([0.7, 0.9, 1.0])

beats(36, 37)
elements(all)
color.uniform([0.675, 1.0, 1.0])

beats(37, 38)
elements(all)
color.uniform([0.675, 1.0, 0.66])

beats(38, 39)
elements(all)
color.uniform([0.675, 1.0, 0.33])
effect.fill_out()

episode(5)

beats(40, 44)
elements(group1)
color.gradient(purple_string[0], blue[0])
effect.fill_in_out()

beats(42,46)
elements(group2)
color.gradient(blue[0], turquoise_string[0])
effect.fill_in_out()

beats(44,48)
elements(group3)
color.gradient(aquamarine[0], turquoise_string[0])
effect.fill_in_out()

beats(46,50)
elements(group4)
color.gradient(aquamarine[0], green[0])
effect.fill_in_out()

beats(48,52)
elements(group5)
color.gradient(green[0], yellow_strip[0])
effect.fill_in_out()

beats(50,54)
elements(group6)
color.gradient(yellow_strip[0], orange_strip[0])
effect.fill_in_out()

beats(52, 56)
elements(group7, group8)
color.gradient(coral[0], orange_strip[0])
effect.fill_in_out()

beats(56, 63)
elements(donuts, flowers, papers)
color.uniform(light_coral)
effect.snake(0.5)

beats(64, 72)
elements(cup_cakes, bottles, cabbages)
color.uniform(light_coral)
effect.snake(0.5)

beats(72, 84)
elements(star7.all ,single_sticks, single_lifas)
color.alternate(light_yellow_strip, yellow_strip)
effect.fill()

beats(84, 88)
elements(all)
color.alternate(light_yellow_strip, yellow_strip)

beats(84, 88)
elements(donuts, gloves , brain7)
color.alternate(light_yellow_strip, yellow_strip)
effect.fade_in()

beats(85, 88)
elements(bottles, papers, cup_cakes)
color.alternate(light_yellow_strip, yellow_strip)
effect.fade_in()

beats(86, 88)
elements(rugs, flowers)
color.alternate(light_yellow_strip, yellow_strip)
effect.fade_in()

beats(0,300)
elements(meduza)
color.uniform(red)








#
# elements(flowers)
# beats(24, 25)
# color.uniform(turquoise_string)
# effect.fill()
#
# elements(flowers)
# beats(25, 32)
# color.uniform(turquoise_string)
#
#
# elements(sticks)
# beats(26, 27)
# color.uniform(turquoise_string)
# effect.fade_in()
#
# elements(sticks)
# beats(27, 32)
# color.uniform(turquoise_string)





send_to_mqtt("dream")
start_song("dream", 0)

