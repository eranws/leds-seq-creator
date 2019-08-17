from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load

from led_objects.cabbages import cabbage1, cabbage6, brain7, cabbage5, cabbages, brains, donut1, donut3, donuts
from led_objects.flood import rugs, cup_cakes
from led_objects.groups import group1
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, lifas, sticks, \
    single_lifas

from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=117, beats_per_episode=32)



episodes(0,3)
cycle(16)
elements(all)
color.uniform(indigo)
effect.breath()
episode(0)
cycle(4)
elements(sticks8)
color.gradient(0,1)
effect.hue_breath()

episodes(1,3)
cycle(8)
elements(flowers,cabbages,brains)
color.gradient(0,0.1)
effect.snake()

episode(1)
cycle(32)
cycle_beats(4,12)
elements(lifas5)
color.uniform(coral)
effect.snake()

episodes(2,5)
cycle(8)
elements(single_sticks,single_lifas)
color.uniform(coral)
effect.snake()

episodes(3,5)
cycle(8)
cycle_beats(4,6)
elements(all)
color.gradient(0,0.1)
effect.breath()
cycle_beats(6,8)
elements(all)
color.gradient(0,0.1)
effect.saw_tooth()

episode(4)
cycle(32)
cycle_beats(4,12)
elements(lifas1)
color.uniform(indigo)
effect.snake()

episodes(5,7)
cycle(2)
elements(all)
color.gradient(0,1)
effect.hue_breath()

episodes(6,8)
cycle(8)
elements(sticks)
color.gradient(0,0.1)
effect.snake()
cycle(8)
cycle_beats(6,8)
elements(single_lifas)
color.gradient(0,0.1)
effect.snake_down_up()
cycle(8)
cycle_beats(4,7)
elements(flowers,brains,cabbages)
color.gradient(0,0.1)
effect.snake()

episodes(8,10)
cycle(2)
elements(all)
color.gradient(0.5,0.75)
effect.saw_tooth()
cycle(32)
cycle_beats(14,20)
elements(cabbages)
color.uniform(purple_string)
effect.snake(3)
cycle_beats(14,20)
elements(brains)
color.uniform(purple_string)
effect.snake(3)
cycle_beats(16,26)
elements(single_sticks,single_lifas)
color.uniform(purple_string)
effect.snake()
cycle_beats(22,32)
elements(single_sticks,single_lifas)
color.uniform(purple_string)
effect.breath()

beats(320,323)
cycle(4)
color.uniform(purple_string)
elements(sticks,lifas)
effect.snake()

beats(322,378)
cycle(1)
elements(single_lifas,single_sticks)
color.uniform(purple_string)
effect.snake()

beats(320,384)
cycle(2)
cycle_beats(1,2)
elements(donuts)
color.gradient(0,0.1)
effect.blink()

beats(320,362)
cycle(8)
elements(cabbage6)
color.gradient(blue[0],indigo[0])
effect.snake()

beats(328,384)
cycle(2)
cycle_beats(1,2)
elements(flowers)
color.gradient(0,0.1)
effect.blink()

beats(336,384)
cycle(2)
cycle_beats(1,2)
elements(cup_cakes)
color.gradient(0,0.1)
effect.blink()

beats(344,384)
cycle(2)
cycle_beats(1,2)
elements(papers)
color.gradient(0,0.1)
effect.blink()

beats(352,384)
cycle(2)
cycle_beats(1,2)
elements(brains)
color.gradient(0,0.1)
effect.blink()

beats(360,384)
cycle(2)
cycle_beats(1,2)
elements(cabbages)
color.gradient(0,0.1)
effect.blink()

beats(368,384)
cycle(2)
cycle_beats(1,2)
elements(lifas)
color.gradient(0,0.1)
effect.blink()

beats(376,384)
cycle(2)
cycle_beats(1,2)
elements(sticks)
color.gradient(0,0.1)
effect.blink()

episodes(12,14)
cycle(16)
elements(all)
color.gradient(0,0.1)
effect.breath()

cycle(8)
elements(flowers,cabbages,brains,cup_cakes)
color.gradient(indigo[0],green[0])
effect.snake()

episode(12)
cycle(32)
cycle_beats(4,12)
elements(sticks3)
color.gradient(indigo[0],green[0])
effect.snake()

send_to_mqtt("outlier")
start_song("outlier",160)#offset in seconds


