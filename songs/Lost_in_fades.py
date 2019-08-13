from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, brain4, cabbage5, cabbages, brains, donut1, donut3
from led_objects.led_object import all
from led_objects.flowers import *
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4
from network.send_to_mqtt import send_to_mqtt
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats
from infra.colors import *

song_settings(bpm=118, beats_per_episode=8)

episodes(0, 12)
elements(lifas1)
cycle(2)
cycle_beats(0,1)
color.uniform(red)
#effect.blink()
cycle_beats(1,2)
color.uniform(green)

episodes(9,10)
elements(papers)
color.uniform(red)
cycle(8)
effect.saw_tooth(edge=1,reverse=True)
episodes(10,11)
cycle(8)
cycle_beats(0,1)
color.uniform(red)


send_to_mqtt("lostShort")



