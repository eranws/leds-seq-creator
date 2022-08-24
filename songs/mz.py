from infra.animations_factory import color, effect
from led_objects.instances import *
from led_objects.objects_selector import elements
from led_objects.groups import lifas1
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, cycle, cycle_beats
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



