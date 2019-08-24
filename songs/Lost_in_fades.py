from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, load
from infra.timing import beats
from led_objects.cabbages import cabbage1, cabbage6, brain7, cabbage5, cabbages, brains, donut1, donut3, donuts
from led_objects.flood import cup_cakes, cup_cake3, cup_cake4, rugs
from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.led_object import all
from led_objects.sheep import  sheep
from led_objects.flowers import *
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, \
    sticks7, sticks3, lifas5, lifas1, lifas4, lifas, stands
from led_objects.meduza import  meduza
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats
from infra.colors import *

song_settings(bpm=118, beats_per_episode=8,start_offset = 3)
episode_length = 8
background_elements = [sheep, cup_cake4] + cabbages + brains + donuts + rugs + flowers + bottles
def snakes_grdiant(first_episode, last_episode, fade_out_intense=0):
    episodes(first_episode, last_episode)
    elements(background_elements + [stands + cup_cakes + brains + papers, meduza])
    cycle(2)
    color.gradient(0.61,0.46)
    effect.snake(0.2)
    effect.hue_breath()
    number_of_episodes = last_episode - first_episode
    cycle(number_of_episodes*episode_length)
    effect.saw_tooth(edge=fade_out_intense)
snakes_grdiant(0,4)


#Snear
def snear(episodes_p):
    episodes(episodes_p[0], episodes_p[1])
    elements(cup_cake3)
    color.uniform(light_indigo)
    cycle(1)
    effect.blink()
snear([4,12])

episodes(6, 9)
elements(sticks3.stand(1), sticks3.stand(2), sticks3.stand(3), sticks3.stand(4), sticks3.stand(5),
         sticks7.stand(1), sticks7.stand(2), sticks7.stand(3), sticks7.stand(4), sticks7.stand(5),
         sticks8.stand(1), sticks8.stand(2), sticks8.stand(3), sticks8.stand(4), sticks8.stand(5),
         lifas5.stand(1), lifas5.stand(2), lifas5.stand(3), lifas5.stand(4), lifas5.stand(5),
        lifas4.stand(1), lifas4.stand(2), lifas4.stand(3), lifas4.stand(4),
         lifas1.stand(1), lifas1.stand(2), lifas1.stand(3), lifas1.stand(4), lifas1.stand(5),
         )
cycle(4)
color.gradient(5/12, 6/12)
effect.snake_up_down(1)

episodes(6, 10)
elements(flowers, bottles, cabbages, donuts, rugs)#, sticks7, sticks8)
cycle(8)
color.gradient(6/12, 8/12)
#effect.breath(1)


def vocalUpAndDown(first_beat, last_beat):
    beats(first_beat,last_beat)
    cycle(last_beat-first_beat)
    elements(papers)
    color.gradient(0.995,1)
    effect.hue_breath(soft)
    effect.breath(0.8)
#Ahhh
vocalUpAndDown(72,81)
#rain_drifting_on_the_cloudy_water
vocalUpAndDown(98,112)
#rain drops shooting our reflection
vocalUpAndDown(116,131)

beats(116, 150)
elements(bottles, flowers, cabbages, rugs, cup_cakes, stands, donuts)
cycle(150-116)
color.uniform([7/12,1,1])
effect.hue_saw_tooth(4/12)

#Lost in fades
vocalUpAndDown(131,150)
#in the fades
vocalUpAndDown(175,178)

episodes(18, 22)
cycle(7)
first_beat=0
def groups_cycle(group):
    global first_beat
    cycle_beats(first_beat,first_beat+1)
    elements(group)
    color.gradient(0.5,0.75)
    first_beat = (first_beat + 1) % 7
groups_cycle(group1)
#groups_cycle(group2,1)
groups_cycle(group3)
groups_cycle(group4)
groups_cycle([paper5, lifas5, bottle5, cabbage5])
groups_cycle(group6)
groups_cycle(group7)
groups_cycle(group8)



def  grrrrr(first_episode, last_episode):
    episodes(first_episode, last_episode)
    elements(meduza)
    cycle(4)
    cycle_beats(1,2)
    color.uniform(purple_strip)
    effect.blink_repeat(16)
grrrrr(22,30)


snear([26,30])

episodes(26,30)
elements(background_elements)
cycle(2)
#effect.blink()
cycle_beats(0,1)
color.alternate(indigo, aquamarine)
cycle_beats(1,2)
color.alternate(aquamarine, indigo)


episodes(30,32)
elems = background_elements + brains + cup_cakes
for e in elems:
    e.random
elements(elems)
cycle(2)
color.gradient(9/12,6/12)
effect.snake()

episodes(32,34)
elements(background_elements + [stands, brains, cup_cakes])
cycle(2)
color.alternate(indigo, light_blue, number_of_pixels=10)
effect.snake()

#Ahhh
vocalUpAndDown(216,226)
#rain_drifting_on_the_cloudy_water
vocalUpAndDown(242,256)
#rain drops shooting our reflection
vocalUpAndDown(260,272)
#rain_drifting_on_the_cloudy_water
vocalUpAndDown(290,302)
#rain drops shooting our reflection
vocalUpAndDown(308,320)
#Lost in fades
vocalUpAndDown(324,336)


def pattern(first_episode, last_episode, stand_elements, stand_colors,double=False):
    for element in stand_elements:
        episodes(first_episode, last_episode)
        cycle(4)
        offset = 1.25

        cycle_beats(0,offset)
        elements(element.stand(5))
        color.uniform(indigo)

        #stand_color = light_turquoise_string
        cycle_beats(offset,offset + 0.25)
        elements(element.stand(1))
        color.gradient(stand_colors[0], stand_colors[1])
        if double:
            effect.blink_repeat(2)

        cycle_beats(offset + 0.25, offset + 0.5)
        elements(element.stand(2))
        color.gradient(stand_colors[0], stand_colors[1])
        if double:
            effect.blink_repeat(2)

        cycle_beats(offset + 0.5, offset + 0.75)
        elements(element.stand(3))
        color.gradient(stand_colors[0], stand_colors[1])
        if double:
            effect.blink_repeat(2)

        cycle_beats(offset + 0.75,offset + 1.25)
        elements(element.stand(4))
        color.gradient(stand_colors[0], stand_colors[1])
        if double:
            effect.blink_repeat(2)

        cycle_beats(offset + 1.25, offset + 1.5)
        elements(element.stand(1))
        color.gradient(stand_colors[0], stand_colors[1])
        if double:
            effect.blink_repeat(2)

        cycle_beats(offset + 1.5, offset + 2)
        elements(element.stand(2))
        color.gradient(stand_colors[0], stand_colors[1])
        if double:
            effect.blink_repeat(2)

        cycle_beats(offset + 2, offset + 2.25)
        elements(element.stand(3))
        color.gradient(stand_colors[0], stand_colors[1])
        if double:
            effect.blink_repeat(2)

        cycle_beats(offset + 2.25, offset + 2.75)
        elements(element.stand(4))
        color.gradient(stand_colors[0], stand_colors[1])
        if double:
            effect.blink_repeat(2)


pattern(35,42, [sticks8], [0.61,9/12])#sticks8)
pattern(42,46, [lifas1, lifas5, sticks3,sticks7,sticks8], [9/12,0.61])

episodes(42,46)
cycle(1)
elements(cabbages, brains, donuts, bottles, flowers, rugs, cup_cakes)
color.uniform([0.7,1,1])
effect.saw_tooth(reverse=True)

grrrrr(46,58)
pattern(46,50,  [lifas1, lifas5, sticks3,sticks7,sticks8], [0.61,9/12], double=True)
pattern(50,54,  [lifas1, lifas5, sticks3,sticks7,sticks8], [9/12,0.61], double=True)


elems = background_elements + brains + cup_cakes
for e in elems:
    e.straight

episodes(50,54)
cycle(8)
elements(background_elements)#flowers, bottles)
color.uniform(turquoise_string)
#effect.saw_tooth(reverse=True)
#effect.hue_breath()
effect.fill_in_out()


pattern(54,58,  [lifas1, lifas5, sticks3,sticks7,sticks8], [0.61,9/12], double=True)

#Ammm
vocalUpAndDown(432,440)
#Lost in fades
vocalUpAndDown(451,467)

snakes_grdiant(58,62)
snakes_grdiant(62,65)
snakes_grdiant(65,66, fade_out_intense=1)

send_to_mqtt("lost")
start_song("lost", 49*8*60/118+0)