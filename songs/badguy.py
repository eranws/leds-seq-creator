import json
import random

from animations.fill import FillAnimation
from float_func.const import ConstFloatFunc
from float_func.sin import SinFloatFunc
from infra.animations_factory import color, effect

from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.groups import flowers, cabbages

# from led_objects.led_object import all
from led_objects.objects_selector import elements
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import beats_in_episode, song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_offset=0
song_settings(bpm=123, beats_per_episode=32, start_offset=0)

# all.append(cabbages)
# all.append(flowers)
groups = [group1, group2, group3, group4, group5, group6, group7, group8]

all = [cabbages, flowers]

episode(0)
elements(all)

# episode(1)
# elements(cabbages)
# color.alternate(blue,green)
# effect.fill_in_steps(32)

# episode(1)
# elements(flowers)
color.uniform(green)
effect.fill()



from thing_to_obj_map import obj_to_thing
for led_object, thing_name in obj_to_thing.items():
    animations_json = [an.to_json_obj(False) for an in led_object.animations]

print(json.dumps(animations_json,separators=(',',':\t'),indent=2))
# send_to_mqtt("badguy")
# start_song("badguy", song_offset)

