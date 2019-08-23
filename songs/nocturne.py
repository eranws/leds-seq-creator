from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.meduza import meduza
from led_objects.cabbages import cabbage1, cabbage6, brain7, cabbage5, cabbages, brains, donut1, donut3, twists, donuts
from led_objects.flood import floods, cup_cakes
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, strings, flower1, bottles, papers
from led_objects.objects_selector import elements
from led_objects.sheep import sheep
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, lifas, single_lifas, \
    stands, single_stands
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=126, beats_per_episode=32, start_offset=3)

# episode 0 entrance, fade out and in
# big entrance with fade out
episodes(0, 0.5)
elements(twists, donuts, flowers, floods, strings)
cycle(beats=2.5)
color.uniform(indigo)
effect.saw_tooth()
cycle(None)
effect.fade_out()

# fade in for main beat
episodes(0.5, 1)
elements(stands)
cycle(beats=2)
color.uniform(indigo)
effect.saw_tooth()
cycle(None)
effect.fade_in()

# episodes 1,2 establish main beat
# main beat continues pulsing between sticks and lifas
episodes(1, 3)
elements(single_sticks, single_lifas)
cycle(beats=2)
color.gradient(0.61, 0.995)

cycle_beats(0, 1)
elements(single_lifas)
effect.blink(edge=hard)

cycle_beats(1, 2)
elements(single_sticks)
effect.blink(edge=hard)

# twists and strings hold the main beat
episodes(1, 3)
elements(twists)
cycle(2/3)
color.uniform(pink_strip)
effect.breath(edge=soft)

# beat maintained episodes 3,4,5,6,7
episodes(3, 8)
elements(twists)
cycle(2/3)
color.uniform(turquoise_strip)
effect.breath(edge=soft)

elements(strings)
cycle(2)
color.alternate(turquoise_strip, green)
effect.blink()

elements(twists, strings)
cycle(16)
effect.hue_blink(edge=0.1)

# episodes 5,6,7,8 violins join
# stands for violins
episodes(5, 9)
elements(stands)
cycle(32)
cycle_beats(0, 8)
color.gradient(0.2, 0.6)
effect.snake(tail=1)
cycle_beats(8, 16)
color.gradient(0.4, 0.8)
effect.snake(tail=1)
cycle_beats(16, 24)
color.gradient(0.6, 1.0)
effect.snake(tail=1)
cycle_beats(24, 32)
color.gradient(0.8, 1.2)
effect.snake_up_down(tail=1)

# light crash at end of episode 5
beats(190, 192)
cycle(2/3)
elements(floods)
color.uniform((1.0, 0.0, 1.0))
effect.breath(edge=soft, reverse=True)

# light crash at end of episode 6 with crash at beginning of 7
beats(222, 224)
cycle(2/3)
elements(floods)
color.uniform((1.0, 0.0, 1.0))
effect.breath(edge=soft, reverse=True)
beats(224, 230)
elements(floods)
color.uniform((1.0, 0.0, 1.0))
effect.saw_tooth(total, reverse=False)

# light crash at end of episode 7
beats(254, 256)
cycle(2/3)
elements(floods)
color.uniform(turquoise_strip)
effect.breath(edge=soft, reverse=True)

# along episode 8 increasing tempo
episodes(8, 9)
cycle(2/3)
elements(floods, donuts)
color.uniform(turquoise_strip)
effect.saw_tooth()
cycle(None)
effect.fade_in()

beats(286, 288)
cycle(2/3)
elements(floods)
color.uniform(turquoise_strip)
effect.breath(edge=soft, reverse=True)

# boom at the start of episode 9
beats(288, 290)
elements(floods, donuts)
color.uniform(dark_green)
effect.fade_out()

# episode 9, 10 strong violins
episodes(9, 10.75)
cycle(8)
elements(stands, twists)
color.uniform(dark_green)
effect.snake(tail=1.0)

# episode 10 continues violins and restores beat
episodes(9, 10.75)
elements(strings)
cycle(8)
cycle_beats(0, 2)
color.uniform(yellow_string)
effect.blink(hard)
cycle_beats(2, 4)
color.uniform(orange_string)
effect.blink(hard)
cycle_beats(4, 6)
color.uniform(magenta)
effect.blink(hard)
cycle_beats(6, 6.5)
color.uniform(red)
effect.blink(hard)
cycle_beats(6.5, 7)
color.uniform(red)
effect.blink(hard)
cycle_beats(7, 7.5)
color.uniform(red)
effect.blink(hard)
cycle_beats(7.5, 8)
color.uniform(red)
effect.blink(hard)

episodes(10.75, 11.25)
elements(stands, floods, twists, papers, donuts)
color.uniform(dark_green)
effect.breath(total)

# episodes 11, 12, 13, 14, 15, 16 return to main beat with twists and strings new color
episodes(11, 15)
elements(twists)
cycle(2/3)
color.uniform(aquamarine)
effect.breath(edge=soft)
cycle(16)
effect.hue_blink(edge=0.1)

episodes(11, 15)
elements(strings)
cycle(2)
color.alternate(aquamarine, light_green)
effect.hue_blink(edge=0.1)
cycle(16)
effect.hue_blink(edge=0.1)

# light crash at end of 11
beats(382, 384)
cycle(2/3)
elements(floods)
color.uniform(turquoise_strip)
effect.breath(edge=soft,reverse=True)

# stands for violins
episodes(12, 15)
elements(stands)
cycle(32)
cycle_beats(0, 8)
color.gradient(0.2, 0.3)
effect.fill()
cycle_beats(8, 16)
color.gradient(0.3, 0.4)
effect.fill()
cycle_beats(16, 24)
color.gradient(0.2, 0.3)
effect.fill()
cycle_beats(24, 32)
color.gradient(0.1, 0.2)
effect.fill_in_out()
cycle(None)
effect.saw_tooth(reverse=True)

# light crash at end of 12 and begin of 13
beats(414, 416)
cycle(2/3)
elements(floods)
color.uniform(turquoise_strip)
effect.breath(edge=soft, reverse=True)
beats(416, 422)
elements(floods, donuts)
color.uniform(turquoise_strip)
effect.saw_tooth(total, reverse=False)

# light crash at end of 13
beats(446, 448)
cycle(2/3)
elements(floods)
color.uniform(turquoise_strip)
effect.breath(edge=soft, reverse=True)

# episodes 14 big crash
beats(472, 478)
elements(twists, strings, stands, donuts)
color.uniform(aquamarine)
effect.saw_tooth(reverse=False)

beats(478, 480)
elements(all, meduza, sheep)
color.gradient(0, 1)
cycle(2/3)
effect.blink()

# episodes 15, 16 high level remains
episodes(15, 17)
elements(floods, twists, donuts)
cycle(2/3)
color.gradient(0, 1)
effect.breath(edge=soft)
cycle(16)
effect.hue_blink(edge=0.1)

episodes(15, 19)
elements(strings)
cycle(2)
color.gradient(0, 1)
effect.hue_blink(edge=0.1)
cycle(16)
effect.hue_blink(edge=0.1)

# stands for violins
episodes(15, 19)
elements(stands)
cycle(32)
cycle_beats(0, 8)
color.gradient(0, 1)
effect.segment_breath()
cycle_beats(8, 16)
color.gradient(0, 1)
effect.segment_breath()
cycle_beats(16, 24)
color.gradient(0, 1)
effect.segment_breath()
cycle_beats(24, 32)
color.gradient(0, 1)
effect.segment_saw_tooth()

# episodes 17,18 stay like 15,16
# light crash at end of 17
beats(574, 576)
cycle(2/3)
elements(floods, donuts)
color.gradient(0, 1)
effect.breath(edge=soft, reverse=True)

# episode 18 freak on
beats(584, 588)
elements(floods, donuts)
color.gradient(0, 1)
# no effect on purpose here
beats(588, 600)
elements(floods, donuts)
color.gradient(0, 1)
effect.snake()

# episodes 19, 20 violin
episodes(19, 22.75)
elements(floods)
cycle(2/3)
color.gradient(0, 1)
effect.breath(edge=soft)
cycle(16)
effect.hue_blink(edge=0.1)

episodes(19, 22.75)
elements(single_stands)
cycle(32)
cycle_beats(0, 8)
color.gradient(0, 1)
effect.snake(tail=1)
cycle_beats(8, 16)
color.gradient(0, 1)
effect.snake(tail=1)
cycle_beats(16, 24)
color.gradient(0, 1)
effect.snake(tail=1)
cycle_beats(24, 32)
color.gradient(0, 1)
effect.snake_down_up(tail=1)

# episodes 21, 22 drama violin added to drama crash
episodes(21, 22.75)
elements(strings)
cycle(8)
color.gradient(0, 0.5)
effect.saw_tooth(edge=total)
cycle(16)
effect.hue_blink(edge=0.5)

# episode 22 big crash
beats(728, 732)
elements(twists, strings, stands)
color.gradient(0, 1)
effect.saw_tooth(reverse=False)

beats(732, 734)
elements(all, meduza, sheep)
color.gradient(0, 1)
effect.blink()
beats(734, 734.66)
elements(group1, group2)
color.gradient(0, 1)
effect.fade_out()
beats(734.66, 735.33)
elements(group3, group8, group6)
color.gradient(0, 1)
effect.fade_out()
beats(735.33, 736)
elements(group4, group5, group7)
color.gradient(0, 1)
effect.fade_out()

# episodes 23, 24 twists soft beat only with increasing music over 2 episodes
episodes(23, 24)
cycle(2/3)
elements(cup_cakes)
color.uniform(pink_strip)
effect.breath(edge=soft)
beats(766, 768)
color.uniform(purple_strip)
effect.blink_repeat(16)

episodes(23.5, 25)
elements(twists)
color.gradient(0.61, 0.995)
effect.saw_tooth(reverse=True)
cycle(8)
effect.hue_breath()

episodes(24, 25)
elements(single_sticks)
color.gradient(0.61, 0.995)
effect.saw_tooth(reverse=True)
cycle(8)
effect.hue_breath()

# light crash at end of 24
beats(798, 800)
cycle(2/3)
elements(floods, donuts)
color.gradient(0.61, 0.995)
effect.breath(edge=soft, reverse=True)

# episode 25 adds drama violin ending with 2 drama beats
episodes(25, 27)
elements(strings)
cycle(8)
color.gradient(0, 0.5)
effect.saw_tooth(edge=total)
cycle(16)
effect.hue_blink(edge=0.5)

episodes(25, 26.8)
elements(twists, donuts)
cycle(8)
cycle_beats(0, 2)
color.uniform(aquamarine)
effect.blink(hard)
cycle_beats(2, 4)
color.uniform(turquoise_strip)
effect.blink(hard)
cycle_beats(4, 6)
color.uniform(magenta)
effect.blink(hard)
cycle_beats(6, 6.66)
color.uniform(indigo)
effect.blink(hard)
cycle_beats(6.66, 7.33)
color.uniform(indigo)
effect.blink(hard)
cycle_beats(7.33, 8)
color.uniform(indigo)
effect.blink(hard)

# episode 26 big crash at end
beats(858, 862)
cycle(2)
elements(all)
color.gradient(0, 1)
effect.blink(reverse=True)
beats(862, 862.66)
elements(group1, group2)
color.gradient(0, 1)
effect.fade_out()
beats(862.66, 863.33)
elements(group3, group6, group8)
color.gradient(0, 1)
effect.fade_out()
beats(863.33, 864)
elements(group4, group5, group7)
color.gradient(0, 1)
effect.fade_out()

# episodes 27, 28, 29, 30 full beat with music
episodes(27, 31)
elements(floods, twists)
cycle(2/3)
color.gradient(0, 1)
effect.breath(edge=soft)
cycle(16)
effect.hue_blink(edge=0.1)

episodes(27, 31)
elements(strings, donuts)
cycle(2)
color.gradient(0, 1)
effect.hue_blink(edge=0.1)
cycle(16)
effect.hue_blink(edge=0.1)

# stands for violins
episodes(27, 31)
elements(single_stands)
cycle(32)
cycle_beats(0, 8)
color.gradient(0, 1)
effect.snake(tail=1)
cycle_beats(8, 16)
color.gradient(0, 1)
effect.snake(tail=1)
cycle_beats(16, 24)
color.gradient(0, 1)
effect.snake(tail=1)
cycle_beats(24, 32)
color.gradient(0, 1)
effect.snake_down_up(tail=1)

# episode 29 second half has downwards music

# episodes 31, 32 fade down music all through 2 episodes to soft crash at end
episodes(31, 33)
elements(floods)
cycle(2/3)
color.gradient(0, 1)
effect.breath(edge=soft)
cycle(16)
effect.hue_blink(edge=0.1)

episodes(31, 33)
elements(single_stands)
cycle(32)
cycle_beats(0, 8)
color.gradient(0, 1)
effect.snake(tail=1)
cycle_beats(8, 16)
color.gradient(0, 1)
effect.snake(tail=1)
cycle_beats(16, 24)
color.gradient(0, 1)
effect.snake(tail=1)
cycle_beats(24, 32)
color.gradient(0, 1)
effect.snake_down_up(tail=1)

# some drum sounds at end of 31
beats(1022, 1024)
cycle(2/3)
elements(donuts)
color.gradient(0, 1)
effect.breath(edge=soft, reverse=True)

# some drum sounds at end of 32
beats(1054, 1058)
elements(floods, donuts)
color.gradient(0, 1)
effect.breath(edge=soft, reverse=True)

# episodes 33, 34 fade
episodes(33, 34)
elements(strings)
cycle(2)
color.alternate(pink_strip, purple_strip)
effect.breath()

beats(1062, 1080)
cycle(8)
cycle_beats(0, 1)
color.gradient(pink_strip[0], purple_strip[0])
effect.snake()

# some drum sounds at end of 33
beats(1086, 1088)
cycle(2/3)
elements(floods)
color.uniform(pink_strip)
effect.breath(edge=soft, reverse=True)

episodes(34, 35)
elements(flowers)
cycle(2)
color.alternate(pink_strip, purple_strip)
effect.breath()
cycle(None)
effect.saw_tooth(reverse=True)

beats(1094, 1112)
cycle(8)
cycle_beats(0, 1)
color.gradient(pink_strip[0], purple_strip[0])
effect.snake()

# drum sounds at end of 34
beats(1118, 1120)
cycle(2/3)
elements(floods)
color.uniform(purple_strip)
effect.breath(edge=soft, reverse=True)

# episode 35 final fade, no beat, elements fade to dark
episodes(35, 35.5)
elements(sheep)
color.uniform((1.0, 0.0, 1.0))
effect.fade_out()
elements(meduza)
color.uniform(indigo)
effect.fade_out()

send_to_mqtt("nocturne")
start_song("nocturne", 0)
