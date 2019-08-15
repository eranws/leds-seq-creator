from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, load
from infra.timing import beats
from led_objects.cabbages import cabbage1, cabbage6, brain7, cabbage5, cabbages, brains, donut1, donut3
from led_objects.flood import cup_cakes, cup_cake3
from led_objects.led_object import all
from led_objects.flowers import *
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, lifas, stands
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats
from infra.colors import *

song_settings(bpm=118, beats_per_episode=8)

episodes(0, 4)
elements(all)
cycle(2)
color.gradient(0.61,0.46)
effect.snake_up_down(0.5)
effect.hue_breath()

#Snear
def snear(episodes_p):
    episodes(episodes_p[0], episodes_p[1])
    elements(cup_cake3)
    color.uniform(light_indigo)
    cycle(1)
    effect.blink()
snear([4,12])

episodes(6, 9)
elements(stands)
cycle(8)
color.uniform(light_blue)
effect.breath(1)

beats(72,81)
elements(papers)
cycle(81-72)
color.uniform(red)
effect.hue_breath(hard)
effect.breath(1)



def rain_drifting_on_the_cloudy_water(first_beat, last_beat):
    beats(first_beat,last_beat)
    cycle(last_beat-first_beat)
    elements(papers)
    color.gradient(0.995,1)
    effect.hue_breath(hard)
    effect.breath(0.8)
rain_drifting_on_the_cloudy_water(98,112)
rain_drifting_on_the_cloudy_water(116,131)
rain_drifting_on_the_cloudy_water(131,147)


episodes(18,22)
cycle(1)
elements(flowers, bottles)
color.uniform(dark_blue)
effect.saw_tooth(1)

episode (22)
elements(papers)
color.gradient (0.995,1)
effect.hue_breath(soft)
#sing

episodes(22,31)
elements(cup_cakes)
color.uniform(blue)
cycle(4)
cycle_beats(0,2)
effect.blink_repeat(16)

snear([26,30])

#episodes 30-32
rain_drifting_on_the_cloudy_water(242,256)
#rain_drifting_on_the_cloudy_water([36,43])

episode(27)
elements(papers)
color.gradient (0.995,1)
effect.hue_breath(soft)
#sing

episodes(30,34)
cycle(16)
elements(papers)
color.gradient (0.995,1)
effect.hue_breath(hard)
#sing

episodes(36,43)
cycle(16)
elements(papers)
color.gradient (0.995,1)
effect.hue_breath(hard)

##############################################################3
def pattern():
    episodes(34,43)
    cycle(4)
    offset = 1.25

    cycle_beats(0,offset)
    elements(sticks8.stand(5))
    color.uniform(red)

    cycle_beats(offset,offset + 0.25)
    elements(sticks8.stand(1))
    color.uniform(light_coral)

    cycle_beats(offset + 0.25, offset + 0.5)
    elements(sticks8.stand(2))
    color.uniform(light_coral)

    cycle_beats(offset + 0.5, offset + 0.75)
    elements(sticks8.stand(3))
    color.uniform(light_coral)

    cycle_beats(offset + 0.75,offset + 1.25)
    elements(sticks8.stand(4))
    color.uniform(light_coral)

    cycle_beats(offset + 1.25, offset + 1.5)
    elements(sticks8.stand(1))
    color.uniform(light_coral)

    cycle_beats(offset + 1.5, offset + 2)
    elements(sticks8.stand(2))
    color.uniform(light_coral)

    cycle_beats(offset + 2, offset + 2.25)
    elements(sticks8.stand(3))
    color.uniform(light_coral)

    cycle_beats(offset + 2.25, offset + 2.75)
    elements(sticks8.stand(4))
    color.uniform(light_coral)

##############################################################3
pattern()

episode (46)
elements(papers)
color.gradient (0.995,1)
effect.hue_breath(soft)
#sing





send_to_mqtt("lostShort")
start_song("lostShort", 116/8*8*1000*60/118)


