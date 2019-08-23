from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cabbage5, cabbages, brains, donut1, donut3, cup_cake4
from led_objects.flood import rug6
from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.led_object import all
from led_objects.flowers import *
from led_objects.meduza import meduza
from led_objects.objects_selector import elements
from led_objects.sheep import sheep
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, stands
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=115, beats_per_episode=8, start_offset=3)

#this function is a short animation for a beat where there are three fast sounds tu tu tu, the animations is color blink from soft to bright
def three_beat(initbeat, element_name, color_name, sound_dir):
    beats(initbeat, (initbeat+0.5))
    elements(element_name)
    color.uniform(color_name)
    if sound_dir == 1:
       effect.brightness(0.25)

    if sound_dir == 0:
       effect.brightness(1)


    beats((initbeat+0.5), (initbeat+1))
    elements(element_name)
    color.uniform(color_name)
    effect.brightness(0.55)

    beats((initbeat+1), (initbeat+1.9))
    elements(element_name)
    color.uniform(color_name)
    if sound_dir == 1:
       effect.brightness(1)
    if sound_dir == 0:
       effect.brightness(0.25)

#episode1 - intro
def introanim():
    #effect.hue_saw_tooth(soft)
    effect.breath()


beats(0,8)
elements(group1)
color.uniform(red)
introanim()

beats(1,8)
elements(group2)
color.uniform(orange_string)
introanim()

beats(2,8)
elements(group3)
color.uniform(yellow_string)
introanim()

beats(3,8)
elements(group4)
color.uniform(green)
introanim()

beats(4,8)
elements(group5)
color.uniform(turquoise_string)
introanim()

beats(5,8)
elements(group6)
color.uniform(dark_blue)
introanim()

beats(6,8)
elements(group7)
color.uniform(pink_string)
introanim()

beats(7,8)
elements(group8,meduza,sheep)
color.uniform(purple_string)
introanim()

#song starts - first house
def groupy():
    effect.snake()

beats(8,12)
cycle(beats=1)
elements(group1)
color.uniform(red)
groupy()

beats(12,16)
cycle(beats=1)
elements(group2)
color.uniform(orange_string)
groupy()

beats(16,20)
cycle(beats=1)
elements(group3)
color.uniform(yellow_string)
groupy()

beats(20,24)
cycle(beats=1)
elements(group4)
color.uniform(green)
groupy()

beats(24,28)
cycle(beats=1)
elements(group5)
color.uniform(turquoise_string)
groupy()

beats(28,32)
cycle(beats=1)
elements(group6)
color.uniform(dark_blue)
groupy()

beats(32,36)
cycle(beats=1)
elements(group7)
color.uniform(pink_string)
groupy()

beats(36,40)
cycle(beats=1)
elements(group8, sheep, meduza)
color.uniform(purple_string)
groupy()

#begins singing - delicate and quiet before high break ()
beats(40,73)
elements(group1)
cycle(beats=2)
#color.gradient(0.61,0.995)
color.uniform(light_pink_strip)
effect.hue_breath()

beats(48,73)
elements(group2)
cycle(beats=2)
#color.gradient(0.61,0.995)
color.uniform(light_pink_strip)
effect.hue_breath()

beats(56,73)
elements(group3)
cycle(beats=2)
#color.gradient(0.61,0.995)
color.uniform(light_pink_strip)
effect.hue_breath()

beats(64,72)
elements(group4)
cycle(beats=2)
#color.gradient(0.61,0.995)
color.uniform(light_pink_strip)
effect.hue_breath()

#guitar
def guitarfunc(initbeat):
    #initbeat first is 72
    beats(initbeat, (initbeat+0.67))
    elements(lifas4)
    color.gradient(0.61, 0.995)
    effect.blink()

    beats((initbeat+1.2), (initbeat+2.2))
    elements(donut1)
    color.gradient(0.5, 0.75)
    effect.blink()

    beats((initbeat+3), (initbeat+3.5))
    elements(flower1)
    color.gradient(0.25, 0.5)
    effect.blink()

    beats((initbeat+3.4), (initbeat+4))
    elements(sheep)
    color.gradient(0.25, 0.5)
    effect.blink()

    beats((initbeat+3.8), (initbeat+4.5))
    elements(sticks3)
    color.gradient(0.25, 0.5)
    effect.blink()

    beats((initbeat+5.3), (initbeat+6))
    elements(bottle4)
    color.gradient(0.61, 0.995)
    effect.blink()

    beats((initbeat+6.3), (initbeat+6.8))
    elements(lifas5)
    color.gradient(0.61, 0.995)
    effect.blink()

    beats((initbeat+7), (initbeat+7.8))
    elements(rug6)
    color.gradient(0.61, 0.995)
    effect.blink()

    beats((initbeat+7.4), (initbeat+8.1))
    elements(sheep)
    color.gradient(0.61, 0.995)
    effect.blink()

    beats((initbeat+8.1), (initbeat+8.8))
    elements(brain7)
    color.gradient(0.61, 0.995)
    effect.blink()

    beats((initbeat+9.1), (initbeat+10))
    elements(lifas5)
    color.gradient(0.61, 0.995)
    effect.blink()

    beats((initbeat+10.5), (initbeat+11.2))
    elements(meduza)
    color.gradient(0.61, 0.995)
    effect.blink()

    beats((initbeat+11.2), (initbeat+12))
    elements(bottle4)
    color.gradient(0.61, 0.995)
    effect.blink()

    beats((initbeat+12), (initbeat+13))
    elements(sticks3)
    color.gradient(0.61, 0.995)
    effect.blink()

    beats((initbeat+13.5), (initbeat+14))
    elements(paper2)
    color.gradient(0.1, 0.3)
    effect.blink()

    beats((initbeat+15.3), (initbeat+16))
    elements(donut1)
    color.gradient(0.1, 0.3)
    effect.blink()

    beats((initbeat+16), (initbeat+16.5))
    elements(sheep)
    color.gradient(0.1, 0.3)
    effect.blink()

    beats((initbeat+17), (initbeat+17.5))
    elements(sticks3)
    color.gradient(0.1, 0.3)
    effect.blink()

    beats((initbeat+17.3), (initbeat+17.8))
    elements(lifas5)
    color.gradient(0.1, 0.3)
    effect.blink()

    beats((initbeat+19), (initbeat+20))
    elements(sticks3)
    color.gradient(0.1, 0.3)
    effect.blink()

    beats((initbeat+20.2), (initbeat+20.8))
    elements(lifas5)
    color.gradient(0.1, 0.3)
    effect.blink()

    beats((initbeat+20.8), (initbeat+21.5))
    elements(paper2)
    color.gradient(0.1, 0.3)
    effect.blink()

    beats((initbeat+21.5), (initbeat+22.3))
    elements(bottle4)
    color.gradient(0.1, 0.3)
    effect.blink()

    beats((initbeat+24), (initbeat+25))
    elements(meduza)
    color.gradient(0.1, 0.3)
    effect.blink()

    beats((initbeat+25.5), (initbeat+26.2))
    elements(donut1)
    color.gradient(0.1, 0.3)
    effect.blink()

    beats((initbeat+27), (initbeat+27.8))
    elements(lifas5)
    color.gradient(0.1, 0.3)
    effect.blink()

    beats((initbeat+27.8), (initbeat+28.3))
    elements(rug6)
    color.gradient(0.1, 0.3)
    effect.blink()

    beats((initbeat+28.1), (initbeat+28.9))
    elements(bottle4)
    color.gradient(0.1, 0.3)
    effect.blink()

    beats((initbeat+29.8), (initbeat+30.4))
    elements(sticks3)
    color.gradient(0.1, 0.3)
    effect.blink()

    beats((initbeat+30.5), (initbeat+31.5))
    elements(flower6)
    color.gradient(0.1, 0.3)
    effect.blink()

guitarfunc(72)

#sun lights up the daytime
beats(104,136)
cycle(beats=1)
elements(group1,group2)
color.gradient(0.8,0.9)
effect.breath()


#the moon lights up the night
beats(112,136)
cycle(beats=1)
elements(group3,group4)
color.gradient(0.4,0.5)
effect.snake()


#cat sniff pocahontas
beats(120,136)
cycle(beats=1)
elements(group5,group6)
color.gradient(0.2,0.3)
effect.breath()

#had a very mad affair
beats(128,136)
cycle(beats=1)
elements(group7,group8, sheep, meduza)
color.gradient(0.7,0.8)
effect.snake()


#romeo loves julliette
beats(136,144)
cycle(beats=1)
elements(group1,group2)
color.gradient(0.8,0.9)
effect.breath()


#juliette she felt the same
beats(144,152)
cycle(beats=1)
elements(group3,group4)
color.gradient(0.4,0.5)
effect.breath()


#i light up when you call my name
beats(152,160)
cycle(beats=1)
elements(group1)
color.gradient(0.1,0.2)
effect.breath()

beats(153,160)
cycle(beats=1)
elements(group2)
color.gradient(0.2,0.3)
effect.breath()

beats(154,160)
cycle(beats=1)
elements(group3)
color.gradient(0.3,0.4)
effect.breath()

beats(155,160)
cycle(beats=1)
elements(group4)
color.gradient(0.4,0.5)
effect.breath()

beats(156,160)
cycle(beats=1)
elements(group5)
color.gradient(0.5,0.6)
effect.breath()

beats(157,160)
cycle(beats=1)
elements(group6)
color.gradient(0.6,0.7)
effect.breath()

beats(158,160)
cycle(beats=1)
elements(group7)
color.gradient(0.7,0.8)
effect.breath()

beats(159,160)
cycle(beats=1)
elements(group8)
color.gradient(0.8,0.9)
effect.breath()

#and i know im gonna treat you right you give me fever
beats(160,168)
cycle(beats=2)
elements(all)
cycle_beats(0,1)
color.alternate(magenta,indigo)
effect.breath()
cycle_beats(1,2)
color.alternate(indigo,magenta)
effect.breath()


#instrumental part runs 4*8 beats
#base beat effect on tall elements
beats(168,184)
cycle(beats=1)
elements(lifas1, lifas5, lifas4)
color.uniform(red)
effect.blink()

#background long sound each 4 beats, slow snake changes color
beats(168,184)
cycle(beats=4)
elements(bottle4)
color.uniform(yellow_string)
effect.snake_down_up()

beats(172,184)
cycle(beats=4)
elements(flower1)
color.uniform(coral)
effect.snake_down_up()

beats(176,184)
cycle(beats=4)
elements(brain7)
color.uniform(orange_string)
effect.snake_down_up()

beats(180,184)
cycle(beats=4)
elements(meduza)
color.uniform(magenta)
effect.snake_down_up()

#base beat effect on tall elements
beats(184,200)
cycle(beats=1)
elements(sticks3, sticks8, sticks7)
color.uniform(dark_blue)
effect.blink()

#background long sound each 4 beats, slow snake changes color
beats(184,200)
cycle(beats=4)
elements(bottle5)
color.uniform(aquamarine)
effect.snake_down_up()

beats(188,200)
cycle(beats=4)
elements(flower6)
color.uniform(dark_green)
effect.snake_down_up()

beats(192,200)
cycle(beats=4)
elements(rug6)
color.uniform(light_green)
effect.snake_down_up()

beats(196,200)
cycle(beats=4)
elements(sheep)
color.uniform(turquoise_string)
effect.snake_down_up()

#second instrumental interval, with guitar again 4*8 beats

#base beat
beats(200,216)
cycle(beats=1)
elements(lifas1, lifas5, lifas4)
color.gradient(0,1)
effect.snake()

beats(200,204)
cycle(beats=4)
elements(sheep)
color.gradient(0.5,0.95)
effect.snake()

beats(204,208)
cycle(beats=4)
elements(rug6)
color.gradient(0.5,0.95)
effect.snake()

beats(208,212)
cycle(beats=4)
elements(bottle4)
color.gradient(0.5,0.95)
effect.snake()

beats(212,216)
cycle(beats=4)
elements(brain7)
color.gradient(0.5,0.95)
effect.snake()

#base beat
beats(216,232)
cycle(beats=1)
elements(sticks3, sticks8, sticks7)
color.gradient(0,1)
effect.snake()

beats(216,220)
cycle(beats=4)
elements(paper2)
color.gradient(0,0.47)
effect.snake()

beats(220,224)
cycle(beats=4)
elements(paper5)
color.gradient(0,0.47)
effect.snake()

beats(224,228)
cycle(beats=4)
elements(meduza)
color.gradient(0,0.47)
effect.snake()

beats(228,232)
cycle(beats=4)
elements(sheep)
color.gradient(0,0.47)
effect.snake()

#quiet word song part 4*8 beats
beats(232,240)
cycle(beats=8)
elements(group1, group2)
color.gradient(0.5,0.97)
effect.snake()

beats(240,248)
cycle(beats=8)
elements(group3, group4)
color.gradient(0,0.47)
effect.snake()

beats(248,256)
cycle(beats=8)
elements(group5, group6)
color.gradient(0.5,0.97)
effect.snake()

beats(256,264)
cycle(beats=8)
elements(group7, group8)
color.gradient(0,0.47)
effect.snake()

#quiet part with guitar 4*8 beats
guitarfunc(264)

#song with beat part - repeat anim from before 4*8 beats
#base beat effect on tall elements
beats(296,312)
cycle(beats=1)
elements(lifas1, lifas5, lifas4)
color.uniform(red)
effect.snake()

#background long sound each 4 beats, slow snake changes color
beats(296,312)
cycle(beats=4)
elements(bottle4)
color.uniform(yellow_string)
effect.snake_down_up()

beats(300,312)
cycle(beats=4)
elements(flower1)
color.uniform(coral)
effect.snake_down_up()

beats(304,312)
cycle(beats=4)
elements(brain7)
color.uniform(orange_string)
effect.snake_down_up()

beats(308,312)
cycle(beats=4)
elements(meduza)
color.uniform(magenta)
effect.snake_down_up()



#base beat effect on tall elements
beats(312,328)
cycle(beats=1)
elements(sticks3, sticks8, sticks7)
color.uniform(dark_blue)
effect.snake()

#background long sound each 4 beats, slow snake changes color
beats(312,328)
cycle(beats=4)
elements(bottle5)
color.uniform(aquamarine)
effect.snake_down_up()

beats(316,328)
cycle(beats=4)
elements(flower6)
color.uniform(dark_green)
effect.snake_down_up()

beats(320,328)
cycle(beats=4)
elements(rug6)
color.uniform(light_green)
effect.snake_down_up()

beats(324,328)
cycle(beats=4)
elements(meduza)
color.uniform(turquoise_string)
effect.snake_down_up()

#instrumental high tempo part 4*8 beats beats 328-360
#base beat through the whole bit
beats(328,336)
cycle(beats=1)
elements(lifas5)
color.uniform(yellow_string)
effect.blink()

beats(336,344)
cycle(beats=1)
elements(lifas4)
color.uniform(yellow_string)
effect.blink()

beats(344,352)
cycle(beats=1)
elements(sticks3)
color.uniform(yellow_string)
effect.blink()

beats(352,360)
cycle(beats=1)
elements(sticks7)
color.uniform(yellow_string)
effect.blink()

three_beat(331, cabbage6, pink_string, 1)
three_beat(335, paper2, purple_string, 1)
three_beat(339, brain7, magenta, 0)
three_beat(343, paper5, purple_string, 0)
three_beat(347, bottle4, aquamarine, 1)
three_beat(351, meduza, blue, 1)
three_beat(355, sheep, turquoise_string, 0)

#last bit, beat and fading out

beats(360,392)
cycle(beats=2)
elements(group1)
color.gradient(0,1)
effect.fade_in()

beats(364,392)
cycle(beats=2)
elements(group2)
color.gradient(0,1)
effect.fade_in()

beats(364,392)
cycle(beats=2)
elements(group3)
color.gradient(0,1)
effect.fade_in()

beats(368,392)
cycle(beats=2)
elements(group4)
color.gradient(0,1)
effect.fade_in()

beats(372,392)
cycle(beats=2)
elements(group5)
color.gradient(0,1)
effect.fade_in()

beats(376,392)
cycle(beats=2)
elements(group6)
color.gradient(0,1)
effect.fade_in()

beats(380,392)
cycle(beats=2)
elements(group7)
color.gradient(0,1)
effect.fade_in()

beats(384,392)
cycle(beats=2)
elements(group8, meduza, sheep)
color.gradient(0,1)
effect.fade_in()

beats(388,392)
cycle(beats=2)
elements(all)
color.uniform(yellow_string)
effect.fade_in()

#fade out
beats(392,398)
elements(all)
color.uniform(yellow_string)
effect.fade_out()

send_to_mqtt("fever")
start_song("fever", 0)

# elements(meduza, sheep)
# effect.fade_out()
# effect.blink_repeat(16)
