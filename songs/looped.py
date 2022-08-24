from infra.animations_factory import color, effect

from led_objects.instances import * 
from led_objects.groups import * 
from led_objects.led_object import all
from led_objects.objects_selector import elements

from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats
from infra.colors import *

song_settings(bpm=120, beats_per_episode=32)

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

episodes(2,4)
cycle(8)
elements(single_sticks,single_lifas)
color.uniform(coral)
effect.snake()

episodes(3,5)
cycle(8)
cycle_beats(4,6)
elements(flowers,papers)
color.gradient(0,0.1)
effect.breath()
cycle_beats(6,8)
elements(flowers,papers)
color.gradient(0,0.1)
effect.breath()

episode(4)
cycle(32)
cycle_beats(4,12)
elements(lifas1)
color.uniform(coral)
effect.snake()

episode(5)
cycle(2)
elements(all)
color.gradient(0,1)
effect.hue_breath()

# episode(1)
# cycle(8)
# elements(all)
# color.uniform(indigo)
# effect.breath()
# cycle(4)
# elements(sticks8)
# color.gradient(0,1)
# effect.hue_breath()
# cycle(8)
# elements(flowers,cabbages,brains)
# color.uniform(indigo)
# effect.snake()
#
# episode(2)
# cycle(4)
# elements(all)
# color.uniform(indigo)
# effect.breath()
#
# cycle(4)
# elements(flowers,cabbages,brains)
# color.uniform(indigo)
# effect.saw_tooth()
#
# cycle(8)
# elements(single_sticks,single_lifas)
# color.uniform(coral)
# effect.snake()
#
# episode(3)
# cycle(4)
# elements(all)
# color.uniform(indigo)
# effect.breath()
#
# cycle(4)
# elements(flowers,cabbages,brains)
# color.uniform(indigo)
# effect.saw_tooth()
#
# cycle(4)
# elements(sticks,lifas)
# color.uniform(coral)
# effect.snake()
#
# cycle(2)
# elements(donuts)
# color.gradient(0.1,.2)
# effect.hue_breath()
#
# episode(4)
# cycle(4)
# elements(all)
# color.uniform(indigo)
# effect.breath()
#
# cycle(2)
# elements(flowers,cabbages,brains)
# color.uniform(blue)
# effect.saw_tooth()
#
# cycle(4)
# elements(sticks,lifas)
# color.uniform(coral)
# effect.snake()
#
# cycle(2)
# elements(donuts)
# color.gradient(0,.1)
# effect.hue_breath()
#
# episode(5)
# cycle(2)
# elements(all)
# color.gradient(0,1)
# effect.hue_breath()
#
# episode(4)
# cycle(4)
# elements(all)
# color.uniform(indigo)
# effect.breath()
#
# cycle(2)
# elements(flowers,cabbages,brains)
# color.uniform(blue)
# effect.saw_tooth()
#
# cycle(4)
# elements(sticks,lifas)
# color.uniform(coral)
# effect.snake()
#
# cycle(2)
# elements(donuts)
# color.gradient(0,1)
# effect.hue_breath()
#
# episode(5)
# cycle(2)
# elements(all)
# color.gradient(0,1)
# effect.hue_breath()
#
# episode(6)
# cycle(2)
# elements(all)
# color.gradient(0,1)
# effect.hue_breath()
#
# cycle(4)
# elements(papers)
# color.alternate(coral,indigo)
# effect.saw_tooth()

# cycle(4)
# elements(sticks)
# color.alternate(red,indigo)
# effect.snake()
#


# episode(0)
# cycle(4)
# cycle_beats(0,1)
# elements(all)
# color.gradient(blue,indigo)
# effect.breath()
# cycle(1)
#
# cycle(4)
# elements(lifas)
# color.alternate(blue,indigo)
# effect.snake()
# cycle(4)
# elements(papers)
# color.alternate(red,indigo)
# effect.hue_blink()
# cycle(8)
# elements(sticks)
# color.alternate(blue,coral)
# effect.snake()
#
# episode(0)
# cycle(2)
# elements(flowers)
# color.gradient(0,1)
# effect.hue_breath()

send_to_mqtt("looped")
start_song("looped",0)#offset in seconds


