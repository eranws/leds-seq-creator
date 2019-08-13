from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cabbage5, cabbages, brains, donut1, donut3, twists, donuts
from led_objects.flood import floods
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, strings, flower1, bottles, papers
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, lifas, single_lifas, \
    stands
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=126, beats_per_episode=32)

# big entrance with fade out
episodes(0, 0.5)
elements(twists, donuts, flowers, floods, strings)
cycle(beats=2.5)
color.uniform(indigo)
effect.saw_tooth()
cycle(None)
effect.saw_tooth(edge=hard, reverse=False)

# fade in for main beat
episodes(0.5, 1)
elements(stands)
cycle(beats=2)
color.uniform(indigo)
effect.saw_tooth()
cycle(None)
effect.saw_tooth(edge=hard, reverse=True)

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

# cabbages and strings hold the main beat
episodes(1, 3)
elements(cabbages)
cycle(beats=2/3)
color.uniform(pink_strip)
effect.breath(edge=soft)

episodes(3, 8)
elements(cabbages)
cycle(2/3)
color.uniform(turquoise_strip)
effect.breath(edge=soft)

elements(strings)
cycle(2)
color.alternate(turquoise_strip, green)
effect.blink()

# floods for violins
episodes(5, 9)
elements(floods)
cycle(8)
cycle_beats(0, 4)
color.gradient(0.2, 0.6)
effect.snake(tail=0.5)

beats(187, 191)
elements(floods)
color.gradient(0.2, 0.6)
effect.snake(tail=0.5, switch_direction=True)
beats(219, 223)
elements(floods)
color.gradient(0.2, 0.6)
effect.snake(tail=0.5, switch_direction=True)
beats(251, 255)
elements(floods)
color.gradient(0.2, 0.6)
effect.snake(tail=0.5, switch_direction=True)
beats(285, 288)
elements(floods)
color.gradient(0.2, 0.6)
effect.snake(tail=0.5, switch_direction=True)

# papers for crash at beginning of episode 7
beats(222, 230)
elements(papers)
color.uniform((1.0, 0.0, 1.0))
effect.saw_tooth(total, reverse=True)

# stands along episode 8 for increasing tempo
episodes(8, 9)
cycle(2/3)
elements(stands)
color.uniform(turquoise_strip)
effect.saw_tooth()
cycle(None)
effect.saw_tooth(edge=hard, reverse=True)

# strong violins
episodes(9, 10.75)
cycle(8)
elements(floods, cabbages, papers)
color.uniform(dark_green)
effect.saw_tooth(total, reverse=False)

# episode 10 continues violins and restores beat
episodes(10, 10.75)
elements(flowers)
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

episodes(10.75, 11)
elements(floods, cabbages, papers)
color.uniform(dark_green)
effect.breath(total)

# return to main beat with cabbages and strings
episodes(11, 16)
elements(cabbages)
cycle(2/3)
color.uniform(turquoise_strip)
effect.breath(edge=soft)

elements(strings)
cycle(2)
color.alternate(turquoise_strip, green)
effect.blink()

# floods for violins
episodes(12, 14)
elements(floods)
cycle(8)
cycle_beats(0, 4)
color.gradient(0.2, 0.6)
effect.snake(tail=0.5)

#change violin ends to match episodes 12 to 14
beats(187, 191)
elements(floods)
color.gradient(0.2, 0.6)
effect.snake(tail=0.5, switch_direction=True)
beats(219, 223)
elements(floods)
color.gradient(0.2, 0.6)
effect.snake(tail=0.5, switch_direction=True)
beats(251, 255)
elements(floods)
color.gradient(0.2, 0.6)
effect.snake(tail=0.5, switch_direction=True)
beats(285, 288)
elements(floods)
color.gradient(0.2, 0.6)
effect.snake(tail=0.5, switch_direction=True)

# episodes 13, 14 increasing to crash

# episodes 15,16 high level remains

# episodes 17,18 stay like 15,16 but adds violins

# episodes 19, 20 violin only

# episodes 21, 22 drama violin added to drama crash

# episodes 23, 24 cabbages soft beat only with increasing music over 2 episodes

# episode 25 adds drama violin ending with 2 drama beats

# episodes 26, 27 full beat with music

# episode 28, 29 changes to a little softer beat

# episode 29 second half has downwards music

# episodes 30, 31 fade down music all through 2 episodes to soft crash at end

# episodes 32, 33 continue fade, some drum sounds at end of 33

# episodes 34 continue fade drums at end of 34

# episode 35 final fade, no beat, one element fade to dark

send_to_mqtt("nocturne")
start_song("nocturne", 0*1000)