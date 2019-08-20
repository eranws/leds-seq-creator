import time

import paho.mqtt.client as mqtt
import json

from thing_to_obj_map import obj_to_thing

host_name = "10.0.0.200"
mqtt_client_id = "objects_map_sender"

def ledObjectToJson(led_object):
    return {
        "total_pixels": led_object.total_pixels,
        "objects": led_object.mapping
    }


client = mqtt.Client(mqtt_client_id)
client.connect(host_name)

for obj_with_thing in obj_to_thing.items():
    thing_name = obj_with_thing[1]
    if thing_name != "sticks8":
        continue
    led_object = obj_with_thing[0]
    json_str = json.dumps(ledObjectToJson(led_object))
    topic = "objects-config/" + thing_name
    print("sending config to thing '{}'".format(thing_name))
    print(json_str)
    client.publish(topic, json_str + '\0')

time.sleep(3)


