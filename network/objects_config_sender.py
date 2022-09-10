import time

import paho.mqtt.client as mqtt
import json

from thing_to_obj_map import obj_to_thing

mqtt_host_name = "10.0.0.200"
mqtt_client_id = "objects_map_sender"

client = mqtt.Client(mqtt_client_id)

try:
    client.connect(mqtt_host_name)
except OSError as e:
    print("Error: Mqtt client is Null:")
    print(e)


def ledObjectToJson(led_object):
    led_object_json = {
        "total_pixels": led_object.total_pixels,
        "objects": led_object.mapping,
    }
    return json.dumps(led_object_json, separators=(",", ":"))


def send_to_single_thing(thing_name, led_object):
    json_str = ledObjectToJson(led_object)
    print(f"json size: {len(json_str)}")
    print(json_str)

    if client:
        client.publish(topic="objects-config/" + thing_name, payload=json_str)
    else:
        print("Mqtt client is Null")


def send_to_all_things():
    for led_object, thing_name in obj_to_thing.items():
        send_to_single_thing(thing_name, led_object)


# send_to_single_thing("flower1", flower1)
send_to_all_things()

time.sleep(3)
