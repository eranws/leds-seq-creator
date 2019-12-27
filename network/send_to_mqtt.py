import http.client
import json

import paho.mqtt.client as mqtt

from infra.functions_store import float_functions_store, boolean_functions_store, discrete_float_functions_store
from thing_to_obj_map import obj_to_thing

host_name = "10.0.0.200"
sender_mqtt_client_id = "leds-seq-creator"


sent_not_acked = set()

def on_publish_callback(client, userdata, mid):
    global sent_not_acked
    sent_not_acked.remove(mid)
    if len(sent_not_acked) == 0:
        print("sent all messages, disconnecting from mqtt")
        client.disconnect()


def start_song(song_name, start_time=0):
    json_data = {
        "file_id": "{}.wav".format(song_name),
        "start_offset_ms": int(start_time * 1000)
    }
    body = json.dumps(json_data)
    conn = http.client.HTTPConnection(host_name, 8080)
    conn.request("PUT", "/api/current-song", body)


def send_to_mqtt(filename):
    global sent_not_acked
    client = mqtt.Client(sender_mqtt_client_id)
    client.connect(host_name)
    client.on_publish = on_publish_callback

    for led_object, thing_name in obj_to_thing.items():

        float_functions_store.reset()
        boolean_functions_store.reset()
        discrete_float_functions_store.reset()

        animations_json = [an.to_json_obj(False) for an in led_object.animations]

        animations_json_compact = [an.to_json_obj(True) for an in led_object.animations]
        print(float_functions_store.saved_func_by_index)
        compact_json = {"float_funcs": float_functions_store.saved_func_by_index,
                        "boolean_funcs": boolean_functions_store.saved_func_by_index,
                        "discrete_float_funcs": discrete_float_functions_store.saved_func_by_index,
                        "animations": animations_json_compact}

        json_str = json.dumps(animations_json, separators=(',', ':')) + '\0'
        json_str_compact = json.dumps(compact_json, separators=(',', ':')) + '\0'

        print(f"sending json to thing {thing_name} size: {len(json_str)}, compact: {len(json_str_compact)}")
        print(json_str)
        msg_info = client.publish("animations/{}/{}".format(thing_name, filename), json_str, qos=1)
        sent_not_acked.add(msg_info.mid)

    client.loop_forever(10)
    print("finished sending new animations to mqtt")
