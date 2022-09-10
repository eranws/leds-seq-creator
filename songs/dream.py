import random

from infra.animations_factory import color, effect
from infra.length import medium, soft, hard, total
from led_objects.instances import *
from led_objects.groups import (
    group1,
    group2,
    group3,
    group4,
    group5,
    group6,
    group7,
    group8,
)
from led_objects.led_object import all
from led_objects.groups import *
from led_objects.meduza import meduza
from led_objects.objects_selector import elements, elements_random
from led_objects.sheep import sheep

# from led_objects.stars import stars, star7, single_stars, star8
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=65, beats_per_episode=8, start_offset=3.44)


def turqouise_opening():
    cycle(8)

    elements(flowers)
    cycle_beats(0, 2)
    color.uniform(turquoise_string)
    effect.fade_in()

    elements(flowers)
    cycle_beats(2, 7)
    color.uniform(turquoise_string)

    elements(sticks)
    cycle_beats(2, 4)
    color.uniform(turquoise_string)
    effect.fade_in()

    elements(sticks)
    cycle_beats(4, 7)
    color.uniform(turquoise_string)

    elements(cabbages)
    cycle_beats(4, 6)
    color.uniform(turquoise_string)
    effect.fade_in()

    elements(cabbages)
    cycle_beats(6, 7)
    color.uniform(turquoise_string)

    elements(papers)
    cycle_beats(6, 7)
    color.uniform(turquoise_string)
    effect.fade_in()

    elements(sticks, cabbages, papers, flowers)
    cycle_beats(7, 7.25)
    color.uniform(indigo)
    cycle_beats(7.25, 7.5)
    color.uniform(purple_string)
    cycle_beats(7.5, 7.75)
    color.uniform(pink_string)
    cycle_beats(7.75, 8)
    color.uniform(light_coral)


episode(0)
turqouise_opening()
elements(sticks, cabbages, papers, flowers)
beats(8, 16)
color.uniform(light_coral)


def opening_coral():
    cycle(8)

    cycle_beats(0, 2)
    elements(lifas)
    color.uniform(coral)
    effect.fade_in()

    cycle_beats(2, 8)
    elements(lifas)
    color.uniform(coral)

    cycle_beats(2, 4)
    elements(rugs)
    color.uniform(coral)
    effect.fade_in()

    cycle_beats(4, 8)
    elements(rugs)
    color.uniform(coral)

    cycle_beats(4, 5)
    elements(cup_cakes)
    color.uniform(coral)
    effect.fade_in()

    cycle_beats(5, 8)
    elements(cup_cakes)
    color.uniform(coral)

    cycle_beats(5, 6)
    elements(bottles, brain7)
    color.uniform(coral)
    effect.fade_in()

    cycle_beats(6, 8)
    elements(bottles, brain7)
    color.uniform(coral)

    cycle_beats(6, 7)
    elements(donuts, gloves)
    color.uniform(coral)
    effect.fade_in()

    cycle_beats(7, 8)
    elements(donuts, gloves)
    color.uniform(coral)

    cycle_beats(7, 8)
    elements(single_stars, meduza)
    color.gradient(0.6, 1.0)
    effect.snake(0.1)


episode(1)
opening_coral()


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
elements(sticks, bottles, stars, donuts, papers)
color.gradient(purple_string[0], coral[0])

beats(20, 22)
elements(flowers, rugs, cup_cakes, gloves, rugs, lifas)
color.gradient(purple_string[0], coral[0])


beats(23, 24)
cycle(0.5)
elements(cabbages)
color.gradient(pink_string[0], coral[0])
effect.hue_blink(medium)

episodes(3, 4)
beats(24, 28)
elements(
    papers, sticks, lifas, rugs, cup_cakes, bottles, cabbages, donuts, gloves, flowers
)
color.gradient(turquoise_string[0], purple_string[0])
effect.snake(0.3, True)

beats(27, 28)
elements(
    papers, sticks, lifas, rugs, cup_cakes, bottles, cabbages, donuts, gloves, flowers
)
effect.fade_out()

beats(28, 32)
elements(
    papers, lifas, rugs, cup_cakes, bottles, cabbages, donuts, gloves, flowers, brain7
)
color.gradient(pink_string[0], purple_string[0])
effect.snake(0.7)

beats(31, 32)
elements(
    papers, lifas, rugs, cup_cakes, bottles, cabbages, donuts, gloves, flowers, brain7
)
effect.fade_out()

beats(27, 28)
elements(sticks)
color.uniform(coral)
effect.breath(medium)

beats(24, 31)
elements(single_stars, meduza)
color.gradient(turquoise_string[0], purple_string[0])
effect.fill()

beats(31, 32)
elements(star7, star8)
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

beats(42, 46)
elements(group2)
color.gradient(blue[0], turquoise_string[0])
effect.fill_in_out()

beats(44, 48)
elements(group3)
color.gradient(aquamarine[0], turquoise_string[0])
effect.fill_in_out()

beats(46, 50)
elements(group4)
color.gradient(aquamarine[0], green[0])
effect.fill_in_out()

beats(48, 52)
elements(group5)
color.gradient(green[0], yellow_strip[0])
effect.fill_in_out()

beats(50, 54)
elements(group6)
color.gradient(yellow_strip[0], orange_strip[0])
effect.fill_in_out()

beats(52, 56)
elements(group7, group8)
color.gradient(0.85, 0.9)
effect.fill_in_out()

episode(5)
cycle(6 / 10)
elements(gloves, sheep)
effect.breath(soft)

beats(56, 72)
for elem in donuts, flowers, papers, rugs:
    elements(elem)
    color.uniform(
        random.choice(
            [light_coral, light_orange_string, light_pink_strip, light_yellow_strip]
        )
    )
beats(56, 64)
elements(donuts, flowers, papers, rugs)
effect.fill_in_steps(24)

beats(64, 72)
cycle(8)
elements(donuts, flowers, papers, rugs)

effect.hue_saw_tooth(medium, True)
beats(70, 72)
elements(donuts, flowers, papers, rugs)
effect.fade_out()


beats(64, 72)
elements(cup_cakes, bottles, cabbages, gloves, brain7)
color.uniform(light_coral)
effect.fill_in_steps(48)
beats(70, 72)
elements(cup_cakes, bottles, cabbages, gloves, brain7)
color.uniform(light_coral)
effect.fade_out()


beats(72, 84)
elements(single_stars, meduza, single_sticks, single_lifas)
color.alternate(light_yellow_strip, yellow_strip)
effect.fill()

beats(84, 88)
elements(single_stars, meduza, sticks, lifas)
color.alternate(light_yellow_strip, yellow_strip)

beats(84, 88)
elements(donuts, gloves, brain7)
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

for elem in all:
    elem.random

beats(88, 92)
elements(group1)
color.gradient(purple_string[0], blue[0])
effect.saw_tooth(total)
beats(92, 102)
elements(group1)
color.uniform((0.11, 0.8, 0.4))
effect.fade_in()

beats(90, 94)
elements(group2)
color.gradient(blue[0], turquoise_string[0])
effect.saw_tooth(total)
beats(94, 102)
elements(group2)
color.uniform((0.11, 0.8, 0.4))
effect.fade_in()

beats(92, 96)
elements(group3)
color.gradient(aquamarine[0], turquoise_string[0])
effect.saw_tooth()
beats(96, 102)
elements(group3)
color.uniform((0.11, 0.8, 0.4))
effect.fade_in()

beats(93, 95)
elements(group4)
color.gradient(aquamarine[0], green[0])
effect.saw_tooth(total)
beats(95, 102)
elements(group4)
color.uniform((0.11, 0.8, 0.4))
effect.fade_in()

beats(94, 96)
elements(group5)
color.gradient(green[0], yellow_strip[0])
effect.saw_tooth(total)
beats(96, 102)
elements(group5)
color.uniform((0.11, 0.8, 0.4))
effect.fade_in()


beats(96, 98)
elements(group6)
color.gradient(yellow_strip[0], orange_strip[0])
effect.saw_tooth(total)
beats(98, 102)
elements(group6)
color.uniform((0.11, 0.8, 0.4))
effect.fade_in()

beats(97, 99)
elements(group8)
color.gradient(pink_strip[0], magenta[0])
effect.saw_tooth(total)
beats(99, 102)
elements(group8)
color.uniform((0.11, 0.8, 0.4))
effect.fade_in()

beats(98, 98.3)
elements(group7)
color.uniform(pink_string)
beats(98.3, 98.6)
elements(group7)
color.uniform(magenta)
beats(98.6, 99)
elements(group7)
color.uniform(purple_string)
beats(99, 99.3)
elements(group7)
color.uniform(magenta)
beats(99.3, 99.6)
elements(group7)
color.uniform(pink_string)
beats(99.6, 100)
elements(group7)
color.uniform(light_orange_strip)
beats(100, 102)
elements(group7)
color.uniform((0.11, 0.8, 0.4))

beats(101, 102)
elements(all)
effect.breath(medium)

beats(102, 103)
elements_random(all)
color.uniform((0.11, 0.8, 0.4))
effect.fill()

beats(103, 104)
elements_random(all)
color.uniform((0.2, 0.8, 0.4))
effect.fill_out(True)


for elem in all:
    elem.straight

beats(88, 104)
cycle(1 / 6)
elements(gloves, sheep)
color.uniform(light_coral)
effect.breath(0.2)


beats(95, 96)
elements(single_stars, meduza)
color.gradient(indigo[0], purple_strip[0])
effect.snake(0.2, True)

episode(13)

beats(104, 115.5)
elements(flowers, papers, brain7, gloves, cabbages)
color.alternate(light_purple_string, purple_string)
effect.fill()
cycle(1)
effect.hue_saw_tooth(soft)
beats(115.5, 116)
elements(flowers, papers, brain7, gloves, cabbages)
color.alternate(light_purple_string, purple_string)
effect.fill_out()

beats(104, 106)
cycle(2)
elements(sticks7)
color.uniform(coral)
effect.blink(medium)

beats(106, 108)
cycle(2)
elements(lifas5)
color.uniform(coral)
effect.blink(medium)

beats(108, 110)
cycle(2)
elements(sticks3)
color.uniform(coral)
effect.blink(medium)

beats(110, 112)
cycle(2)
elements(lifas1)
color.uniform(coral)
effect.blink(medium)

beats(112, 114)
cycle(2)
elements(sticks8)
color.uniform(coral)
effect.blink(medium)

beats(114, 116)
cycle(2)
elements(lifas4)
color.uniform(coral)
effect.blink(medium)

beats(116, 120)
elements(donuts, gloves, brain7)
color.alternate(aquamarine, light_blue)
effect.saw_tooth(total)

beats(117, 120)
elements(bottles, papers, cup_cakes)
color.alternate(aquamarine, light_blue)
effect.saw_tooth(total)

beats(118, 120)
elements(rugs, flowers, cabbages)
color.alternate(aquamarine, light_blue)
effect.saw_tooth(total)

beats(119, 120)
elements(sticks, lifas, star7, star8)
color.alternate(aquamarine, light_blue)
effect.saw_tooth(total)


episodes(15, 18)
beats(120, 152)
elements(flowers, bottles, gloves, papers)
color.uniform(aquamarine)
elements(sticks, lifas)
color.uniform(light_blue)
elements(rugs, star7, star8, cup_cakes)
color.uniform(blue)
elements(cabbages, brain7)
color.uniform(turquoise_strip)
elements(all)
cycle(4)
effect.hue_saw_tooth(soft)


beats(120, 128)
elements(all)
effect.fade_in()

beats(120, 128)
cycle(0.01)
elements(all)
effect.breath(0.1)

beats(128, 136)
cycle(0.33)
elements(all)
effect.breath(0.1)

episode(18)
beats(136, 138)
cycle(1)
elements(sticks)
color.gradient(yellow_strip[0], orange_strip[0])
effect.breath(medium)
beats(138, 150)
elements(sticks)
color.gradient(yellow_strip[0], orange_strip[0])

beats(138, 140)
cycle(1)
elements(flowers)
color.gradient(yellow_strip[0], orange_strip[0])
effect.breath(medium)
beats(140, 150)
elements(flowers)
color.gradient(yellow_strip[0], orange_strip[0])

beats(140, 142)
cycle(1)
elements(cup_cakes)
color.gradient(yellow_strip[0], orange_strip[0])
effect.breath(medium)
beats(142, 150)
elements(cup_cakes)
color.gradient(yellow_strip[0], orange_strip[0])

beats(142, 144)
cycle(1)
elements(rugs)
color.gradient(yellow_strip[0], orange_strip[0])
effect.breath(medium)
beats(144, 150)
elements(rugs)
color.gradient(yellow_strip[0], orange_strip[0])

beats(144, 146)
cycle(1)
elements(papers, cabbages, brain7)
color.gradient(yellow_strip[0], orange_strip[0])
effect.breath(medium)
beats(146, 150)
elements(papers, cabbages, brain7)
color.gradient(yellow_strip[0], orange_strip[0])

beats(146, 148)
cycle(1)
elements(lifas, cup_cakes)
color.gradient(yellow_strip[0], orange_strip[0])
effect.breath(medium)
beats(148, 150)
elements(lifas, cup_cakes)
color.gradient(yellow_strip[0], orange_strip[0])

beats(148, 150)
cycle(1)
elements(star7, star8, gloves, bottles)
color.gradient(yellow_strip[0], orange_strip[0])
effect.breath(medium)

beats(150, 151)
elements(all)
color.uniform(indigo)

beats(151, 152)
elements(all)
color.gradient(indigo[0], light_blue[0])
effect.fill_out()


beats(152, 153)
elements(all)
color.uniform(magenta)

beats(152 + 17 - 16, 152 + 18 - 16)
elements(all)
color.uniform(coral)

beats(152 + 18 - 16, 152 + 19 - 16)
elements(all)
color.uniform(magenta)

beats(152 + 19 - 16, 152 + 20 - 16)
cycle(0.5)
elements(all)
color.gradient(purple_string[0], coral[0])
effect.hue_blink(medium)


beats(152 + 20 - 16, 152 + 24 - 16)
elements(all)
color.uniform([1.0, 0.0, 0.7])

beats(152 + 20 - 16, 152 + 21 - 16)
elements(sticks, bottles, stars, donuts, papers)
color.gradient(purple_string[0], coral[0])

beats(152 + 20 - 16, 152 + 22 - 16)
elements(flowers, rugs, cup_cakes, gloves, rugs, lifas)
color.gradient(purple_string[0], coral[0])


beats(152 + 23 - 16, 152 + 24 - 16)
cycle(0.33)
elements(cabbages)
color.gradient(coral[0], orange_strip[0] + 1)
effect.hue_blink(medium)

beats(24 + 136, 28 + 136)
elements(
    papers, sticks, lifas, rugs, cup_cakes, bottles, cabbages, donuts, gloves, flowers
)
color.gradient(turquoise_string[0], purple_string[0])
effect.snake(0.3, True)

beats(27 + 136, 28 + 136)
elements(
    papers, sticks, lifas, rugs, cup_cakes, bottles, cabbages, donuts, gloves, flowers
)
effect.fade_out()


beats(28 + 136, 32 + 136)
elements(
    papers, lifas, rugs, cup_cakes, bottles, cabbages, donuts, gloves, flowers, brain7
)
color.gradient(pink_string[0], purple_string[0])
effect.snake(0.7)

beats(31 + 136, 32 + 136)
elements(
    papers, lifas, rugs, cup_cakes, bottles, cabbages, donuts, gloves, flowers, brain7
)
effect.fade_out()


for elem in [sticks7, sticks3, sticks8, sticks7]:
    elem.random
beats(27 + 136, 28 + 136)
elements(sticks)
color.uniform(turquoise_strip)
effect.snake(0.2)


beats(24 + 136, 31 + 136)
elements(single_stars, meduza)
color.gradient(turquoise_string[0], purple_string[0])
effect.fill()

beats(31 + 136, 32 + 136)
elements(star7, star8)
cycle(0.25)
color.gradient(turquoise_string[0], purple_string[0])
effect.random_brightness()
effect.hue_shift_steps(4, 0.08)

for elem in [sticks7, sticks3, sticks8, star7, star8]:
    elem.straight


beats(168, 169)
elements(papers, lifas, donuts)
color.uniform(aquamarine)
effect.fade_in()
beats(169, 169.3)
elements(papers, lifas, donuts)
color.uniform((0.39, 0.75, 1.0))
beats(169.3, 169.6)
elements(papers, lifas, donuts)
color.uniform((0.39, 0.55, 1.0))
beats(169.6, 170)
elements(papers, lifas, donuts)
color.uniform((0.39, 0.35, 1.0))


beats(170, 171)
elements(sticks, star7, star8, flowers)
color.uniform(orange_strip)
effect.fade_in()
beats(171, 172)
elements(sticks, single_stars, meduza, flowers)
color.uniform((0.045, 0.75, 1.0))
effect.fill_out()

beats(172, 173)
elements(all)
color.uniform(light_coral)
effect.breath(soft)

beats(173, 174)
elements(all)
color.uniform((0.995, 0.75, 1.0))
effect.breath(soft)

beats(174, 175)
elements(all)
color.uniform(coral)
effect.breath(soft)

beats(175, 176)
elements(all)
color.gradient(coral[0], light_pink_strip[0])
effect.fill_out()

beats(176, 177)
elements(group8, group4, group2, group6)
color.alternate(dark_blue, blue)

beats(177, 177.3)
elements(group8, group4, group2, group6)
color.alternate(light_blue, blue)

beats(177.3, 177.6)
elements(group8, group4, group2, group6)
color.alternate(light_blue, turquoise_strip)

beats(177.6, 184)
elements(group8, group4, group2, group6)
color.alternate(turquoise_strip, aquamarine)

beats(178, 179)
elements(group1, group3, group5, group7)
color.alternate(yellow_strip, orange_strip)

beats(179, 179.3)
elements(group1, group3, group5, group7)
color.alternate(yellow_strip, light_green)

beats(179.3, 179.6)
elements(group1, group3, group5, group7)
color.alternate(light_green, turquoise_strip)

beats(179.6, 184)
elements(group1, group3, group5, group7)
color.alternate(turquoise_strip, aquamarine)


beats(180, 184)
elements(all)
effect.fade_in()


beats(184, 188)
for elem in all:
    elements(elem)
    color.uniform(random.choice([blue, indigo, light_blue, turquoise_strip]))
elements(all)
effect.fade_out()
beats(184, 187 + 1 / 3)
cycle(1 / 3)
elements(all)
effect.breath(0.2, 0.2)

beats(187, 188)
elements_random(gloves, sheep)
color.uniform(light_yellow_strip)
effect.snake(0.8, True)

beats(188, 204)
elements(papers)
color.uniform(light_coral)
effect.fill_in_steps(36)
effect.brightness(0.5)

beats(204, 216)
cycle(12)
elements_random(papers)
color.uniform(light_purple_string)
effect.fill_out(reverse=True)
effect.brightness(0.5)


beats(188, 192)
elements(
    lifas4.stand(1),
    sticks7.stand(1),
    sticks8.stand(1),
    sticks3.stand(1),
    lifas5.stand(1),
    lifas1.stand(1),
)
color.uniform(orange_strip)
effect.saw_tooth(total)

beats(192, 196)
elements(
    lifas4.stand(2),
    sticks7.stand(2),
    sticks8.stand(2),
    sticks3.stand(2),
    lifas5.stand(2),
    lifas1.stand(2),
)
color.uniform(orange_strip)
effect.saw_tooth(total)

beats(195.5, 196)
elements(
    lifas4.stand(3),
    sticks7.stand(3),
    sticks8.stand(3),
    sticks3.stand(3),
    lifas5.stand(3),
    lifas1.stand(3),
)
color.uniform(coral)


beats(196, 199)
elements(
    lifas4.stand(3),
    sticks7.stand(3),
    sticks8.stand(3),
    sticks3.stand(3),
    lifas5.stand(3),
    lifas1.stand(3),
)
color.uniform(orange_strip)
effect.saw_tooth(total)

beats(199, 199.8)
elements(
    lifas4.stand(4),
    sticks7.stand(4),
    sticks8.stand(4),
    sticks3.stand(4),
    lifas5.stand(4),
    lifas1.stand(4),
)
color.uniform(red)

beats(199.8, 200)
elements(
    lifas4.stand(4),
    sticks7.stand(4),
    sticks8.stand(4),
    sticks3.stand(4),
    lifas5.stand(4),
    lifas1.stand(4),
)
color.uniform(coral)


beats(200, 204)
elements(
    lifas4.stand(4),
    sticks7.stand(4),
    sticks8.stand(4),
    sticks3.stand(4),
    lifas5.stand(4),
    lifas1.stand(4),
)
color.uniform(orange_strip)
effect.saw_tooth(total)

beats(203.8, 204)
elements(
    lifas4.stand(1),
    sticks7.stand(1),
    sticks8.stand(1),
    sticks3.stand(1),
    lifas5.stand(1),
    lifas1.stand(1),
)
color.uniform(coral)


beats(204, 206)
elements(
    lifas4.stand(1),
    sticks7.stand(1),
    sticks8.stand(1),
    sticks3.stand(1),
    lifas5.stand(1),
    lifas1.stand(1),
)
color.uniform(orange_strip)
effect.saw_tooth(total)

beats(206, 208)
elements(
    lifas4.stand(2),
    sticks7.stand(2),
    sticks8.stand(2),
    sticks3.stand(2),
    lifas5.stand(2),
    lifas1.stand(2),
)
color.uniform(orange_strip)
effect.saw_tooth(total)

beats(208, 210)
elements(
    lifas4.stand(3),
    sticks7.stand(3),
    sticks8.stand(3),
    sticks3.stand(3),
    lifas5.stand(3),
    lifas1.stand(3),
)
color.uniform(orange_strip)
effect.saw_tooth(total)

beats(211.83, 212)
elements(
    lifas4.stand(1),
    sticks7.stand(1),
    sticks8.stand(1),
    sticks3.stand(1),
    lifas5.stand(1),
    lifas1.stand(1),
)
color.uniform(coral)

beats(212, 214)
elements(
    lifas4.stand(1),
    sticks7.stand(1),
    sticks8.stand(1),
    sticks3.stand(1),
    lifas5.stand(1),
    lifas1.stand(1),
)
color.uniform(orange_strip)
effect.saw_tooth(total)

beats(214, 216)
elements(
    lifas4.stand(2),
    sticks7.stand(2),
    sticks8.stand(2),
    sticks3.stand(2),
    lifas5.stand(2),
    lifas1.stand(2),
)
color.uniform(orange_strip)
effect.saw_tooth(total)

beats(216, 218)
elements(
    lifas4.stand(3),
    sticks7.stand(3),
    sticks8.stand(3),
    sticks3.stand(3),
    lifas5.stand(3),
    lifas1.stand(3),
)
color.uniform(orange_strip)
effect.saw_tooth(total)

beats(204, 216)
elements(single_stars, meduza)
color.uniform(indigo)
effect.fill()

beats(204, 216)
elements(donuts, cabbages, gloves, bottles, flowers, rugs, brain7, cup_cakes)
color.gradient(aquamarine[0], turquoise_strip[0])
effect.fade_in()

beats(204, 216)
cycle(2)
elements(donuts, cabbages, gloves, bottles, flowers, rugs, brain7, cup_cakes)
effect.hue_saw_tooth(medium)


beats(216, 217)
elements(all)
color.uniform(indigo)

beats(217, 218)
elements(all)
color.uniform(purple_string)


beats(218, 220)
cycle(2)
elements_random(all)
elements(all)
color.uniform(purple_string)
effect.fill_out(True)


beats(40 + 180, 44 + 180)
elements(group1)
color.gradient(purple_string[0], blue[0])
effect.fill_in_out()

beats(42 + 180, 46 + 180)
elements(group2)
color.gradient(blue[0], turquoise_string[0])
effect.fill_in_out()

beats(44 + 180, 48 + 180)
elements(group3)
color.gradient(aquamarine[0], turquoise_string[0])
effect.fill_in_out()

beats(46 + 180, 50 + 180)
elements(group4)
color.gradient(aquamarine[0], green[0])
effect.fill_in_out()

beats(48 + 180, 52 + 180)
elements(group5)
color.gradient(green[0], yellow_strip[0])
effect.fill_in_out()

beats(50 + 180, 54 + 180)
elements(group6)
color.gradient(yellow_strip[0], orange_strip[0])
effect.fill_in_out()

beats(52 + 180, 56 + 180)
elements(group7, group8)
color.gradient(0.8, 0.99)
effect.fill_in_out()

beats(220, 229)
cycle(1)
elements(all)
effect.hue_saw_tooth(total)

beats(229, 230)
cycle(0.3)
elements(all)
effect.hue_saw_tooth(total)

beats(231, 232)
cycle(0.3)
elements(all)
effect.hue_saw_tooth(hard)

beats(232, 234)
cycle(1)
elements(all)
effect.hue_saw_tooth(hard)


beats(234, 235)
elements(single_stars, meduza)
color.alternate(magenta, light_pink_strip)
effect.snake(0.1)

beats(235, 236)
elements_random(gloves, sheep)
color.uniform(light_purple_string)
effect.snake(0.8, True)

beats(236, 244)
elements(all)
color.uniform(purple_string)
effect.saw_tooth(total)

beats(244, 253)
elements(all)
color.uniform((0.675, 0.8, 1.0))
effect.saw_tooth(total)

beats(252, 253)
elements(all)
effect.fill_out()

beats(236, 253)
elements(papers, flowers)
color.uniform(light_orange_string)
effect.snake()
cycle(1)
effect.hue_saw_tooth(soft)

beats(251, 252)
elements_random(meduza)
color.gradient(blue[0], indigo[0])
effect.fill_in_out()
#
# episode(4)
# beats(152+32, 152+33)
# elements(all)
# color.uniform([0.88, 0.7, 0.25])
#
# beats(152+33, 152+34)
# elements(all)
# color.uniform([0.88, 0.7, 0.5])
#
#
# beats(152+34, 152+34.3)
# elements(all)
# color.uniform([0.88, 0.7, 0.75])
#
#
# beats(152+34.3, 152+36)
# elements(group4, group8)
# color.uniform([0.675, 1.0, 1.0])
#
# beats(152+34.66, 152+36)
# elements(group2, group6)
# color.uniform([0.675, 1.0, 1.0])
#
# beats(152+35, 152+36)
# elements(group3)
# color.uniform([0.675, 1.0, 1.0])
#
# beats(152+35.33, 152+36)
# elements(group7, group5)
# color.uniform([0.675, 1.0, 1.0])
#
# beats(152+35.66, 152+36)
# elements(group1)
# color.uniform([0.675, 1.0, 1.0])
#
# beats(152+36, 152+37)
# elements(all)
# color.uniform([0.675, 1.0, 0.8])
#
# beats(152+37, 152+38)
# elements(all)
# color.uniform([0.675, 1.0, 0.66])
#
# beats(152+38, 152+39)
# elements(all)
# color.uniform([0.675, 1.0, 0.33])
# effect.fill_out()
#
# beats(152+39, 152+40)
# elements(all)
# cycle(0.25)
# color.gradient(indigo[0], purple_string[0])
# effect.random_brightness()
# effect.hue_shift_steps(4, 0.08)

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
