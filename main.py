import paho.mqtt.client as mqtt
import json
from led_objects.led_object import all
from infra.colors import red, blue
from infra.animations_factory import effect, color
from infra.timing import cycle, episodes, song_settings
from led_objects.instances import flower1, cabbage1
from led_objects.objects_selector import elements
from thing_to_obj_map import obj_to_thing

song_settings(bpm=123, beats_per_episode=32, start_offset=0)

all.append(flower1)
all.append(cabbage1)

episodes(0, 10)
# cycle_beats(0,16)
elements(cabbage1)
cycle(32)
color.uniform(red)
effect.fill()

elements(flower1)
cycle(16)
color.uniform(blue)
effect.fill()

host_name = "10.0.0.200"
client = mqtt.Client("leds-seq-creator")
client.connect(host_name)

for led_object, thing_name in obj_to_thing.items():
    animations_json = [an.to_json_obj(False) for an in led_object.animations]
    json_str = json.dumps(animations_json, separators=(",", ":")) + "\0"
    print("sending json of size {} to thing {}".format(len(json_str), thing_name))
    client.publish("animations/{}/alterego".format(thing_name), json_str)
