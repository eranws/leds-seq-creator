import time

import requests
import json


def send_new_file(file_name):
    data = {
        "file_id": file_name,
        "start_offset_ms": 0
    }
    r = requests.put(url = "http://10.0.0.200:8080/api/current-song", data=json.dumps(data))


for i in range(1000):
    send_new_file("alterego.wav")
    time.sleep(10)
    # send_new_file("millenium.wav")
    # time.sleep(3)







