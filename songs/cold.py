import random

from animations import brightness
from animations.hue_shift import hue_shift_jump_on_cycle
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.flood import cup_cakes, rugs
from led_objects.groups import group1, group2, group8, group3, group6, group4, group7, group5
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles, paper2, flower1
from led_objects.meduza import meduza
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands, \
    single_lifas, single_stands, single_stands_per_stand
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=60, beats_per_episode=1, start_offset=0)

with open('/home/amir/labels/cold.txt') as fp:
    row_lines = [l.split() for l in fp]
    segments = [{"start": float(label[0]), "end": float(label[1]), "name": label[2]} for label in row_lines if len(label) == 3]
    cues = [float(label[0]) for label in row_lines if len(label) == 2]

# map fade start time to end time
fades = [segment for segment in segments if segment["name"] == "fade"]
def find_fade_end(start_time):
    dist = [fade for fade in fades if abs(start_time - fade["start"]) < 0.05]
    return dist[0]["end"]

voices = [{"name": segment["name"],
           "start": segment["start"],
           "fade": segment["end"],
           "end": find_fade_end(segment["end"]),
           "cues": list(sorted([cue for cue in cues if cue >= segment["start"] and cue <= segment["end"]]))
           } for segment in segments if segment["name"] != "fade"]

fade_back = [group1, [group2, group8], [group3, group6], group4, group7, group5]
fade_front = list(reversed([group1, [group2, group8], [group3, group6], group4, group7, group5]))
fade_left = [[group3, group4], [group2, group7], [group8], [group1, group5], group6]
fade_right = list(reversed([[group3, group4], [group2, group7], [group8], [group1, group5], group6]))
fade_orders = [fade_back, fade_front, fade_left, fade_left]

def rand_fade_out(fade_start, fade_end):
    fade_time = fade_end - fade_start
    fade_order = random.choice(fade_orders)
    for i, elem in enumerate(fade_order):
        elements(elem)
        curr_fade_start = fade_start + (i / len(fade_order)) * fade_time
        beats(curr_fade_start, fade_end)
        effect.fade_out()
        cycle(0.1)
        effect.blink(0.03)

for voice in voices:

    elements(all)

    beats(voice["start"], voice["end"])

    # coloring
    if voice["name"] == "la":
        color.gradient(0.98, 1.05)
    else:
        color.gradient(0.6, 0.75)
        effect.brightness(0.5)
    effect.hue_saw_tooth(0.1)

    # fade in in entrence
    beats(voice["start"], voice["start"] + 0.3)
    effect.fade_in()

    rand_fade_out(voice["fade"], voice["end"])

send_to_mqtt("cold")
start_song("cold", 0)


