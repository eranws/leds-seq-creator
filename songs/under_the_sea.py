from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, load
from infra.timing import beats
from led_objects.cabbages import cabbage1, cabbage6, brain7, cabbage5, cabbages, brains, donut1, donut3, donuts
from led_objects.flood import cup_cakes, cup_cake3, rugs
from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.led_object import all
from led_objects.sheep import  sheep
from led_objects.flowers import *
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, \
    sticks7, sticks3, lifas5, lifas1, lifas4, lifas, stands
from led_objects.meduza import  meduza
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats
from infra.colors import *

song_settings(bpm=128, beats_per_episode=8,start_offset = 3.09)
episode_length = 8
background_elements = [sheep] + cabbages + brains + donuts + rugs + flowers + bottles

def pattern(first_beat, main_color=coral, second_color=indigo, standing_elem=sticks8):
    beats(first_beat,first_beat+4)
    cycle(8)
    offset = 0
    def pattern_inner(offset):
        cycle_beats(offset, offset + 0.25)
        elements(standing_elem.stand(1))
        color.uniform(main_color)

        cycle_beats(offset + 0.25, offset + 0.5)
        elements(standing_elem.stand(2))
        color.uniform(main_color)

        cycle_beats(offset + 0.5, offset + 0.75)
        elements(standing_elem.stand(3))
        color.uniform(main_color)

        cycle_beats(offset + 0.75, offset + 1.25)
        elements(standing_elem.stand(4))
        color.uniform(main_color)

        cycle_beats(offset + 1.25, offset + 1.75)
        elements(standing_elem.stand(5))
        color.uniform(main_color)

        cycle_beats(offset + 1.75, offset + 2)
        elements(standing_elem.stand(1))
        color.uniform(main_color)

        cycle_beats(offset + 2, offset + 2.5)
        elements(standing_elem.stand(2))
        color.uniform(main_color)

        cycle_beats(offset + 2.5, offset + 3)
        elements(standing_elem.stand(3))
        color.uniform(main_color)

    pattern_inner(0)
    cycle_beats(3, 3.5)
    elements(standing_elem.stand(4))
    color.uniform(second_color)

    cycle_beats(3.5, 4)
    elements(standing_elem.stand(5))
    color.uniform(main_color)

    pattern_inner(4)

    cycle_beats(7, 8)
    elements(standing_elem.stand(4))
    color.uniform(main_color)
pattern(2, sticks8)
pattern(10, sticks7)

send_to_mqtt("under")
start_song("under", 0*8*60/118+3)