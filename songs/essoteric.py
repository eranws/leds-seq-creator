from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.flood import cup_cakes, cup_cake3, rug4, rug6, rugs
from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles, paper2, flower1, bottle4, bottle5
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands, \
    single_lifas
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=73.5, beats_per_episode=16, start_offset=3)

def yellowopening():

    elements(group5)
    cycle(beats=16)
    cycle_beats(0, 3)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group1)
    cycle(beats=16)
    cycle_beats(2, 5)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group6)
    cycle(beats=16)
    cycle_beats(4, 7)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group2)
    cycle(beats=16)
    cycle_beats(6, 9)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group4)
    cycle(beats=16)
    cycle_beats(8, 11)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group7)
    cycle(beats=16)
    cycle_beats(10, 14)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group3)
    cycle(beats=16)
    cycle_beats(12, 16)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group8)
    cycle(beats=16)
    cycle_beats(14, 16)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

episode(0)
yellowopening()

def coloropening():
    elements(cabbages)
    cycle(beats=16)
    cycle_beats(0.0, 0.74)
    color.uniform(coral)
    effect.breath(0.4)
    cycle_beats(0.74, 16)
    color.uniform(coral)
    effect.saw_tooth(1.0, False)

    elements(sticks)
    cycle(beats=16)
    cycle_beats(2.0, 2.74)
    color.uniform(pink_strip)
    effect.breath(0.4)
    cycle_beats(2.74, 16)
    color.uniform(magenta)
    effect.saw_tooth(1.0, False)

    elements(flowers)
    cycle(beats=16)
    cycle_beats(4, 4.74)
    color.uniform((0.03, 1.0, 1.0))
    effect.breath(0.4)
    cycle_beats(4.74, 16)
    color.uniform((0.05, 1.0, 1.0))
    effect.saw_tooth(1.0, False)

    elements(brains)
    cycle(beats=16)
    cycle_beats(6, 6.74)
    color.uniform((0.995, 0.85, 1.0))
    effect.breath(0.4)
    cycle_beats(6.74, 16)
    color.uniform((0.995, 0.85, 1.0))
    effect.saw_tooth(1.0, False)

    elements(donuts)
    cycle(beats=16)
    cycle_beats(6, 6.74)
    color.uniform(light_coral)
    effect.breath(0.4)
    cycle_beats(6.74, 16)
    color.uniform(light_coral)
    effect.saw_tooth(1.0, False)

    elements(bottles)
    cycle(beats=16)
    cycle_beats(8, 8.74)
    color.uniform(magenta)
    effect.breath(0.4)
    cycle_beats(8.74 , 16)
    color.uniform(pink_string)
    effect.saw_tooth(1.0, False)

    elements(cup_cakes)
    cycle(beats=16)
    cycle_beats(10, 10.74)
    color.uniform((0.80, 1.0, 1.0))
    effect.breath(0.4)
    cycle_beats(10.74, 16)
    color.uniform((0.80, 1.0, 1.0))
    effect.saw_tooth(1.0, False)

    elements(lifas)
    cycle(beats=16)
    cycle_beats(12, 12.74)
    color.uniform(red)
    effect.breath(0.4)
    cycle_beats(12.74, 16)
    color.uniform(red)
    effect.saw_tooth(1.0, False)

    elements(papers)
    cycle(beats=16)
    cycle_beats(14, 14.74)
    color.uniform((0.03, 1.0, 0.8))
    effect.breath(0.4)
    cycle_beats(14.74, 16)
    color.uniform((0.03, 1.0, 0.8))
    effect.saw_tooth(1.0, False)

    elements(rugs)
    cycle(beats=16)
    cycle_beats(14, 14.74)
    color.uniform(coral)
    effect.breath(0.4)
    cycle_beats(14.74, 16)
    color.uniform(coral)
    effect.saw_tooth(1.0, False)

episode(1)
coloropening()

# episode(1)
# effect.blink(0.4)
# cycle(1)
def clapping(clapping_lights):

    elements(clapping_lights)
    cycle(beats=2)

    cycle_beats(1.0, 1.37)
    effect.saw_tooth(0.2, False)
    color.uniform(coral)

    cycle_beats(1.37, 1.67)
    effect.saw_tooth(0.2, False)
    color.uniform((0.995, 0.9, 1.0))

    cycle_beats(1.67, 2.0)
    effect.snake(0.2)
    color.uniform((0.995, 0.75, 0.4))

episode(2)
clapping(all)

def light_stick_on_note(stick_to_light, g1, g2, stand_index, b_start, b_end):

    if stick_to_light.num_of_sticks > 4:
        note_to_stand = {1:1, 2:2, 3:3, 4:4, 5:5}
    else:
        note_to_stand = {1:1, 2:2, 3:3, 4:4, 5:1}

    elements(stick_to_light.stand(note_to_stand[stand_index]))
    cycle(beats=8)
    cycle_beats(b_start, b_end)
    color.gradient(g1, g2)
    effect.snake(1.0, True)

def violin1(stick_to_light, g1, g2):
    light_stick_on_note(stick_to_light, g1, g2, 3, 0.0, 0.85)
    light_stick_on_note(stick_to_light, g1, g2, 1, 0.55, 1.3)
    light_stick_on_note(stick_to_light, g1, g2, 2, 1.0, 2.05)
    light_stick_on_note(stick_to_light, g1, g2, 5, 1.75, 2.37)
    light_stick_on_note(stick_to_light, g1, g2, 2, 2.07, 2.78)
    light_stick_on_note(stick_to_light, g1, g2, 4, 2.48, 3.3)
    light_stick_on_note(stick_to_light, g1, g2, 3, 3.0, 3.85)
    light_stick_on_note(stick_to_light, g1, g2, 4, 3.55, 4.3)
    light_stick_on_note(stick_to_light, g1, g2, 2, 4.0, 4.8)
    light_stick_on_note(stick_to_light, g1, g2, 1, 4.5, 5.3)
    light_stick_on_note(stick_to_light, g1, g2, 2, 5.0, 6.01)
    light_stick_on_note(stick_to_light, g1, g2, 5, 5.71, 6.37)
    light_stick_on_note(stick_to_light, g1, g2, 3, 6.07, 6.9)
    light_stick_on_note(stick_to_light, g1, g2, 2, 6.6, 7.3)
    light_stick_on_note(stick_to_light, g1, g2, 4, 7.0, 8.0)



def light_lifa_on_note(lifa_to_light, g1, g2, stand_index, b_start, b_end):

    if lifa_to_light.num_of_sticks > 4:
        note_to_stand = {1:1, 2:2, 3:3, 4:4, 5:5}
    else:
        note_to_stand = {1:1, 2:2, 3:3, 4:4, 5:1}

    elements(lifa_to_light.stand(note_to_stand[stand_index]))
    cycle(beats=8)
    cycle_beats(b_start, b_end)
    color.gradient(g1, g2)
    effect.snake(1.0, True)


def violin2(lifa_to_light, g1, g2):

    light_lifa_on_note(lifa_to_light, g1, g2, 3, 0.0, 0.85)
    light_lifa_on_note(lifa_to_light, g1, g2, 1, 0.55, 1.3)
    light_lifa_on_note(lifa_to_light, g1, g2, 2, 1.0, 1.85)
    light_lifa_on_note(lifa_to_light, g1, g2, 5, 1.55, 2.37)
    light_lifa_on_note(lifa_to_light, g1, g2, 2, 2.07, 2.78)
    light_lifa_on_note(lifa_to_light, g1, g2, 4, 2.48, 3.3)
    light_lifa_on_note(lifa_to_light, g1, g2, 3, 3.0, 3.85)
    light_lifa_on_note(lifa_to_light, g1, g2, 4, 3.55, 4.3)
    light_lifa_on_note(lifa_to_light, g1, g2, 2, 4.0, 4.85)
    light_lifa_on_note(lifa_to_light, g1, g2, 1, 4.55, 5.3)
    light_lifa_on_note(lifa_to_light, g1, g2, 2, 5.0, 5.85)
    light_lifa_on_note(lifa_to_light, g1, g2, 5, 5.55, 6.37)
    light_lifa_on_note(lifa_to_light, g1, g2, 3, 6.07, 6.85)
    light_lifa_on_note(lifa_to_light, g1, g2, 2, 6.55, 7.3)
    light_lifa_on_note(lifa_to_light, g1, g2, 4, 7.0, 8.0)



episodes(3, 7)
violin1(sticks3, 0.035, yellow_strip[0])

episodes(4, 7)
violin1(sticks8, 0.035, yellow_strip[0])

episodes(4, 7)
violin1(sticks7, 0.035, yellow_strip[0])

episodes(5, 7)
violin2(lifas5, purple_strip[0], indigo[0])
violin2(lifas1, purple_strip[0], indigo[0])
violin2(lifas4, purple_strip[0], indigo[0])


episodes(5, 7)
cycle(8)
elements(flowers, cabbages, cup_cakes,papers, donuts)
color.uniform((0.11, 0.8, 0.4))
effect.breath(0.8)




def small_bit():
    effect.hue_breath(0.4)

    elements(flower6)
    beats((16 * 7) + 0.12, (16*7) + 32)
    color.uniform(red)

    elements(cabbage1)
    beats((16*7) +0.5, (16*7) + 32)
    color.uniform(aquamarine)

    elements(lifas5.stand(3), lifas5.stand(5))
    beats((16*7) +1.0, (16*7) + 32)
    color.uniform(blue)

    elements(cup_cake4)
    beats((16*7) +1.37, (16*7) + 32)
    color.uniform(purple_string)

    elements(lifas4.stand(4))
    beats((16*7) +1.75, (16*7) + 32)
    color.uniform(yellow_string)

    elements(paper2)
    beats((16*7) +2.0, (16*7) + 32)
    color.uniform(orange_string)

    elements(lifas5.stand(2))
    beats((16*7) +2.55, (16*7) + 32)
    color.uniform(light_blue)

    elements(donut3)
    beats((16*7) +3.0, (16*7) + 32)
    color.uniform(light_green)

    elements(cabbage5)
    beats((16*7) +3.34, (16*7) + 32)
    color.uniform(coral)

    elements(sticks7.stand(1))
    beats((16*7) +3.66, (16*7) + 32)
    color.uniform(blue)

    elements(flower1)
    beats((16*7) +4.12, (16*7) + 32)
    color.uniform(light_purple_string)

    elements(bottle4)
    beats((16*7) +4.5, (16*7) + 32)
    color.uniform(aquamarine)

    elements(sticks8.stand(2))
    beats((16*7) +5.0, (16*7) + 32)
    color.uniform((0.87, 1.0, 1.0))

    elements(cup_cake3)
    beats((16*7) +5.37, (16*7) + 32)
    color.uniform(light_pink_strip)

    elements(lifas1.stand(3))
    beats((16*7) +5.75, (16*7) + 32)
    color.uniform(light_turquoise_string)

    elements(sticks3.stand(3))
    beats((16*7) +6.0, (16*7) + 32)
    color.uniform(light_orange_strip)

    elements(lifas5.stand(1))
    beats((16*7) +6.55, (16*7) + 32)
    color.uniform(light_blue)

    elements(lifas4.stand(2))
    beats((16*7) +7.0, (16*7) + 32)
    color.uniform(yellow_strip)

    elements(rug4)
    beats((16*7) +7.34, (16*7) + 32)
    color.uniform(coral)

    elements(sticks7. stand(2))
    beats((16*7) +7.66, (16*7) + 32)
    color.uniform(blue)

    elements(bottle5)
    beats((16*7) +8.12, (16*7) + 32)
    color.uniform(magenta)

    elements(lifas5.stand(4))
    beats((16*7) +8.5, (16*7) + 32)
    color.uniform(dark_blue)

    elements(lifas1.stand(5))
    beats((16*7) +9.0, (16*7) + 32)
    color.uniform(light_turquoise_string)

    elements(sticks7.stand(6))
    beats((16*7) +9.37, (16*7) + 32)
    color.uniform(blue)

    elements(rug6)
    beats((16*7) +9.75, (16*7) + 32)
    color.uniform(turquoise_string)

    elements(sticks3.stand(1))
    beats((16*7) +10.0, (16*7) + 32)
    color.uniform(orange_string)

    elements(brain7)
    beats((16*7) +10.55, (16*7) + 32)
    color.uniform(blue)

    elements(paper5)
    beats((16*7) +11.0, (16*7) + 32)
    color.uniform(light_green)

    elements(sticks8.stand(4))
    beats((16*7) +11.34, (16*7) + 32)
    color.uniform((0.9, 1.0, 1.0))

    elements([sticks7.stand(2), sticks7.stand(4)])
    beats((16*7) +11.66, (16*7) + 32)
    color.uniform(dark_blue)

    elements(lifas4.stand(1))
    beats((16*7) +12.12, (16*7) + 32)
    color.uniform(yellow_string)

    elements(sticks3.stand(2))
    beats((16*7) +12.5, (16*7) + 32)
    color.uniform(orange_string)

    elements(lifas1.stand(2))
    beats((16*7) +13.0, (16*7) + 32)
    color.uniform(turquoise_strip)

    elements([sticks7.stand(3), sticks7.stand(5)])
    beats((16*7) +13.37, (16*7) + 32)
    color.uniform(light_blue)

    elements([sticks8.stand(3), sticks8.stand(5)])
    beats((16*7) +13.75, (16*7) + 32)
    color.uniform(magenta)

    elements(donut1)
    beats((16*7) +14.0, (16*7) + 32)
    color.uniform(yellow_string)

    elements(sticks3.stand(5), sticks3.stand(4))
    beats((16*7) +14.55, (16*7) + 32)
    color.uniform(orange_strip)

    elements([lifas1.stand(1), lifas1.stand(4)])
    beats((16*7) +15.0, (16*7) + 32)
    color.uniform(turquoise_string)

    elements(sticks8.stand(1))
    beats((16*7) +15.34, (16*7) + 32)
    color.uniform((0.87, 1.0, 1.0))

    elements(lifas4.stand(3))
    beats((16*7) +15.66, (16*7) + 32.0)
    color.uniform(yellow_strip)

episodes(7, 9)
small_bit()

episode(8)
cycle(2)
elements(all)
effect.hue_saw_tooth(0.4, True)

beats(142, 143)
effect.snake(0.5)

beats(143, 144)
elements(all)
color.gradient(red[0], orange_strip[0])
effect.saw_tooth(total)





def quickgroupcolorchange():
    cycle(4)
    effect.breath(0.1)

    cycle_beats(0.0, 0.5)
    elements(group3)
    color.alternate(pink_strip, purple_strip, 5)

    cycle_beats(0.50, 1.0)
    elements(group6)
    color.alternate(indigo, magenta, 5)


    cycle_beats(1.0, 1.5)
    elements(group1)
    color.alternate(green, yellow_string, 5)

    cycle_beats(1.5, 2.0)
    elements(group4)
    color.alternate(red, purple_strip, 5)

    cycle_beats(2.0, 2.5)
    elements(group8)
    color.alternate(aquamarine, dark_blue, 5)

    cycle_beats(2.5, 3.0)
    elements(group5)
    color.alternate(orange_strip, magenta, 5)

    cycle_beats(3.0, 3.5)
    elements(group2)
    color.alternate(turquoise_string, purple_strip, 5)

    cycle_beats(3.5, 4.0)
    elements(group7)
    color.alternate(coral, yellow_string, 5)


episode(9)
quickgroupcolorchange()

episode(9)
cycle(4)
elements(all)
effect.hue_breath(0.1)


episode(10)

cycle(0.5)
elements(all)
color.gradient(blue[0], aquamarine[0])
effect.breath(soft)



cycle(beats=8)
cycle_beats(0.0, 0.5)
elements(cup_cakes)
color.gradient(0.78, 0.9)
effect.breath(0.8)

cycle_beats(0.5, 1.0)
elements(cup_cakes)
effect.breath(0.8)
color.gradient(0.78, 0.9)


cycle_beats(1.0, 1.5)
elements(donuts)
color.gradient(0.78, 0.9)
effect.breath(0.8)

cycle_beats(1.5, 2.0)
elements(donuts)
color.gradient(0.78, 0.9)
effect.breath(0.8)

cycle_beats(2.0, 2.5)
elements(rug4, rug6)
color.gradient(0.78, 0.9)
effect.breath(0.8)

cycle_beats(2.5, 2.9)
elements(rug4,rug6)
color.gradient(0.78, 0.9)
effect.breath(0.8)

cycle_beats(2.9, 4.1)
elements(cabbages, single_sticks)
color.gradient(0.78, 0.9)
effect.breath(0.8)

cycle_beats(4.0, 4.5)
elements(cup_cakes)
color.gradient(0.78, 0.9)
effect.breath(0.8)

cycle_beats(4.5, 5.0)
elements(cup_cakes)
color.gradient(0.78, 0.9)
effect.breath(0.8)

cycle_beats(5.0, 5.5)
elements(bottles)
color.gradient(0.78, 0.9)
effect.breath(0.8)

cycle_beats(5.5, 6.0)
elements(bottles)
color.gradient(0.78, 0.9)
effect.breath(0.8)

cycle_beats(6.0, 7.0)
elements(cabbages, papers, single_sticks)
color.gradient(0.78, 0.9)
effect.breath(0.8)

cycle_beats(7.0, 8.0)
elements(papers,cabbages, single_sticks)
color.gradient(0.78, 0.9)
effect.breath(0.8)


# def wave():
#     cycle(1)
#
#     elements(flower1)
#     cycle_beats(0.0, 0.025)
#     effect.breath(0.1)
#     color.uniform(aquamarine)
#
#     elements(lifas1, cabbage1)
#     cycle_beats(0.025, 0.05)
#     effect.breath(0.1)
#     color.uniform(aquamarine)
#
#     elements(donut1)
#     cycle_beats(0.05, 0.075)
#     effect.breath(0.1)
#     color.uniform(aquamarine)
#
#     elements(sticks8, paper2, flower6)
#     cycle_beats(0.075, 0.1)
#     effect.breath(0.1)
#     color.uniform(aquamarine)
#
#     elements(cup_cake3, cabbage6, rug6)
#     cycle_beats(0.1, 0.125)
#     effect.breath(0.1)
#     color.uniform(aquamarine)
#
#     elements(sticks3, donut3, brain7)
#     cycle_beats(0.125, 0.15)
#     effect.breath(0.1)
#     color.uniform(aquamarine)
#
#     elements(sticks7, lifas4, rug4)
#     cycle_beats(0.15, 0.175)
#     effect.breath(0.1)
#     color.uniform(aquamarine)
#
#     elements(paper5)
#     cycle_beats(0.175, 0.2)
#     effect.breath(0.1)
#     color.uniform(aquamarine)
#
#     elements(cabbage6, bottle5)
#     cycle_beats(0.2, 0.225)
#     effect.breath(0.1)
#     color.uniform(aquamarine)
#
#     elements(paper5, lifas5, bottle5)
#     cycle_beats(0.225, 0.25)
#     effect.breath(0.1)
#     color.uniform(aquamarine)
#
#     elements(cabbage6, bottle5)
#     cycle_beats(0.275, 0.3)
#     effect.breath(0.1)
#     color.uniform(green)
#
#     elements(paper5)
#     cycle_beats(0.3, 0.325)
#     effect.breath(0.1)
#     color.uniform(green)
#
#     elements(sticks7, lifas4, rug4)
#     cycle_beats(0.325, 0.35)
#     effect.breath(0.1)
#     color.uniform(green)
#
#     elements(sticks3, donut3, brain7)
#     cycle_beats(0.35, 0.375)
#     effect.breath(0.1)
#     color.uniform(green)
#
#     elements(cup_cake3, cabbage6, rug6)
#     cycle_beats(0.375, 0.4)
#     effect.breath(0.1)
#     color.uniform(green)
#
#     elements(sticks8, paper2, flower6)
#     cycle_beats(0.4, 0.425)
#     effect.breath(0.1)
#     color.uniform(green)
#
#     elements(donut1)
#     cycle_beats(0.425, 0.45)
#     effect.breath(0.1)
#     color.uniform(green)
#
#     elements(lifas1, cabbage1)
#     cycle_beats(0.45, 0.475)
#     effect.breath(0.1)
#     color.uniform(green)
#
#     elements(flower1)
#     cycle_beats(0.475, 0.5)
#     effect.breath(0.1)
#     color.uniform(green)



def full_wave():
    cycle(0.5)

    elements(flower1)
    cycle_beats(0.0, 0.47)
    effect.breath(0.1)
    color.uniform(aquamarine)

    elements(lifas1, cabbage1)
    cycle_beats(0.025, 0.47)
    effect.breath(0.1)
    color.uniform(aquamarine)

    elements(donut1)
    cycle_beats(0.05, 0.47)
    effect.breath(0.1)
    color.uniform(aquamarine)

    elements(sticks8, paper2, flower6)
    cycle_beats(0.075, 0.47)
    effect.breath(0.1)
    color.uniform(aquamarine)

    elements(cup_cake3, cabbage6, rug6)
    cycle_beats(0.1, 0.47)
    effect.breath(0.1)
    color.uniform(aquamarine)

    elements(sticks3, donut3, brain7)
    cycle_beats(0.125, 0.47)
    effect.breath(0.1)
    color.uniform(aquamarine)

    elements(sticks7, lifas4, rug4)
    cycle_beats(0.15, 0.47)
    effect.breath(0.1)
    color.uniform(aquamarine)

    elements(paper5)
    cycle_beats(0.175, 0.47)
    effect.breath(0.1)
    color.uniform(aquamarine)

    elements(cabbage6, bottle5)
    cycle_beats(0.2, 0.47)
    effect.breath(0.1)
    color.uniform(aquamarine)

    elements(paper5, lifas5, bottle5)
    cycle_beats(0.225, 0.47)
    effect.breath(0.1)
    color.uniform(aquamarine)

    elements(cabbage6, bottle5)
    cycle_beats(0.25, 0.47)
    effect.breath(0.1)
    color.uniform(aquamarine)

    elements(paper5)
    cycle_beats(0.275, 0.47)
    effect.breath(0.1)
    color.uniform(aquamarine)

    elements(sticks7, lifas4, rug4)
    cycle_beats(0.3, 0.47)
    effect.breath(0.1)
    color.uniform(aquamarine)

    elements(sticks3, donut3, brain7)
    cycle_beats(0.325, 0.47)
    effect.breath(0.1)
    color.uniform(aquamarine)

    elements(cup_cake3, cabbage6, rug6)
    cycle_beats(0.35, 0.47)
    effect.breath(0.1)
    color.uniform(aquamarine)

    elements(sticks8, paper2, flower6)
    cycle_beats(0.375, 0.47)
    effect.breath(0.1)
    color.uniform(aquamarine)

    elements(donut1)
    cycle_beats(0.4, 0.47)
    effect.breath(0.1)
    color.uniform(aquamarine)

    elements(lifas1, cabbage1)
    cycle_beats(0.425, 0.47)
    effect.breath(0.1)
    color.uniform(aquamarine)


episode(11)
full_wave()
cycle(8)

beats(176, 192)
cycle(8)
elements(all)
effect.hue_breath(medium)

beats(184, 192)
elements(cabbages, brains,lifas)
color.uniform(orange_strip)
effect.snake(0.6)

beats(186, 192)
elements(sticks, flowers, cup_cakes)
color.uniform(orange_strip)
effect.snake(0.6)

beats(188, 192)
elements(papers, bottles, rugs, donuts)
color.uniform(orange_strip)
effect.snake(0.6)


# episode(11)
# cycle(16)
# elements(all)
# effect.saw_tooth(total, False)

def light_stick_on_note_end(stick_to_light, c, stand_index, b_start, b_end):

    if stick_to_light.num_of_sticks > 4:
        note_to_stand = {1:1, 2:2, 3:3, 4:4, 5:5}
    else:
        note_to_stand = {1:1, 2:2, 3:3, 4:4, 5:1}

    elements(stick_to_light.stand(note_to_stand[stand_index]))
    cycle(beats=8)
    cycle_beats(b_start, b_end)
    color.uniform(c)
    effect.snake(1.0, True)

def violin1end(stick_to_light, c):
    light_stick_on_note_end(stick_to_light, c, 3, 0.0, 0.85)
    light_stick_on_note_end(stick_to_light, c, 1, 0.55, 1.3)
    light_stick_on_note_end(stick_to_light, c, 2, 1.0, 2.05)
    light_stick_on_note_end(stick_to_light, c, 5, 1.75, 2.37)
    light_stick_on_note_end(stick_to_light, c, 2, 2.07, 2.78)
    light_stick_on_note_end(stick_to_light, c, 4, 2.48, 3.3)
    light_stick_on_note_end(stick_to_light, c, 3, 3.0, 3.85)
    light_stick_on_note_end(stick_to_light, c, 4, 3.55, 4.3)
    light_stick_on_note_end(stick_to_light, c, 2, 4.0, 4.8)
    light_stick_on_note_end(stick_to_light, c, 1, 4.5, 5.3)
    light_stick_on_note_end(stick_to_light, c, 2, 5.0, 6.01)
    light_stick_on_note_end(stick_to_light, c, 5, 5.71, 6.37)
    light_stick_on_note_end(stick_to_light, c, 3, 6.07, 6.9)
    light_stick_on_note_end(stick_to_light, c, 2, 6.6, 7.3)
    light_stick_on_note_end(stick_to_light, c, 4, 7.0, 8.0)


def light_lifa_on_note(lifa_to_light, c, stand_index, b_start, b_end):

    if lifa_to_light.num_of_sticks > 4:
        note_to_stand = {1:1, 2:2, 3:3, 4:4, 5:5}
    else:
        note_to_stand = {1:1, 2:2, 3:3, 4:4, 5:1}

    elements(lifa_to_light.stand(note_to_stand[stand_index]))
    cycle(beats=8)
    cycle_beats(b_start, b_end)
    color.uniform(c)
    effect.snake(1.0, True)

def violin2end (lifa_to_light, c):


        light_lifa_on_note(lifa_to_light, c, 3, 0.0, 0.85)
        light_lifa_on_note(lifa_to_light, c, 1, 0.55, 1.3)
        light_lifa_on_note(lifa_to_light, c, 2, 1.0, 1.85)
        light_lifa_on_note(lifa_to_light, c, 5, 1.55, 2.37)
        light_lifa_on_note(lifa_to_light, c, 2, 2.07, 2.78)
        light_lifa_on_note(lifa_to_light, c, 4, 2.48, 3.3)
        light_lifa_on_note(lifa_to_light, c, 3, 3.0, 3.85)
        light_lifa_on_note(lifa_to_light, c, 4, 3.55, 4.3)
        light_lifa_on_note(lifa_to_light, c, 2, 4.0, 4.85)
        light_lifa_on_note(lifa_to_light, c, 1, 4.55, 5.3)
        light_lifa_on_note(lifa_to_light, c, 2, 5.0, 5.85)
        light_lifa_on_note(lifa_to_light, c, 5, 5.55, 6.37)
        light_lifa_on_note(lifa_to_light, c, 3, 6.07, 6.85)
        light_lifa_on_note(lifa_to_light, c, 2, 6.55, 7.3)
        light_lifa_on_note(lifa_to_light, c, 4, 7.0, 8.0)

#
#     light_lifa_on_note(lifa_to_light, c, 3, 0.0, 1.0)
#     light_lifa_on_note(lifa_to_light, c, 2, 1.0, 2.07)
#     light_lifa_on_note(lifa_to_light, c, 4, 2.07, 3.0)
#     light_lifa_on_note(lifa_to_light, c, 3, 3.0, 4.0)
#     light_lifa_on_note(lifa_to_light, c, 1, 4.0, 5.0)
#     light_lifa_on_note(lifa_to_light, c, 2, 5.0, 6.07)
#     light_lifa_on_note(lifa_to_light, c, 3, 6.07, 7.0)
#     light_lifa_on_note(lifa_to_light, c, 4, 7.0, 8.0)

# def violin2end (lifa_to_light, c):
#
#     light_lifa_on_note(lifa_to_light, c, 3, 0.0, 0.55)
#     light_lifa_on_note(lifa_to_light, c, 1, 0.55, 1.0)
#     light_lifa_on_note(lifa_to_light, c, 2, 1.0, 1.55)
#     light_lifa_on_note(lifa_to_light, c, 5, 1.55, 2.07)
#     light_lifa_on_note(lifa_to_light, c, 2, 2.07, 2.48)
#     light_lifa_on_note(lifa_to_light, c, 4, 2.48, 3.0)
#     light_lifa_on_note(lifa_to_light, c, 3, 3.0, 3.55)
#     light_lifa_on_note(lifa_to_light, c, 4, 3.55, 4.0)
#     light_lifa_on_note(lifa_to_light, c, 2, 4.0, 4.55)
#     light_lifa_on_note(lifa_to_light, c, 1, 4.55, 5.0)
#     light_lifa_on_note(lifa_to_light, c, 2, 5.0, 5.55)
#     light_lifa_on_note(lifa_to_light, c, 5, 5.55, 6.07)
#     light_lifa_on_note(lifa_to_light, c, 3, 6.07, 6.55)
#     light_lifa_on_note(lifa_to_light, c, 2, 6.55, 7.0)
#     light_lifa_on_note(lifa_to_light, c, 4, 7.0, 8.0)


episodes(12, 14)
violin1end(sticks3, light_yellow_strip)

episode(12)
violin1end(sticks8, light_yellow_strip)
violin1end(sticks7, light_yellow_strip)

episode(12)
violin2end(lifas5, (0.74, 0.6, 1.0))
violin2end(lifas1, (0.74, 0.6, 1.0))
violin2end(lifas4, (0.74, 0.6, 1.0))


episode(12)
cycle(16)
elements(lifas, sticks8, sticks8)
effect.saw_tooth(1.0, False)

episodes(12, 13)
cycle(16)
elements(donut1, rug4, flower6)
color.uniform(coral)
effect.breath(1.0)

elements(bottle5, paper2)
color.uniform(pink_string)
effect.breath(1.0)

elements(cup_cake4, cabbage6)
color.uniform(light_coral)
effect.breath(1.0)

elements(cabbage5, bottle4, donut3)
color.uniform(magenta)
effect.breath(1.0)

elements(flower1, cup_cake3, brain7)
color.uniform(red)
effect.breath(1.0)

elements(cabbage1, paper5, rug6)
color.uniform((0.9, 0.9, 1.0))
effect.breath(1.0)

send_to_mqtt("essoteric")
start_song("essoteric", 0)

