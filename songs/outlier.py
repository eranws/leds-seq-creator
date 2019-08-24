import random

from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects import meduza, sheep

from led_objects.cabbages import cabbage1, cabbage6, brain7, cabbage5, cabbages, brains, donut1, donut3, donuts
from led_objects.flood import rugs, cup_cakes, cup_cake3, rug6, cup_cake4
from led_objects.groups import group1
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, flower1, paper2, strings, bottles
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, lifas, sticks, \
    single_lifas

from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

##### left to work on #####
# pull and see if still works (meduza & sheep?), Also change accordingly list for final blinking.
# nothing changes in episode 21 (maybe add more hue shift, change frequency, or add some crazy coral)
# after all corals do 'bling', all turns off - not nice
# nothing on episode 28
###########################
song_settings(bpm=117, beats_per_episode=32, start_offset=3)

all.append(meduza.meduza)
not_tubes = [strings,cabbages,rugs,donuts,cup_cakes,meduza.meduza]
def bling(elem, col_uni):
    cycle(32)
    cycle_beats(4, 12)
    elements(elem)
    color.uniform(col_uni)
    effect.snake()

def bling_b(beat, elem, col_uni):
    beats(beat, beat+8)
    elements(elem)
    color.uniform(col_uni)
    effect.snake()

def fast( start_beat, end_beat, elem, elem_strong, col_grad ):
    beats(start_beat, start_beat+1)
    for el in elem:
        for e in all+[sheep.sheep]:
            e.random
        elements(el)
        color.gradient(col_grad[0],col_grad[1])
        effect.snake(0.5)
        for e in all+[sheep.sheep]:
            e.straight
    beats(start_beat+1, start_beat+2)
    for elem_s in elem_strong:
        elements(elem_s)
        color.gradient(col_grad[0],col_grad[1])
        effect.snake(4)

    beats(start_beat+2,end_beat)
    cycle(3)

    for el in elem:
        for e in all+[sheep.sheep]:
            e.random
        cycle_beats(0, 2/3)
        elements(el)
        color.gradient(col_grad[0], col_grad[1])
        effect.snake(0.5)

        cycle_beats(2/3, 4/3)
        elements(el)
        color.gradient(col_grad[0], col_grad[1])
        effect.snake(0.5)

        cycle_beats(4/3,2)
        elements(el)
        color.gradient(col_grad[0], col_grad[1])
        effect.snake(0.5)
        for e in all+[sheep.sheep]:
            e.straight
    cycle_beats(2,3)
    for elem_s in elem_strong:
        elements(elem_s)
        color.gradient(col_grad[0], col_grad[1])
        effect.snake(4)

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
episode(8)
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

episode(9)
cycle(32)
cycle_beats(0,6)
elements(cabbages)
color.uniform(purple_string)
effect.snake(3)
cycle_beats(0,6)
elements(brains)
color.uniform(purple_string)
effect.snake(3)
cycle_beats(2,12)
elements(single_sticks,single_lifas)
color.uniform(purple_string)
effect.snake()
cycle_beats(8,18)
elements(single_sticks,single_lifas)
color.uniform(purple_string)
effect.breath()

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

cycle_beats(24,30)
elements(cabbages)
color.uniform(purple_string)
effect.snake(3)
cycle_beats(24,30)
elements(brains)
color.uniform(purple_string)
effect.snake(3)
cycle_beats(26,32)
elements(single_sticks,single_lifas)
color.uniform(purple_string)
effect.snake()

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
elements(cabbages,bottles)
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
episode(12)
bling(sticks3,purple_strip)

episodes(12,15)
cycle(8)
elements(flowers,cabbages,brains,cup_cakes)
color.gradient(indigo[0],green[0])
effect.snake()

episode(14)
bling(lifas4,yellow_string)


# episodes(15,17)
# cycle(4)
# elements(all)
# color.gradient(indigo[0],green[0])
# effect.breath()

# for e in sticks:
#     e.random
# fast(13*32, 14*32, [sticks7],[sticks7.stand(1),sticks7.stand(2),sticks7.stand(3),sticks7.stand(4),sticks7.stand(5)],[purple_strip[0],purple_strip[0]])
fast(13*32, 14*32, [cup_cake3],[cup_cake3],[0.14,8])


episodes(14,16)
cycle(8)
elements(not_tubes)
color.uniform(aquamarine)
effect.breath()
fast(14*32, 15*32, [sticks],[single_sticks],[0.14,0.8])



# for el in all: #[cabbage1,cabbage5,cabbage6,brain7,flower6,flower1,paper5,paper2,donut1,donut3]:
#     el.random

fast(15*32, 16*32, [sticks,lifas],[single_sticks,single_lifas,strings,cup_cakes],[0.14,0.8])
fast(512,550, [all],[single_sticks,single_lifas,not_tubes],[0.14,0.8])

# for el in all: #[cabbage1,cabbage5,cabbage6,brain7,flower6,flower1,paper5,paper2,donut1,donut3]:
#     el.straight

episodes(15,21)
cycle(8)
elements(cabbages,brains)
color.uniform(aquamarine)
effect.snake()


episode(15)
bling(sticks7,coral)

p_end_beat = 640

beats(548,600)
cycle(1)
elements(single_lifas,single_sticks)
color.uniform(purple_string)
effect.snake()

beats(550,p_end_beat)
cycle(2)
cycle_beats(1,2)
elements(flowers)
color.gradient(turquoise_string[0],coral[0])
effect.blink()

beats(558,p_end_beat)
cycle(2)
cycle_beats(1,2)
elements(cup_cakes)
color.gradient(turquoise_string[0],coral[0])
effect.blink()

beats(566,p_end_beat)
cycle(2)
cycle_beats(1,2)
elements(papers)
color.gradient(turquoise_string[0],coral[0])
effect.blink()

beats(574,p_end_beat)
cycle(2)
cycle_beats(1,2)
elements(rugs)
color.gradient(turquoise_string[0],coral[0])
effect.blink()

beats(582,p_end_beat)
cycle(2)
cycle_beats(1,2)
elements(bottles)
color.gradient(turquoise_string[0],coral[0])
effect.blink()

beats(590,p_end_beat)
cycle(2)
cycle_beats(1,2)
elements(lifas)
color.gradient(turquoise_string[0],coral[0])
effect.blink()

beats(600,p_end_beat)
cycle(2)
cycle_beats(1,2)
elements(sticks)
color.gradient(turquoise_string[0],coral[0])
effect.blink()

bling_b(604,sticks3,green)
bling_b(637,lifas5,coral)

episode(20)
cycle(8)
elements(all)
color.gradient(turquoise_string[0],coral[0])
effect.hue_breath(0.2)

episode(21)
cycle(8)
elements(all)
color.gradient(turquoise_string[0],coral[0])
effect.hue_breath(0.4)

episodes(20,22)
cycle(2)
elements(papers,rugs)
color.uniform(coral)
effect.saw_tooth()

episode(21)
cycle(32)
cycle_beats(24,32)
elements(all)
effect.fade_out()

last_blinking = [sheep.sheep,flower6,meduza.meduza,cup_cakes]
fast(664,696,last_blinking,last_blinking,[0,1])
fast(696,716,last_blinking,last_blinking,[0,1])

# bling_b(668,sticks8,aquamarine)
beats(668, 676)
elements(all)
color.gradient(0,1)
effect.snake()

episodes(22,24)
cycle(32)
for b,e in enumerate(all+[cup_cake3,cup_cake4,flower1,flower6,paper2,paper5]):
    cycle_beats(b,b+4)
    e.random
    elements(e)
    color.gradient(turquoise_string[0],coral[0])
    effect.snake()
    effect.fade_out()
    e.straight

# cycle(32)
# for b,e in enumerate(all):
#     cycle_beats(b,b+4)
#     e.random
#     elements(e)
#     color.gradient(turquoise_string[0],coral[0])
#     effect.snake()
#     effect.fade_out()
#     e.straight
# for b,e in enumerate(all):
#     cycle_beats(b+2,b+6)
#     e.random
#     elements(e)
#     color.gradient(turquoise_string[0],coral[0])
#     effect.snake()
#     effect.fade_out()
#     e.straight
# for b,e in enumerate(all):
#     cycle_beats(b+4,b+8)
#     e.random
#     elements(e)
#     color.gradient(turquoise_string[0],coral[0])
#     effect.snake()
#     effect.fade_out()
#     e.straight
# for b,e in enumerate([cup_cake3,cup_cake4,flower1,flower6,paper2,paper5]):
#     cycle_beats(b+23,b+27)
#     e.random
#     elements(e)
#     color.gradient(turquoise_string[0],coral[0])
#     effect.snake()
#     effect.fade_out()
#     e.straight


beats(32*22,32*22+24)
cycle(2)
elements(papers,rugs)
color.uniform(coral)
effect.saw_tooth()
beats(32*22+16,32*22+24)
elements(papers,rugs)
effect.fade_out()
episode(22)
elements(papers,rugs)
effect.fill_out()



episode(24)
cycle(0.1)
elements(all)
color.gradient(0,0.07)
effect.random_brightness()
cycle(32)
for e in all:
    e.random
effect.fill_in_out()

for e in all:
    e.random
episode(25)
cycle(32)
elements(all)
color.uniform(indigo)
effect.snake(2)
for e in all:
    e.straight

episode(26)
cycle(32)
elements(all)
color.uniform(indigo)
effect.snake()

episode(23)
cycle(32)
elements(sticks8)
color.gradient(0,1)
effect.fill()

episodes(24,29)
cycle(4)
elements(sticks8)
color.gradient(0,1)
effect.hue_breath()

episode(28)
cycle(32)
elements(sticks8)
color.gradient(0,1)
effect.fade_out()

send_to_mqtt("outlier")
start_song("outlier",0)#16.4*28)#offset in seconds


