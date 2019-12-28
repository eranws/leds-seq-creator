from animations import brightness
from animations.brightness import BrightnessAnimation
from animations.fill import FillAnimation
from float_func.const import ConstFloatFunc
from float_func.linear import LinearFloatFunc
from float_func.steps import StepsFloatFunc
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from led_objects.common import no_stands
from led_objects.stars import stars, star7, single_stars
from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.meduza import meduza
from led_objects.cabbages import cabbage1, cabbage6, brain7, cabbage5, cabbages, brains, donut1, donut3, twists, donuts
from led_objects.flood import floods, cup_cakes, cup_cake3, rug4, cup_cake4, rug6, rugs
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, strings, flower1, bottles, papers, paper2, bottle4, bottle5, \
    gloves8, gloves
from led_objects.objects_selector import elements
from led_objects.sheep import sheep
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, lifas, single_lifas, \
    stands, single_stands, sticks
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats, beats_in_episode
from infra.colors import *


def fade_in_parameteric(start_factor=0.0, end_factor=1.0):
    BrightnessAnimation(LinearFloatFunc(start_factor, end_factor)).apply()


def n_episodes(start, end):
    if start >= 3:
        beats(start * 32 + 1, end * 32 + 1)
    else:
        episodes(start, end)


song_settings(bpm=126, beats_per_episode=32, start_offset=3)

# episode 0 start triolas, last 8 beats are different
n_episodes(0, 2.75)
for e in all:
    e.random
elements(bottles, flowers, papers, donuts, stars, twists)
color.uniform(indigo)
effect.brightness(0.5)
cycle(8)
cycle_beats(0, 2)
elements(bottles, paper5)
effect.fill_out_in()
cycle_beats(2, 4)
elements(flowers, paper2)
effect.fill_out_in()
cycle_beats(4, 6)
elements(donuts, stars)
effect.fill_out_in()
cycle_beats(6, 8)
elements(twists)
effect.fill_out_in()

beats(24, 32)
elements(bottles, flowers, papers, donuts, stars, twists)
fade_in_parameteric(1.0, 2.0)

beats(25, 32)
elements(lifas4)
color.gradient(0.61, 0.995)
beats(27, 32)
elements(sticks3)
color.gradient(0.61, 0.995)
beats(29, 32)
elements(sticks7, sticks8, gloves8)
color.gradient(0.61, 0.995)
beats(31, 32)
elements(lifas1, lifas5)
color.gradient(0.61, 0.995)

# Add drum
n_episodes(1, 2.75)
cycle(4)
elements(floods)
color.uniform(red)
effect.saw_tooth()

# blings sequence
beats(59, 70)
elements(lifas4)
color.alternate(indigo, red)
beats(61, 70)
elements(sticks3)
color.alternate(indigo, red)
beats(63, 70)
elements(sticks8, sticks7)
color.alternate(indigo, red)
# additional bling in sequence
beats(63 + 2 / 3, 70)
elements(gloves8, meduza)
color.alternate(indigo, red)
beats(65, 70)
elements(lifas5, lifas1)
color.alternate(indigo, red)

# stop triolas for one beat and static noise
beats(71, 72)
elements(all)
color.uniform(black)

# stretched out background sound
beats(88, 88 + 2/3)
elements(floods)
color.uniform(red)
effect.saw_tooth()
beats(88 + 2/3, 89 + 1/3)
elements(floods)
color.uniform(red)
effect.saw_tooth()
beats(89 + 1/3, 90)
elements(floods)
color.uniform(red)
effect.saw_tooth()
beats(90, 90 + 2/3)
elements(floods)
color.uniform(red)
effect.saw_tooth()

beats(90 + 2/3, 91.5)
elements(floods)
color.uniform(red)
effect.saw_tooth()
beats(91.5, 92.33)
elements(floods)
color.uniform(red)
effect.saw_tooth()
beats(92.33, 93)
elements(floods)
color.uniform(red)
effect.saw_tooth()

beats(93, 93.66)
elements(floods)
color.uniform(red)
effect.saw_tooth()
beats(93.66, 94.5)
elements(floods)
color.uniform(red)
effect.saw_tooth()
beats(94.5, 95.5)
elements(floods)
color.uniform(red)
effect.saw_tooth()
beats(95.5, 96.1)
elements(floods)
color.uniform(red)
effect.saw_tooth()
beats(96.1, 97)
elements(floods)
color.uniform(red)
effect.saw_tooth()


# stretched out bling sequence
beats(89 + 1/11, 100)
elements(lifas4)
color.gradient(0.995, 0.61)

beats(91 + 2/10, 100)
elements(sticks3)
color.gradient(0.995, 0.61)

beats(93 + 4/10, 100)
elements(lifas5)
color.gradient(0.995, 0.61)

beats(95 + 7/10, 100)
elements(sticks7, sticks8)
color.gradient(0.995, 0.61)

beats(96 + 6/10, 100)
elements(gloves8, meduza)
color.gradient(0.995, 0.61)

beats(98, 100)
elements(lifas1, sheep)
color.gradient(0.995, 0.61)

# episode 3, triolas, drum and some specific maps
n_episodes(3, 4)
elements(bottles, flowers, papers, donuts, twists)
color.uniform(turquoise_string)
cycle(8)
cycle_beats(0, 2)
elements(bottles, paper5)
effect.fill_out_in()
cycle_beats(2, 4)
elements(flowers, paper2)
effect.fill_out_in()
cycle_beats(4, 6)
elements(donuts, stars)
effect.fill_out_in()
cycle_beats(6, 8)
elements(twists)
effect.fill_out_in()

# Add drum
n_episodes(3, 4)
cycle(4)
elements(floods)
color.uniform(red)
effect.saw_tooth()

# episode 3 small sounds middle
beats(111.6, 113)
elements(lifas1.stand(1), lifas4.stand(1), lifas5.stand(1), star7.ray(1), star7.ray(7))
color.uniform(white)
beats(112, 113)
elements(lifas1.stand(2), lifas4.stand(2), lifas5.stand(2), star7.ray(2), star7.ray(8))
color.uniform(aquamarine)
beats(112.33, 113)
elements(lifas1.stand(3), lifas4.stand(3), lifas5.stand(3), star7.ray(3), star7.ray(9))
color.uniform(magenta)
beats(112.66, 113)
elements(lifas1.stand(4), lifas4.stand(4), lifas5.stand(4), star7.ray(4), star7.ray(10))
color.uniform(coral)

# episode 3 small sounds end
beats(120, 129)
elements(sticks3.stand(1), sticks7.stand(1), sticks8.stand(1), star7.ray(1), star7.ray(7))
color.uniform(white)
beats(121, 129)
elements(sticks3.stand(2), sticks7.stand(2), sticks8.stand(2), star7.ray(2), star7.ray(8))
color.uniform(aquamarine)
beats(122.33, 128.66)
elements(sticks3.stand(3), sticks7.stand(3), sticks8.stand(3), star7.ray(3), star7.ray(9))
color.uniform(magenta)
beats(123.33, 128)
elements(sticks3.stand(4), sticks7.stand(4), sticks8.stand(4), star7.ray(4), star7.ray(10))
color.uniform(coral)
beats(124, 126)
elements(sticks3.stand(5), sticks7.stand(5), sticks8.stand(5), star7.ray(5), star7.ray(11))
color.uniform(green)

# episode 4 triolas and drum on 2 beats
n_episodes(4, 5)
elements(bottles, flowers, papers, donuts, twists)
color.uniform(purple_strip)
cycle(8)
cycle_beats(0, 2)
elements(bottles, paper5)
effect.fill_out_in()
cycle_beats(2, 4)
elements(flowers, paper2)
effect.fill_out_in()
cycle_beats(4, 6)
elements(donuts)
effect.fill_out_in()
cycle_beats(6, 8)
elements(twists)
effect.fill_out_in()

# Add drum
n_episodes(4, 5)
cycle(1)
elements(floods, stars)
color.uniform(magenta)
effect.saw_tooth()

beats(138, 139)
elements(gloves8, meduza)
color.uniform(green)
beats(144, 145)
elements(lifas4)
color.uniform(green)
beats(146, 147)
elements(sticks3)
color.uniform(green)
beats(154, 163)
elements(lifas4)
color.uniform(green)
beats(156, 163)
elements(sticks3)
color.uniform(green)
beats(158, 163)
elements(lifas1, lifas5)
color.uniform(green)
beats(160, 163)
elements(sticks7, sticks8)
color.uniform(green)
beats(161, 163)
elements(gloves8, sheep)
color.uniform(green)

# episode 5 triolas and drum fades, background increases
n_episodes(5, 6)
elements(bottles, flowers, papers, donuts, twists)
color.uniform(green)
cycle(8)
cycle_beats(0, 2)
elements(bottles, paper5)
effect.fill_out_in()
cycle_beats(2, 4)
elements(flowers, paper2)
effect.fill_out_in()
cycle_beats(4, 6)
elements(donuts)
effect.fill_out_in()
cycle_beats(6, 8)
elements(twists)
effect.fill_out_in()
cycle(None)
elements(bottles, flowers, papers, donuts, twists)
effect.fade_out()

# drum fade
n_episodes(5, 5.25)
cycle(1)
elements(floods)
color.uniform(magenta)
effect.saw_tooth()
cycle(None)
effect.fade_out()

# background fade in
n_episodes(5.25, 5.5)
elements(floods)
color.uniform(dark_green)
effect.fade_in()

# drama pulses fade_in
n_episodes(5.5, 6)
elements(floods)
color.uniform(dark_green)
cycle(2)
cycle_beats(0, 2/3)
effect.saw_tooth()
cycle_beats(2/3, 2)
effect.saw_tooth()
cycle(None)
fade_in_parameteric(1.0, 2.0)

for e in all:
    e.straight

# episode 6 cello triolas
n_episodes(6, 8.875)
elements(bottles, flowers, papers, donuts, stars, twists)
color.uniform(aquamarine)
effect.brightness(0.5)
cycle(8)
cycle_beats(0, 2)
elements(bottles, paper5)
effect.snake()
cycle_beats(2, 4)
elements(flowers, paper2)
effect.snake()
cycle_beats(4, 6)
elements(donuts, stars)
effect.snake()
cycle_beats(6, 8)
elements(twists)
effect.snake()

# n_episodes(6, 6.25)
# elements(bottles, flowers, papers, donuts, stars, twists)
# effect.brightness(0.5)
# effect.fade_in()

# episode 7 add violin1
n_episodes(7, 8.875)
elements(single_lifas)
color.gradient(0.61, 0.995)
effect.brightness(0.5)
cycle(8)
effect.snake_up_down()

# episode 8 add violin2
n_episodes(8, 8.875)
elements(bottles, flowers, papers, donuts, twists)
color.uniform(indigo)
effect.brightness(0.5)
cycle(8)
cycle_beats(0, 2)
elements(bottles, paper5)
effect.snake()
cycle_beats(2, 4)
elements(flowers, paper2)
effect.snake()
cycle_beats(4, 6)
elements(donuts)
effect.snake()
cycle_beats(6, 8)
elements(twists)
effect.snake()

n_episodes(8, 8.875)
elements(single_sticks, single_stars)
color.gradient(0.61, 0.995)
effect.brightness(0.5)
cycle(8)
effect.snake_down_up()

n_episodes(8.5, 8.875)
elements(floods)
color.uniform(indigo)
effect.brightness(0.5)
effect.fade_in()

# big rise for drop
n_episodes(8.875, 9)
elements(all, meduza, sheep)
color.uniform(indigo)
# add the half brightness if we dont want the three rises
# effect.brightness(0.5)
fade_in_parameteric(1.0, 2.0)

# episode 9 drama
n_episodes(9, 9.75)
color.uniform(black)
cycle(4)
cycle_beats(2, 4)
color.uniform(red)
effect.blink_repeat(32)
effect.hue_shift_cycle_diff(0.0, 0.2)
# blinks at end
beats(313, 319)
color.gradient(0.61, 0.995)
effect.blink_repeat(24)
# change blinks a little at the end
beats(317, 319)
effect.hue_shift(-0.2)
effect.brightness(0.5)

# episode 10 triolas come back still with drama
n_episodes(10, 10 + 15/16)
elements(bottles, flowers, papers, lifas, sticks, gloves8)
color.uniform(pink_string)
cycle(8)
cycle_beats(0, 8)
effect.hue_shift_cycle_diff(0.0, 0.2)
cycle_beats(0, 2)
elements(bottles, paper5, lifas4, lifas5, sticks7)
effect.snake()
cycle_beats(4, 6)
elements(flowers, paper2, lifas1, sticks3, sticks8, gloves8)
effect.snake()

# drama every 2 for 2 cycles
beats_in_episode(10, 3, 5)
elements(twists)
color.uniform(turquoise_strip)
effect.blink_repeat(64)
beats_in_episode(10, 7, 9)
elements(stars)
color.uniform(turquoise_strip)
effect.fade_out()
beats_in_episode(10, 11, 13)
elements(donuts)
color.uniform(turquoise_strip)
effect.snake()
beats_in_episode(10, 15, 17)
elements(floods)
color.uniform(turquoise_strip)
effect.fill()
beats_in_episode(10, 19, 21)
elements(twists)
color.uniform(turquoise_strip)
effect.snake()
beats_in_episode(10, 23, 25)
elements(stars)
color.uniform(turquoise_strip)
effect.blink()

# end of episode blinks
elements(twists,stars, donuts, floods, meduza, sheep)
beats(345, 351)
color.gradient(0.61, 0.995)
effect.blink_repeat(64)

beats(349, 351)
effect.hue_shift(-0.2)
effect.brightness(0.5)

beats(351, 353)
elements(all, meduza, sheep)
color.uniform(aquamarine)
effect.brightness(0.7)
effect.fade_in()

# episode 11
# bass drum
n_episodes(11, 11 + 7/8)
elements(star7)
color.uniform(red)
cycle(2)
effect.saw_tooth()

# background
n_episodes(11, 12)
elements(strings)
cycle(8)
color.uniform(aquamarine)
effect.breath(0.4)
effect.hue_shift_cycle_diff(0.0, 0.05)

# blings
n_episodes(11, 13)
cycle(4)
cycle_beats(0, 0.66)
elements([lifas1.stand(5), lifas5.stand(5), sticks3.stand(5), sticks7.stand(5), sticks8.stand(5)])
color.gradient(0.6, 1.0)
effect.saw_tooth(1.0)

cycle_beats(1, 1.66)
elements([lifas1.stand(1), lifas4.stand(1), lifas5.stand(1), lifas1.stand(3), lifas4.stand(3), lifas5.stand(3)])
color.gradient(0.4, 0.8)
effect.saw_tooth(1.0)

cycle_beats(1.33, 2.0)
elements([sticks3.stand(2), sticks7.stand(2), sticks8.stand(2), sticks3.stand(4), sticks7.stand(4), sticks8.stand(4)])
color.gradient(0.4, 0.8)
effect.saw_tooth(1.0)

cycle_beats(2, 2.66)
elements([lifas1.stand(5), lifas5.stand(5), sticks3.stand(5), sticks7.stand(5), sticks8.stand(5)])
color.gradient(0.6, 1.0)
effect.saw_tooth(1.0)

cycle_beats(3, 3.66)
elements([lifas1.stand(2), lifas4.stand(2), lifas5.stand(2), lifas1.stand(4), lifas4.stand(4), lifas5.stand(4)])
color.gradient(0.4, 0.8)
effect.saw_tooth(1.0)

cycle_beats(3.33, 4.0)
elements([sticks3.stand(1), sticks7.stand(1), sticks8.stand(1), sticks3.stand(3), sticks7.stand(3), sticks8.stand(3)])
color.gradient(0.4, 0.8)
effect.saw_tooth(1.0)

elements(stands)
effect.hue_shift_cycle_diff(0.0, 0.2)

beats_in_episode(11, 30, 31)
elements(gloves8)
color.gradient(0.4, 0.8)
effect.saw_tooth()

# end of episode blinks
elements(floods, twists)
beats_in_episode(11, 25, 33)
color.gradient(0.4, 0.8)
effect.blink_repeat(64)

beats_in_episode(11, 29, 33)
effect.hue_shift(-0.2)
# effect.brightness(0.5)

# episode 12 similar to 11 but with a few diffs
# background
n_episodes(12, 13)
elements(strings)
cycle(8)
color.uniform(indigo)
effect.snake()
effect.hue_shift_cycle_diff(0.0, 0.1)
# bass drum
n_episodes(12, 13)
elements(star7)
color.uniform(purple_strip)
cycle(2)
effect.saw_tooth()

# end of episode blinks
elements(floods, twists)
beats_in_episode(12, 25, 33)
color.gradient(0.1, 0.3)
effect.blink_repeat(32)

beats_in_episode(12, 29, 33)
effect.hue_shift(-0.2)
# effect.brightness(0.5)

beats_in_episode(12, 30, 31)
elements(gloves8, meduza)
color.gradient(0.4, 0.8)
effect.saw_tooth()


# episode 13 things change
# blings now on rugs, cabbages and cupcakes
n_episodes(13, 16)
cycle(4)
cycle_beats(0, 0.66)
elements(rugs)
color.gradient(0.6, 1.0)
effect.saw_tooth(1.0)

cycle_beats(1, 1.66)
elements(cabbages)
color.gradient(0.4, 0.8)
effect.saw_tooth(1.0)

cycle_beats(1.33, 2.0)
elements(cup_cakes)
color.gradient(0.4, 0.8)
effect.saw_tooth(1.0)

cycle_beats(2, 2.66)
elements(rugs)
color.gradient(0.6, 1.0)
effect.saw_tooth(1.0)

cycle_beats(3, 3.66)
elements(cup_cakes)
color.gradient(0.4, 0.8)
effect.saw_tooth(1.0)

cycle_beats(3.33, 4.0)
elements(cabbages)
color.gradient(0.4, 0.8)
effect.saw_tooth(1.0)

cycle(4)
elements(rugs, cup_cakes, cabbages)
effect.hue_shift_cycle_diff(0.0, 0.2)
effect.brightness(0.5)

# triolas again
n_episodes(13, 16)
for e in all:
    e.random
elements(bottles, flowers, papers, donuts)
color.gradient(0.6, 1.0)
effect.brightness(0.5)
cycle(8)
effect.hue_shift_cycle_diff(0.0, 0.2)
cycle_beats(0, 2)
elements(bottles)
effect.fill_out_in()
cycle_beats(2, 4)
elements(flowers)
effect.fill_out_in()
cycle_beats(4, 6)
elements(donuts)
effect.fill_out_in()
cycle_beats(6, 8)
elements(papers)
effect.fill_out_in()

# episode 14
# enter low violin
n_episodes(14, 15)
elements(stars, brains, gloves, meduza, sheep)
color.uniform(dark_blue)
cycle(2)
effect.brightness(0.5)
effect.saw_tooth()
effect.hue_shift_cycle_diff(0.0, 0.01)

# episode 15
# enter high violin
n_episodes(15, 16 + 15/16)
elements(single_stands)
color.gradient(0.7, 0.9)
cycle(2)
effect.brightness(0.5)
effect.saw_tooth()
effect.fill_out_in()
effect.hue_shift_cycle_diff(0.0, 0.01)

# episode 16
# enter second triola
n_episodes(16, 16 + 15/16)
elements(no_stands)
color.gradient(0.8, 1.0)
effect.brightness(0.5)
cycle(8)
effect.hue_shift_cycle_diff(0.0, 0.04)
cycle_beats(0, 2)
elements(bottles, brains, cabbages)
effect.fill_out_in()
cycle_beats(2, 4)
elements(flowers, gloves, rugs)
effect.fill_out_in()
cycle_beats(4, 6)
elements(donuts, stars)
effect.fill_out_in()
cycle_beats(6, 8)
elements(papers, cup_cakes)
effect.fill_out_in()

# background increasing to explosion at end of episode
n_episodes(16.5, 16 + 15/16)
elements(all)
fade_in_parameteric(1.0, 1.5)

beats_in_episode(16, 31, 33)
color.uniform(red)
effect.fade_in()

# episodes 17, 18 drama
n_episodes(17, 17 + 15/16)
cycle(4)
cycle_beats(0, 2)
elements(no_stands, meduza, sheep)
color.uniform(yellow_strip)
effect.blink_repeat(32)
cycle_beats(2, 4)
elements(single_stands)
color.gradient(0.2, 0.4)

elements(single_stands)
cycle(8)
cycle_beats(2, 4)
FillAnimation(ConstFloatFunc(0.0), StepsFloatFunc(6, 1/6, 1/6)).apply()
cycle_beats(6, 8)
FillAnimation(ConstFloatFunc(0.0), StepsFloatFunc(6, -1/6, 1)).apply()

cycle(4)
elements(all, meduza, sheep)
effect.hue_shift_cycle_diff(0.0, 0.2)

n_episodes(17 + 15/16, 18)
elements(single_stands)
color.gradient(0.6, 0.8)
effect.blink_repeat(3)

n_episodes(18, 18 + 15/16)
cycle(4)
cycle_beats(0, 2)
elements(no_stands, meduza, sheep)
color.uniform(yellow_strip)
effect.blink_repeat(32)
cycle_beats(2, 4)
elements(single_stands)
color.gradient(0.2, 0.4)

elements(single_stands)
cycle(8)
cycle_beats(2, 4)
FillAnimation(ConstFloatFunc(0.0), StepsFloatFunc(6, 1/6, 1/6)).apply()
cycle_beats(6, 8)
FillAnimation(ConstFloatFunc(0.0), StepsFloatFunc(6, -1/6, 1)).apply()

cycle(4)
elements(all, meduza, sheep)
effect.hue_shift_cycle_diff(0.0, 0.2)

n_episodes(18 + 15/16, 19)
elements(single_stands)
color.gradient(0.6, 0.8)
effect.blink_repeat(3)

# episode 19 start fade out until 20.5
n_episodes(19, 20.5)
elements(no_stands, meduza, sheep)
color.uniform(red)
BrightnessAnimation(StepsFloatFunc(12, -1/12, 1)).apply()
cycle(4)
effect.hue_shift_cycle_target(0, indigo[0])

n_episodes(19, 20.5)
elements(single_stands)
color.gradient(0.2, 0.4)
cycle(4)
cycle_beats(0, 2)
FillAnimation(ConstFloatFunc(0.0), StepsFloatFunc(3, 1/3, 1/3)).apply()
cycle_beats(2, 4)
FillAnimation(ConstFloatFunc(0.0), StepsFloatFunc(3, -1/3, 1)).apply()
cycle(4)
effect.hue_shift_cycle_diff(0.0, 0.02)

# episode 20.5 fade, only slowing down blings
beats(658, 662.5)
elements(group1, group2)
color.gradient(0.2, 0.4)

beats(658.66, 663.2)
elements(group3, group8)
color.gradient(0.2, 0.4)

beats(660.1, 664.9)
elements(group4, group7)
color.gradient(0.2, 0.4)

beats(660.9, 665.8)
elements(group5, group6)
color.gradient(0.2, 0.4)

beats(667.5, 673.8)
elements(group1, group2)
color.gradient(0.2, 0.4)

beats(668.5, 675)
elements(group3, group8)
color.gradient(0.2, 0.4)

beats(670.5, 677.5)
elements(group4, group7)
color.gradient(0.2, 0.4)

beats(671.5, 678.8)
elements(group5, group6)
color.gradient(0.2, 0.4)

# episode 21 slowing blings continue and fin!
# give an extra touch to a different bling towards the end
beats(673.8, 675)
elements(meduza, sheep)
color.gradient(0.2, 0.4)

# final bling is meduza and kivsi only
beats(681.5, 686)
elements(meduza)
color.uniform(indigo)

elements(sheep)
color.uniform(white)


send_to_mqtt("nikki")
start_song("nikki", 0)
