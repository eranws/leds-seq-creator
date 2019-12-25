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
color.uniform(magenta)

beats(17, 18)
elements(all)
color.uniform(coral)

beats(18, 19)
elements(all)
color.uniform(magenta)

beats(19, 20)
cycle(0.5)
elements(all)
color.gradient(purple_string[0], coral[0])
effect.hue_blink(medium)


beats(20, 24)
elements(all)
color.uniform([1.0, 0.0, 0.7])

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
beats(24, 28)
elements(papers, sticks, lifas, rugs, cup_cakes, bottles, cabbages, donuts, gloves, flowers)
color.gradient(turquoise_string[0], purple_string[0])
effect.snake(0.3, True)

beats(27, 28)
elements(papers, sticks, lifas, rugs, cup_cakes, bottles, cabbages, donuts, gloves, flowers)
effect.fade_out(0.3, True)

beats(28, 32)
elements(papers, lifas, rugs, cup_cakes, bottles, cabbages, donuts, gloves, flowers, brain7)
color.gradient(pink_string[0], purple_string[0])
effect.snake(0.7)

beats(31, 32)
elements(papers, lifas, rugs, cup_cakes, bottles, cabbages, donuts, gloves, flowers, brain7)
effect.fade_out()

beats(27, 28)
elements(sticks)
color(turquoise_strip)
effect.breath(medium)

beats(24, 31)
elements(star7.all)
color.gradient(turquoise_string[0], purple_string[0])
effect.fill()

beats(31, 32)
elements(star7)
cycle(0.25)
color.gradient(turquoise_string[0], purple_string[0])
effect.random_brightness()
effect.hue_shift_steps(4, 0.08)



episode(4)
beats(32, 33)
elements(all)
color.uniform([0.88, 0.7, 0.25])

beats(33, 34)
elements(all)
color.uniform([0.88, 0.7, 0.5])


beats(34, 34.3)
elements(all)
color.uniform([0.88, 0.7, 0.75])

# beats(34.3, 34.6)
# elements(all)
# color.uniform([0.88, 0.7, 1.0])
#
# beats(34.66, 35)
# elements(all)
# color.uniform([0.85, 0.75, 1.0])
#
# beats(35, 35.33)
# elements(all)
# color.uniform([0.8, 0.8, 1.0])
#
# beats(35.33, 35.66)
# elements(all)
# color.uniform([0.76, 0.85, 1.0])
#
# beats(35.66, 36)
# elements(all)
# color.uniform([0.7, 0.9, 1.0])

beats(34.3, 36)
elements(group4, group8)
color.uniform([0.675, 1.0, 1.0])

beats(34.66, 36)
elements(group2, group6)
color.uniform([0.675, 1.0, 1.0])

beats(35, 36)
elements(group3)
color.uniform([0.675, 1.0, 1.0])

beats(35.33, 36)
elements(group7, group5)
color.uniform([0.675, 1.0, 1.0])

beats(35.66, 36)
elements(group1)
color.uniform([0.675, 1.0, 1.0])

beats(36, 37)
elements(all)
color.uniform([0.675, 1.0, 0.8])

beats(37, 38)
elements(all)
color.uniform([0.675, 1.0, 0.66])

beats(38, 39)
elements(all)
color.uniform([0.675, 1.0, 0.33])
effect.fill_out()

beats(39, 40)
elements(all)
cycle(0.25)
color.gradient(indigo[0], purple_string[0])
effect.random_brightness()
effect.hue_shift_steps(4, 0.08)

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

episode(5)
cycle_beats(6/10)
elements(gloves)
effect.breath(soft)

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



episode(11)

beats(88, 92)
elements(group1)
color.gradient(purple_string[0], blue[0])
effect.breath(total)

beats(90,94)
elements(group2)
color.gradient(blue[0], turquoise_string[0])
effect.breath(total)

beats(92,96)
elements(group3)
color.gradient(aquamarine[0], turquoise_string[0])
effect.breath(total)

beats(94,98)
elements(group4)
color.gradient(aquamarine[0], green[0])
effect.breath(total)

beats(96,100)
elements(group5)
color.gradient(green[0], yellow_strip[0])
effect.breath(total)

beats(98,102)
elements(group6)
color.gradient(yellow_strip[0], orange_strip[0])
effect.breath(total)

beats(98, 100)
cycle_beats(0.33)
elements(group6)
effect.hue_blink(hard)

beats(100, 104)
elements(group7, group8)
color.gradient(coral[0], orange_strip[0])
effect.breath(total)

episodes(11, 12)
cycle_beats(6/10)
elements(gloves)
color.uniform(aquamarine)
effect.breath(soft)

beats(95, 96)
elements(star7.all)
color.gradient(indigo[0], purple_strip[0])
effect.snake(0.2, True)

episode(13)

beats(104, 116)
elements(star7.all ,single_sticks, single_lifas)
color.alternate(light_yellow_strip, yellow_strip)
effect.fill()

beats(116, 120)
elements(all)
color.alternate(aquamarine, light_blue)

beats(116, 120)
elements(donuts, gloves , brain7)
color.alternate(aquamarine, light_blue)
effect.fade_in()

beats(117, 120)
elements(bottles, papers, cup_cakes)
color.alternate(aquamarine, light_blue)
effect.fade_in()

beats(118, 120)
elements(rugs, flowers)
color.alternate(aquamarine, light_blue)
effect.fade_in()

beats(104, 120)
cycle(1)
elements(all)
effect.hue_saw_tooth(hard, False)
beats(104, 120)
cycle(16)
elements(all)
effect.hue_breath(soft)

beats(104)
elements(donut1)
color([1.0, 0.0, 1.0])
effect.saw_tooth(total)

beats(106)
elements(brain7)
color([1.0, 0.0, 1.0])
effect.saw_tooth(total)

beats(108)
elements(flower1)
color([1.0, 0.0, 1.0])
effect.saw_tooth(total)

beats(110)
elements(paper5)
color([1.0, 0.0, 1.0])
effect.saw_tooth(total)

beats(112)
elements(cup_cake3)
color([1.0, 0.0, 1.0])
effect.saw_tooth(total)

beats(114)
elements(cabbage6)
color([1.0, 0.0, 1.0])
effect.saw_tooth(total)

beat(119)
elements(all)
effect.fade_out()

episodes(15, 18)
elements(flowers, bottles, gloves, papers)
color.uniform(aquamarine)
elements(sticks, lifas)
color.uniform(light_blue)
elements(rugs, star7, cup_cakes)
color.uniform(blue)
elements(cabbages, brain7)
cycle(4)
effect.hue_saw_tooth(soft)
cycle(1/6)
effect.blink(soft)

beats(120, 128)
elements(all)
effect.fade_in()

episode(18)
beats(136, 138)
cycle(1)
elements(sticks)
color.gradient(yellow_strip, orange_strip)
effect.breath(medium)
beats(138, 150)
elements(sticks)
color.gradient(yellow_strip, orange_strip)

beats(138, 140)
cycle(1)
elements(flowers)
color.gradient(yellow_strip, orange_strip)
effect.breath(medium)
beats(140, 150)
elements(flowers)
color.gradient(yellow_strip, orange_strip)

beats(140, 142)
cycle(1)
elements(cup_cakes)
color.gradient(yellow_strip, orange_strip)
effect.breath(medium)
beats(142, 150)
elements(cup_cakes)
color.gradient(yellow_strip, orange_strip)

beats(142, 144)
cycle(1)
elements(rugs)
color.gradient(yellow_strip, orange_strip)
effect.breath(medium)
beats(144, 150)
elements(rugs)
color.gradient(yellow_strip, orange_strip)

beats(144, 146)
cycle(1)
elements(papers, cabbages)
color.gradient(yellow_strip, orange_strip)
effect.breath(medium)
beats(146, 150)
elements(papers,cabbages)
color.gradient(yellow_strip, orange_strip)

beats(146, 148)
cycle(1)
elements(lifas, cup_cakes)
color.gradient(yellow_strip, orange_strip)
effect.breath(medium)
beats(148, 150)
elements(lifas, cup_cakes)
color.gradient(yellow_strip, orange_strip)

beats(148, 150)
cycle(1)
elements(star7, gloves, bottles)
color.gradient(yellow_strip, orange_strip)
effect.breath(medium)

beats(150, 151)
elements(all)
color.uniform(indigo)

beats(152, 152)
elements(all)
color.uniform(light_blue)
effect.fill_out()
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

