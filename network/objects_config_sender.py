import time

import paho.mqtt.client as mqtt
import json

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
    for led_object,thing_name in obj_to_thing.items():
        send_to_single_thing(thing_name, led_object)


# send_to_single_thing("flower1", flower1)
send_to_all_things();

time.sleep(3)


