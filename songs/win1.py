from infra.animations_factory import color, effect
from led_objects.led_object import all
from led_objects.meduza import meduza
from led_objects.objects_selector import elements
from led_objects.sheep import sheep
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, cycle, beats
from infra.colors import *

song_settings(bpm=60, beats_per_episode=1, start_offset=0)

beats(0, 8)
cycle(2)
elements(all)
color.uniform(pink_strip)
effect.breath(edge=0.5)

beats(0, 8)
cycle(2)
elements(meduza)
color.uniform(indigo)
effect.breath(edge=0.5)

beats(0, 8)
cycle(2)
elements(sheep)
color.uniform((1.0, 0, 1.0))
effect.breath(edge=0.5)

beats(0, 0.5)
effect.fade_in()

send_to_mqtt("game_audio/win1")
start_song("game_audio/win1", 0)
