# from led_objects.instances import donut1, cabbage1, donut3, cup_cake4, cabbage5, cabbage6, brain7, cup_cake3, rug4, rug6
from led_objects.instances import *

# from led_objects.flowers import flower1, paper2, bottle4, paper5, bottle5, flower6, gloves8
# from led_objects.stands import lifas1, sticks3, lifas4, lifas5, sticks7, sticks8
# from led_objects.stars import star7, star8
from led_objects.objects_selector import elements_flatten

group1 = elements_flatten([flower1, donut1, lifas1, cabbage1])
group2 = elements_flatten([paper2])
group3 = elements_flatten([cup_cake3, donut3, sticks3])
group4 = elements_flatten([lifas4, rug4, bottle4, cup_cake4])
group5 = elements_flatten([paper5, lifas5, bottle5, cabbage5])
group6 = elements_flatten([flower6, cabbage6, rug6])
group7 = elements_flatten([sticks7, brain7, star7])
group8 = elements_flatten([sticks8, gloves8, star8])

# cabbages:
cabbages = elements_flatten([cabbage1, cabbage6, cabbage5])
brains = elements_flatten([brain7])
twists = elements_flatten([cabbages, brains])
donuts = elements_flatten([donut1, donut3])

# flowers:
flowers = elements_flatten([flower1, flower6])
bottles = elements_flatten([bottle4, bottle5])
papers = [paper2, paper5]  # ??
strings = elements_flatten([flowers, bottles, papers])
gloves = elements_flatten([gloves8])

# flood:
cup_cakes = elements_flatten([cup_cake4, cup_cake3])
rugs = elements_flatten([rug4, rug6])
floods = elements_flatten([cup_cakes, rugs])

# stands:
sticks = elements_flatten([sticks3, sticks7, sticks8])
single_sticks = elements_flatten([stick.all for stick in sticks])
lifas = elements_flatten([lifas1, lifas4, lifas5])
single_lifas = elements_flatten([lifa.all for lifa in lifas])

# stands:
stands = elements_flatten([sticks, lifas])
single_stands = elements_flatten([single_lifas, single_sticks])
single_stands_per_stand = elements_flatten(single_sticks + single_lifas)

# stars:
stars = elements_flatten([star7, star8])
single_stars = elements_flatten([star.all for star in stars])

# common (no-stands):
no_stands = elements_flatten(
    [flowers, bottles, cabbages, papers, cup_cakes, donuts, brains, rugs, gloves, stars]
)
