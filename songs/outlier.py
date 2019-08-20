from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects import meduza

from led_objects.cabbages import cabbage1, cabbage6, brain7, cabbage5, cabbages, brains, donut1, donut3, donuts
from led_objects.flood import rugs, cup_cakes
from led_objects.groups import group1
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, flower1, paper2
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, lifas, sticks, \
    single_lifas

from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=117, beats_per_episode=32, start_offset=3)

def bling(elem, col_uni):
    cycle(32)
    cycle_beats(4, 12)
    elements(elem)
    color.uniform(col_uni)
    effect.snake()

def fast( start_beat, end_beat, elem, elem_strong, col_grad ):
    beats(start_beat, start_beat+1)
    for el in elem:
        elements(el)
        color.gradient(col_grad[0],col_grad[1])
        effect.snake()
    beats(start_beat+1, start_beat+2)
    for elem_s in elem_strong:
        elements(elem_s)
        color.gradient(col_grad[0],col_grad[1])
        effect.snake()

    beats(start_beat+2,end_beat)
    cycle(3)
    cycle_beats(0,1)
    for el in elem:
        elements(el)
        color.gradient(col_grad[0], col_grad[1])
        effect.snake()
        cycle_beats(1,2)
        elements(el)
        color.gradient(col_grad[0], col_grad[1])
        effect.snake()
    cycle_beats(2,3)
    for elem_s in elem_strong:
        elements(elem_s)
        color.gradient(col_grad[0], col_grad[1])
        effect.snake()

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
elements(flowers,cabbages,brains,cup_cakes)
color.gradient(0,0.1)
effect.snake()

episode(1)
bling(lifas5,coral)
# cycle(32)
# cycle_beats(4,12)
# elements(lifas5)
# color.uniform(coral)
# effect.snake()

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
# cycle(32)
# cycle_beats(28,29)
# effect.saw_tooth()
# cycle_beats(29,30)
# effect.saw_tooth()
# cycle_beats(30,31)
# effect.saw_tooth()
# cycle_beats(31,32)
# effect.saw_tooth()

episode(4)
cycle(32)
cycle_beats(4,12)
elements(lifas1)
color.uniform(indigo)
effect.snake()

# lots of color coming in
episodes(5,7)
cycle(2)
elements(all)
color.gradient(0,1)
effect.hue_breath()

# tututututututu
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

# untzuntz
episodes(8,10)
cycle(2)
elements(all)
color.gradient(0.5,0.75)
effect.saw_tooth()
# tududu
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

# moving to the underlying base
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
cycle(32)
cycle_beats(0,8)
elements(cabbage6)
color.gradient(blue[0],indigo[0])
effect.snake()
cycle_beats(8,16)
elements(cabbage1)
color.gradient(blue[0],indigo[0])
effect.snake()
cycle_beats(16,24)
elements(cabbage5)
color.gradient(blue[0],indigo[0])
effect.snake()
cycle_beats(24,32)
elements(brain7)
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
elements(brains,rugs)
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

episodes(12,15)
cycle(16)
elements(all)
color.gradient(0,0.1)
effect.breath()

cycle(8)
elements(flowers,cabbages,brains,cup_cakes)
color.gradient(indigo[0],green[0])
effect.snake()

episode(12)
bling(sticks3,red)
# cycle(32)
# cycle_beats(4,12)
# elements(sticks3)
# color.gradient(indigo[0],green[0])
# effect.snake()
#
# episode(14)
# cycle(32)
# cycle_beats(4,12)
# elements(lifas4)
# color.uniform(coral)
# effect.snake()
episode(14)
bling(lifas4,yellow_string)

# episodes(15,17)
# cycle(4)
# elements(all)
# color.gradient(indigo[0],green[0])
# effect.breath()

# fast(13*32, 14*32, [sticks3],[single_sticks,cup_cakes],[aquamarine[0],aquamarine[0]])

for el in [cabbage1,cabbage5,cabbage6,brain7,flower6,flower1,paper5,paper2,donut1,donut3]:
    el.random

fast(512,568, [lifas,sticks],[single_sticks,single_lifas,cabbages,brains,flowers,papers,donuts],[aquamarine[0],purple_strip[0]])
fast(568,700, [lifas,sticks],[single_sticks,single_lifas,cabbages,brains,flowers,papers,donuts],[aquamarine[0],purple_strip[0]])
# fast(17*32,[lifas,sticks],[single_sticks,single_lifas,cabbages,brains,flowers,papers,donuts],[aquamarine[0],purple_strip[0]])
#
# episode(15)
# cycle(32)
# cycle_beats(4,12)
# elements(all)
# effect.breath(edge=0)
# elements(lifas,sticks)
# color.gradient(0,1)
# effect.snake()

# episode(17)
# beats(550,592)
# cycle(4)
# color.uniform(coral)
# elements(sticks,lifas)
# effect.snake()


# beats(552,592)
# cycle(1)
# elements(single_lifas,single_sticks)
# color.uniform(coral)
# effect.snake()

beats(550,608)
cycle(2)
cycle_beats(1,2)
elements(donuts)
color.gradient(0,1)
effect.hue_breath()

beats(550,608)
cycle(32)
cycle_beats(0,8)
elements(cabbage6)
color.gradient(blue[0],indigo[0])
effect.snake()
cycle_beats(8,16)
elements(cabbage1)
color.gradient(blue[0],indigo[0])
effect.snake()
cycle_beats(16,24)
elements(cabbage5)
color.gradient(blue[0],indigo[0])
effect.snake()
cycle_beats(24,32)
elements(brain7)
color.gradient(blue[0],indigo[0])
effect.snake()

beats(550,608)
cycle(2)
cycle_beats(1,2)
elements(flowers)
color.uniform(red)
effect. blink()

beats(558,608)
cycle(2)
cycle_beats(1,2)
elements(cup_cakes)
color.uniform(red)
effect.blink()

beats(566,608)
cycle(2)
cycle_beats(1,2)
elements(papers)
color.uniform(red)
effect.blink()

beats(574,608)
cycle(2)
cycle_beats(1,2)
elements(brains)
color.uniform(red)
effect.blink()

beats(582,608)
cycle(2)
cycle_beats(1,2)
elements(cabbages)
color.uniform(red)
effect.blink()

beats(590,608)
cycle(2)
cycle_beats(1,2)
elements(lifas)
color.uniform(coral)
effect.blink()

beats(600,608)
cycle(2)
cycle_beats(1,2)
elements(sticks)
color.uniform(coral)
effect.blink()

episode(18)
bling(sticks3,green)

episodes(19,22)
cycle(2)
cycle_beats(1,2)
elements(all)
color.gradient(turquoise_string[0]+0.1,coral[0]-0.1)
effect.blink()

for e in all:
    e.straight

episode(23)
cycle(32)
elements(all)
color.uniform(indigo)
effect.snake()
cycle(4)
elements(sticks8)
color.gradient(0,1)
effect.hue_breath()

episode(24)
cycle(4)
elements(sticks8)
color.gradient(0,1)
effect.hue_breath()

send_to_mqtt("outlier")
start_song("outlier",16.4*16-10)#offset in seconds


