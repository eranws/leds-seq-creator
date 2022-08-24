import time

import led_objects.object_config_pb2
import paho.mqtt.client as mqtt
import json

from led_objects.cabbages import cabbage1, cabbage6, cabbage5, brain7, donut3, donut1
from led_objects.flood import cup_cake3, cup_cake4, rug6, rug4
from led_objects.flowers import flower6, flower1, paper5, paper2, bottle4, bottle5, gloves8
from led_objects.meduza import meduza
from led_objects.sheep import sheep
from led_objects.stands import sticks7, lifas4, lifas1, lifas5, sticks3
from led_objects.stars import star7, star8
from thing_to_obj_map import obj_to_thing

mqtt_host_name = "10.0.0.200"
mqtt_client_id = "objects_map_sender"

def ledObjectToJson(led_object):
    return {
        "total_pixels": led_object.total_pixels,
        "objects": led_object.mapping
    }


client = mqtt.Client(mqtt_client_id)
client.connect(mqtt_host_name)

def send_to_single_thing(thing_name, led_object):
    json_str = json.dumps(ledObjectToJson(led_object), separators=(',', ':'))
    print(f"json size: {len(json_str)}")
    print(json_str)

    topic = "objects-config/" + thing_name
    client.publish(topic, json_str)

def send_to_all_things():
    for obj_with_thing in obj_to_thing.items():
        thing_name = obj_with_thing[1]
        led_object = obj_with_thing[0]
        send_to_single_thing(thing_name, led_object)


# send_to_single_thing("flower1", flower1)
send_to_all_things();

time.sleep(3)


