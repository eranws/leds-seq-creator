from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cabbage5, cabbages, brains, donut1, donut3
from led_objects.led_object import all
from led_objects.flowers import *
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4
from network.send_to_mqtt import send_to_mqtt
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats
from infra.colors import *

song_settings(bpm=118, beats_per_episode=8)

episodes(0, 4)
elements(paper2)
cycle(2)
cycle_beats(0,1)
color.uniform(red)
effect.saw_tooth()
cycle_beats(1,2)
elements(paper2)
color.uniform(blue)
effect.saw_tooth()

elements(lifas1)
cycle(2)
cycle_beats(0,0.5)
elements(lifas1.stand(5))
color.uniform(light_coral)
cycle_beats(0.5,1)
elements(lifas1.stand(2))
color.uniform(light_coral)
cycle_beats(1,1.5)
elements(lifas1.stand(3))
color.uniform(light_coral)
cycle_beats(1.5,2)
elements(lifas1.stand(4))
color.uniform(light_coral)



send_to_mqtt("mzShort")



