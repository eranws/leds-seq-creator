from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.flood import cup_cakes, cup_cake3, rug6, rugs, rug4
from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles, flower1, paper2, bottle5, bottle4
from led_objects.objects_selector import elements
from led_objects.sheep import sheep
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands, \
    single_stands, single_lifas
from led_objects.meduza import meduza
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=124, beats_per_episode=64,start_offset = 3)


''' Episode 0: groups blink, siren on stands '''
#main_beat
episodes(0, 1)
cycle(2)
#cycle_beats(0,1)
elements(flower1,paper2,cup_cake3)
color.alternate(pink_string,light_pink_strip)
effect.blink(medium)
#cycle_beats(1,2)
elements(paper5,flower6,cabbage5)
color.alternate(turquoise_string,light_turquoise_strip)
effect.blink(medium, True)


#siren
episodes (0+8/64, 1)
cycle(16)
cycle_beats(0,4)
elements(sticks)
color.gradient(0.0,0.11)
effect.breath(medium)


''' Episodes 1, 2:
- Siren: continue on stands, change mood
- Drums: blinking cabbages, start on episode 2
- Main Beat: blink between groups  
'''

#main_beat  (30s)
episodes(1, 3)
cycle(2)
cycle_beats(0,1)
elements(paper2,cup_cake3,rugs,donut1,flower1)
color.gradient(0.61,0.995)
cycle_beats(1,2)
elements(paper5,flower6,cup_cake4,donut3)
color.gradient(0.39,0.695)


#drums
episodes(2, 3)
elements(cabbages)
cycle(1/3)
color.uniform(light_pink_strip)
effect.breath(soft)

#siren
episodes(1, 3)
elements(single_sticks,single_stands)
cycle(32)
cycle_beats(0,6)
color.alternate(red,orange_strip,10)
effect.snake_up_down()
cycle_beats(16,20)
color.alternate(red,orange_strip,10)
effect.snake()


"""
Episodes 3 
"""

# episode3-4
#drama
wanted_elements = [group1, group2, group3, group4, group5, group6, [group7, group8], [] ]
current_elements = []
current_beat = 192
for element in wanted_elements:
    current_elements.append(element)
    beats(current_beat, current_beat + 8)
    cycle(1/2)
    elements(current_elements)
    color.uniform(indigo)
    effect.saw_tooth(total)
    current_beat += 8

color.uniform(red)
effect.saw_tooth(total)

"""
Epiosde 4, first 8 beats
Slow Effect: drama drops, snakes turn off the scene
"""

#fast drop   (120s)
beats(256,257)
elements(single_stands)
color.uniform(red)
effect.snake(1,switch_direction=True)

#slow drop
beats(256,262)
elements(cup_cake4,cup_cake4,cabbages,paper2)
color.uniform(light_pink_strip)
effect.snake(1,switch_direction=True)

beats(256,262)
elements(meduza)
color.uniform(light_pink_strip)
effect.fade_out()

"""
Episodes 4, 5. start after drop ((120s)
"""


def light_one(start_beat, element, c1,c2,c3):
    cycle_beats(start_beat, start_beat + 1)
    elements(element)
    color.alternate(c1,c2,c3)
    effect.saw_tooth(edge=medium)


#main_beat - 3/8
episodes (4 + 1/8, 4 + 4/8)
cycle(8)
light_one(0, cabbage1, blue,green,15)
light_one(1, cabbage5, green,yellow_string,20)
light_one(2, brain7, yellow_string,orange_strip,10)
light_one(3, cup_cake3, blue,red,30)
light_one(4, donut3, pink_string,purple_string,20)
light_one(5, cup_cake4, yellow_string,pink_string,25)
light_one(6, paper2, blue,light_pink_strip,10)
light_one(7, flower1, red, pink_string,5)

elements(all)
cycle(None)
effect.hue_shift_steps(8, 0.25)


"""
sticks 8 doing something special, lead beat - white blink
"""
episodes (4.5,6)
elements(sticks8)
cycle(1/3)
color.uniform((0.98, 0.45, 1))
effect.blink()


"""
main_beat - next 4/8
"""
episodes (4 + 4/8, 4 + 8/8)
cycle(8)
light_one(0, [cabbage1, flower6,cup_cake4], green,light_turquoise_strip,10)
light_one(1, [cabbage5,rug6, paper5,donut3], turquoise_string,light_pink_strip,10)
light_one(2, [brain7,flower6,flower1], yellow_string,orange_strip,25)
light_one(3, [cup_cake3,paper2,bottle5], blue,red,10)
light_one(4, [donut3,cabbage1,rug4, brain7], purple_string,pink_string,5)
light_one(5, [cup_cake4,bottle4,cabbage5], blue, coral,6)
light_one(6, [paper2,rug6,flower6], green,light_purple_strip,10)
light_one(7, [flower1,brain7,cup_cake4], aquamarine,turquoise_string,25)

elements(all)
effect.hue_shift_steps(8, 0.25)

"""
main_beat - next 4/8
"""
episodes(5, 5.5)
cycle(8)
light_one(0, [cabbage1, flower6,cup_cake4,bottle4], dark_green,light_green,20)
light_one(1, [cabbage5,paper5,donut3,rug6], light_purple_string,pink_string,15)
light_one(2, [brain7,flower6,flower1,paper5], light_turquoise_strip,indigo,10)
light_one(3, [cup_cake3,paper2,bottle5, cabbage1], light_yellow_string,orange_strip,15)
light_one(4, [donut3,cabbage1,brain7,paper2], indigo,light_purple_strip,5)
light_one(5, [cup_cake4,bottle4,cabbage5,cabbage1], yellow_string,aquamarine,10)
light_one(6, [paper2,rug6,flower6,bottle5], red,light_coral,8)
light_one(7, [flower1,brain7,cup_cake4,cabbage5], light_coral,yellow_string,10)

elements(all)
effect.hue_shift_steps(8, 0.25)

"""
main_beat - next 4/8
"""
episodes (5.5, 6)
cycle(8)

light_one(0, [group1,group4], light_yellow_string,orange_strip,15)
light_one(1, [group6,group7,group8], yellow_string,aquamarine,10)
light_one(2, [group2,group3], light_coral,yellow_string,5)
light_one(3, [group5,group7], purple_string,pink_string,5)
light_one(4, [group1,group3], light_coral,yellow_string,10)
light_one(5, [group5,group2],  yellow_string,orange_strip,25)
light_one(6, [group1,group3], turquoise_string,light_pink_strip,10)
light_one(7, [group5,group8,group2], red,light_coral,8)

elements(all)
effect.hue_shift_steps(8, 0.25)


"""
end of episodes 4,5 - drop in last beat
"""
beats(384,385)
elements(single_stands)
color.uniform(red)
effect.snake(0.5,switch_direction=True)


"""
Episode 6: (180s)
breath: some elements, calm
snake on cabbeges, building drama on last 5/8 - 7/8
drama at end: all blink white, prepare for episode 7
"""

episode(6)
cycle(8)
elements(paper2,cup_cakes,flowers,paper5)
color.gradient(turquoise_string[0],aquamarine[0])
effect.breath(total)


episodes(6 + 5/8, 6+7/8)
cycle(1)
elements(cabbages)
color.uniform(orange_strip)
effect.snake()

#drama
episodes(6 + 7/8, 6+8/8)
cycle(1)
elements(all,sheep)
color.uniform(light_pink_strip)
effect.blink(medium)

"""
episode 7: drama. groups blink and group fade with snake (210s)
"""

def blink_part(part_8, e, c_blink_a,c_blink_b):
    episodes(7 + (part_8)/8, 7 + (part_8+1)/8)
    cycle(1)
    elements(e)
    color.gradient(c_blink_a,c_blink_b)
    effect.saw_tooth()

def snake_part(part_8, e, c_snake_a,c_snake_b):
    # one beat of drop
    episodes(7 + (part_8+1)/8, 7 + (part_8+1)/8 + 1/64)
    elements(e)
    color.gradient(c_snake_a,c_snake_b)
    effect.snake()

def blink_and_snake_group(part_8, e, c_blink_a,c_blink_b, c_snake_a,c_snake_b):
    blink_part(part_8, e, c_blink_a,c_blink_b)
    snake_part(part_8, e,c_snake_a,c_snake_b)


blink_and_snake_group(0, group1, coral[0], coral[0],coral[0], coral[0])
blink_and_snake_group(1, [group2, group3], turquoise_string[0], indigo[0], turquoise_string[0], indigo[0])
blink_and_snake_group(2, [group4, group5], purple_string[0], light_purple_strip[0], purple_string[0], blue[0])

blink_part(3, [group6,group7,group8], dark_green[0],aquamarine[0] )

#drop all scene with snakes
beats(479,480)
elements(all)
color.uniform(light_pink_strip)
effect.snake()

"""
Episodes: 7.5 - 8.5
equilaizer on sticks, add graduately
"""

def sticks_eq(e):
    elements(e)
    cycle(4/3)
    color.gradient(0.4, 0.55)
    effect.snake_down_up(1.0)


episodes(7.5, 8.5)
sticks_eq(sticks8)

episodes(7.5 + 1/8, 8.5)
sticks_eq(sticks7)

episodes(7.5 + 2/8, 8.5)
sticks_eq(sticks3)



"""
Episode 8:
we had equilaizer on the sticks until 8.5
before sticks removed, drama start - shine with red
"""

beats(536,552)
cycle(2/3)
elements(group1,group2,cup_cakes,donuts,group4,group5,group6,cabbages,brains,rugs,meduza,sheep)
color.uniform(purple_string)
effect.breath(hard)
cycle(16)
effect.saw_tooth(total, True)

"""
darama start - all blink colorful (240s)
"""

beats(552,576)
cycle(1/3)
elements(all)
color.gradient(magenta[0],light_coral[0])
effect.breath()


beats(576,592)
cycle(4)
cycle_beats(0,2)
elements(group1,group2,group3,group8,flower6)
color.alternate(orange_strip,coral,10)
effect.blink_repeat(6, 0.2)
cycle_beats(2,4)
elements(group4,group5,group7,rug6,cabbage6)
color.alternate(dark_green,yellow_string,10)
effect.blink_repeat(6, 0.2)

beats(592,608)
cycle(2)
cycle_beats(0,1)
elements(group1,group2,group3,group8,flower6)
color.alternate(orange_strip,coral,10)
effect.blink_repeat(3, 0.2)
cycle_beats(1,2)
elements(group4,group5,group7,rug6,cabbage6)
color.alternate(dark_green,light_yellow_string,10)
effect.blink_repeat(3, 0.2)

beats(608,624)
cycle(4)
cycle_beats(0,2)
elements(group1,group2,group3,group8,flower6)
color.alternate(indigo,turquoise_string,10)
effect.blink_repeat(6, 0.2)
cycle_beats(2,4)
elements(group4,group5,group7,rug6,cabbage6)
color.alternate(light_aquamarine,green,10)
effect.blink_repeat(6, 0.2)

beats(624,640)
cycle(2)
cycle_beats(0,1)
elements(group1,group2,group3,group8,flower6)
color.alternate(indigo,turquoise_string,10)
effect.blink_repeat(3, 0.2)
cycle_beats(1,2)
elements(group4,group5,group7,rug6,cabbage6)
color.alternate(light_aquamarine,green,10)
effect.blink_repeat(3, 0.2)

beats(640,656)

cycle(2)
cycle_beats(0,1)
elements(group1,group2,group3,group8,flower6)
color.alternate(light_green,green,10)
effect.blink_repeat(3, 0.2)
cycle_beats(1,2)
elements(group4,group5,group7,rug6,cabbage6)
color.alternate(light_pink_strip,orange_strip,10)
effect.blink_repeat(3, 0.2)

beats(656,671)
cycle(4)
cycle_beats(0,2)
elements(group1,group2,group3,group8,flower6)
color.alternate(yellow_string,coral,10)
effect.blink_repeat(6, 0.2)
cycle_beats(2,4)
elements(group4,group5,group7,rug6,cabbage6)
color.alternate(light_pink_strip,orange_strip,10)
effect.blink_repeat(6, 0.2)


"""
drama - part 2
"""

def light_8_beats(beats_start, e):
    beats(beats_start, beats_start + 8)
    cycle(1)
    elements(e)

light_8_beats(672, all)
color.alternate(indigo,turquoise_string,10)
effect.snake()

# drum - make one beat of white (320s)
beats(672,673)
elements(all,meduza)
color.uniform(black)
elements(stands,cabbages,meduza)
color.uniform(light_pink_strip)
effect.saw_tooth()

paper2.random
flower1.random
flower6.random
cup_cake3.random
cup_cake4.random

light_8_beats(680, [group1,group3,group5])
color.alternate(coral,light_pink_strip,10)
effect.snake()

light_8_beats(688, [group2,group6,group4,group7,group8])
color.alternate(light_pink_strip,orange_strip,10)
effect.snake()

light_8_beats(696, [stands])
color.alternate(turquoise_string,dark_blue,10)
effect.snake()

light_8_beats(704, [papers,cup_cakes,donuts,cabbages])
color.alternate(green,light_green,10)
effect.snake()

light_8_beats(712, [flowers,lifas,papers,cup_cakes,sticks3,donut3,bottles,rugs])
color.alternate(pink_string,yellow_string,10)
effect.snake()

light_8_beats(720, [sticks8,sticks7,cabbages,brain7])
color.alternate(pink_string,indigo,10)
effect.snake()

light_8_beats(728, [all])
color.gradient(0,1)
effect.snake()
#drums

paper2.random
flower6.random
flower1.random
paper5.random

beats (736,808)
cycle(32)
cycle_beats(0,12)
elements(paper2,flowers,paper5)
color.uniform(turquoise_string)
effect.snake()
cycle_beats(12,32)
elements(paper2,flowers, paper5)
color.uniform(pink_string)
effect.snake()

beats(736,832)
cycle(2)
elements(cup_cake3)
cycle_beats(0,1)
color.uniform(light_coral)
effect.saw_tooth(soft)
effect.blink_repeat(3)
cycle_beats(1,2)
color.uniform(orange)
effect.saw_tooth(soft)

cycle(None)
beats(782,834)
effect.fade_out()



beats(828,840)
cycle(12)
elements(single_lifas)
color.uniform(purple_string)
effect.snake(0.4,True)

beats(840,844)
elements(meduza,sheep)
color.uniform(purple_string)
effect.breath(1.0)

send_to_mqtt("millenium")
start_song("millenium", 350)