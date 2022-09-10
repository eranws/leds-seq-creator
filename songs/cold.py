from animations.rainbow import Rainbow
from float_func.sin import SinFloatFunc
from infra.animations_factory import effect
from led_objects.led_object import all
from led_objects.objects_selector import elements
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, cycle, beats
from infra.colors import *

song_settings(bpm=60, beats_per_episode=1, start_offset=0)

with open("/home/amir/labels/cold.txt") as fp:
    row_lines = [l.split() for l in fp]
    segments = [
        {"start": float(label[0]), "end": float(label[1]), "name": label[2]}
        for label in row_lines
        if len(label) == 3
    ]
    cues = [float(label[0]) for label in row_lines if len(label) == 2]

# map fade start time to end time
fades = [segment for segment in segments if segment["name"] == "fade"]


def find_fade_end(start_time):
    dist = [fade for fade in fades if abs(start_time - fade["start"]) < 0.05]
    return dist[0]["end"]


voices = [
    {
        "name": segment["name"],
        "start": segment["start"],
        "fade": segment["end"],
        "end": find_fade_end(segment["end"]),
        "cues": list(
            sorted(
                [
                    cue
                    for cue in cues
                    if cue >= segment["start"] and cue <= segment["end"]
                ]
            )
        ),
    }
    for segment in segments
    if segment["name"] != "fade"
]

beats(0, 1000)
elements(all)
cycle(15)
Rainbow(SinFloatFunc(-0.01, 0.12, 0, 1), SinFloatFunc(-0.01, 0.12, 0.5, 1)).apply()
effect.brightness(0.25)

for voice in voices:

    beats(voice["start"], voice["end"])

    # # coloring
    # if voice["name"] == "la":
    #     color.gradient(0.98, 1.05)
    # else:
    #     color.gradient(0.6, 0.75)
    #     effect.brightness(0.5)
    # effect.hue_saw_tooth(0.1)
    #
    # # fade in in entrence
    # beats(voice["start"], voice["start"] + 0.3)
    # effect.fade_in()

    beats(voice["fade"], voice["end"])
    # effect.fade_out()
    # if voice["name"] == "la":
    #     fade_out_wave_rand()
    # else:
    #     fade_out_gradually_rand()

send_to_mqtt("cold")
start_song("cold", 0)
