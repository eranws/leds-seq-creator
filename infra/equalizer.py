from float_func.const import ConstFloatFunc
from float_func.sin import SinFloatFunc
from animations.fill import FillAnimation
from float_func.const import ConstFloatFunc
from led_objects.objects_selector import elements

import random

def single_equalizer(phase, max_val):
    FillAnimation(ConstFloatFunc(0.0), SinFloatFunc(0.1, max_val, phase, 1)).apply()


def equalizer(elem):
    for p, s in enumerate(elem.all):
        elements(s)
        single_equalizer(p/len(elem.all),random.uniform(0.6,1))
