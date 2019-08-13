from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.flood import cup_cakes
from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands
from network.send_to_mqtt import send_to_mqtt
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=73.5, beats_per_episode=16)

def yellowopening():

    elements(group5)
    cycle(beats=16)
    cycle_beats(0, 1)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group1)
    cycle(beats=16)
    cycle_beats(2, 3)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group6)
    cycle(beats=16)
    cycle_beats(4, 5)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group2)
    cycle(beats=16)
    cycle_beats(6, 7)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group4)
    cycle(beats=16)
    cycle_beats(8, 9)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group7)
    cycle(beats=16)
    cycle_beats(10, 11)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group3)
    cycle(beats=16)
    cycle_beats(12, 13)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group8)
    cycle(beats=16)
    cycle_beats(14, 15)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

episode(0)
yellowopening()

def coloropening():
    elements(group5)
    cycle(beats=16)
    cycle_beats(0, 16)
    color.uniform(light_orange_strip)
    effect.saw_tooth(1.0, False)

    elements(group1)
    cycle(beats=16)
    cycle_beats(2, 16)
    color.uniform(light_coral)
    effect.saw_tooth(1.0, False)

    elements(group6)
    cycle(beats=16)
    cycle_beats(4, 16)
    color.uniform(light_pink_strip)
    effect.saw_tooth(1.0, False)

    elements(group2)
    cycle(beats=16)
    cycle_beats(6, 16)
    color.uniform(light_purple_string)
    effect.saw_tooth(1.0, False)

    elements(group4)
    cycle(beats=16)
    cycle_beats(8, 16)
    color.uniform(purple_string)
    effect.saw_tooth(1.0, False)

    elements(group7)
    cycle(beats=16)
    cycle_beats(10, 16)
    color.uniform(blue)
    effect.saw_tooth(1.0, False)

    elements(group3)
    cycle(beats=16)
    cycle_beats(12, 16)
    color.uniform(light_blue)
    effect.saw_tooth(1.0, False)

    elements(group8)
    cycle(beats=16)
    cycle_beats(14, 16)
    color.uniform(aquamarine)
    effect.saw_tooth(1.0, False)

episode(1)
coloropening()

def clapping(clapping_lights):

    elements(clapping_lights)
    cycle(beats=4)

    cycle_beats(1.0, 1.37)
    effect.saw_tooth(0.5)
    color.uniform(coral)

    cycle_beats(1.37, 1.75)
    effect.saw_tooth(0.5)
    color.uniform(pink_strip)

    cycle_beats(1.75, 3)
    effect.saw_tooth(0.5)
    color.uniform(light_pink_strip)



episode(2)
clapping(all)

def violin1(stick_to_light):

    elements(stick_to_light.stand(3))
    cycle(beats=8)
    cycle_beats(0.0, 0.55)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)


    elements(stick_to_light.stand(1))
    cycle(beats=8)
    cycle_beats(0.55, 1.0)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

    elements(stick_to_light.stand(2))
    cycle(beats=8)
    cycle_beats(1.0, 1.75)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

    elements(stick_to_light.stand(5))
    cycle(beats=8)
    cycle_beats(1.75, 2.07)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)


    elements(stick_to_light.stand(2))
    cycle(beats=8)
    cycle_beats(2.07, 2.48)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

    elements(stick_to_light.stand(4))
    cycle(beats=8)
    cycle_beats(2.48, 3.0)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

    elements(stick_to_light.stand(3))
    cycle(beats=8)
    cycle_beats(3.0, 3.55)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

    elements(stick_to_light.stand(4))
    cycle(beats=8)
    cycle_beats(3.55, 4.0)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)


    elements(stick_to_light.stand(3))
    cycle(beats=8)
    cycle_beats(4.0, 4.5)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)


    elements(stick_to_light.stand(1))
    cycle(beats=8)
    cycle_beats(4.5, 5.0)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

    elements(stick_to_light.stand(2))
    cycle(beats=8)
    cycle_beats(5.0, 5.71)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

    elements(stick_to_light.stand(5))
    cycle(beats=8)
    cycle_beats(5.71, 6.07)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)


    elements(stick_to_light.stand(2))
    cycle(beats=8)
    cycle_beats(6.07, 6.6)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

    elements(stick_to_light.stand(4))
    cycle(beats=8)
    cycle_beats(6.6, 7.0)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

    elements(stick_to_light.stand(3))
    cycle(beats=8)
    cycle_beats(7.0, 8.0)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)


episodes(3, 7)
violin1(sticks3)

episodes(4, 7)
violin1(sticks8)

episodes(5, 7)
violin1(sticks7)


episode(5)
clapping(flowers)

episode(6)
clapping(cabbages)

episode(7)
clapping(flowers)





send_to_mqtt("essoteric")



