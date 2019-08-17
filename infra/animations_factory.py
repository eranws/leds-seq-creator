import copy
from enum import Enum

from animations.confetti import ConfettiAnimation
from animations.rand_brightness import RandBrightnessAnimation
from animations.rand_sat import RandSaturationAnimation
from float_func.steps import StepsFloatFunc
from infra import timing, stored_animations
from animations.alternate_coloring import AlternateColoringAnimation
from animations.brightness import BrightnessAnimation
from animations.const_color import ConstColorAnimation
from animations.hue_shift import HueShiftAnimation
from animations.rainbow import Rainbow
from animations.snake import SnakeAnimation
from boolean_func.const import ConstBooleanFunc
from float_func.comb2 import Comb2FloatFunc
from float_func.const import ConstFloatFunc
from float_func.half import HalfFloatFunc
from float_func.linear import LinearFloatFunc
from float_func.repeat import RepeatFloatFunc
from float_func.sin import SinFloatFunc
from infra.length import short, medium, long, soft, hard, total
from led_objects.objects_selector import get_elements


class ColorFactory:

    def uniform(self, color):
        ConstColorAnimation(color).apply()

    def gradient(self, hue_start, hue_end):
        Rainbow(ConstFloatFunc(hue_start), ConstFloatFunc(hue_end)).apply()

    def alternate(self, color1, color2, number_of_pixels = 3):
        AlternateColoringAnimation(color1, color2, number_of_pixels).apply()


color = ColorFactory()


class EffectFactory:

    def brightness(self, factor):
        BrightnessAnimation(ConstFloatFunc(factor)).apply()

    def snake(self, tail=1.0, switch_direction=False):
        if isinstance(tail, str):
            tail = {short: 0.25, medium: 1.0, long: 4.0}[tail]
        if switch_direction:
            SnakeAnimation(LinearFloatFunc(1.0, 0.0 - tail), ConstFloatFunc(tail), ConstBooleanFunc(not switch_direction)).apply()
        else:
            SnakeAnimation(LinearFloatFunc(0.0, 1.0 + tail), ConstFloatFunc(tail), ConstBooleanFunc(not switch_direction)).apply()

    def snake_up_down(self, tail=1.0):
        if isinstance(tail, str):
            tail = {short: 0.25, medium: 1.0, long: 4.0}[tail]
        SnakeAnimation(SinFloatFunc(1.0, -0.1, -0.25, 1), ConstFloatFunc(tail), ConstBooleanFunc(True)).apply()

    def snake_down_up(self, tail=1.0):
        if isinstance(tail, str):
            tail = {short: 0.25, medium: 1.0, long: 4.0}[tail]
        SnakeAnimation(SinFloatFunc(0.0, 1.0, -0.25, 1), ConstFloatFunc(tail), ConstBooleanFunc(False)).apply()

    def blink_repeat(self, repeat, edge=0.5):
        if isinstance(edge, str):
            edge = {soft: 0.25, medium: 0.5, hard: 0.75, total: 1.0}[edge]
        BrightnessAnimation(RepeatFloatFunc(repeat, HalfFloatFunc(ConstFloatFunc(1.0), ConstFloatFunc(1.0 - edge)))).apply()

    def blink(self, edge=0.5, reverse=False):
        if isinstance(edge, str):
            edge = {soft: 0.25, medium: 0.5, hard: 0.75, total: 1.0}[edge]
        v1 = 1.0 - edge if reverse else 1.0
        v2 = 1.0 if reverse else 1.0 - edge
        BrightnessAnimation(HalfFloatFunc(ConstFloatFunc(v1), ConstFloatFunc(v2))).apply()

    def breath(self, edge=0.6, reverse=False):
        if isinstance(edge, str):
            edge = {soft: 0.4, medium: 0.6, hard: 0.8, total: 1.0}[edge]
        phase = 0.25 if reverse else -0.25
        BrightnessAnimation(SinFloatFunc(1.0 - edge, 1.0, phase, 1)).apply()

    def saw_tooth(self, edge=0.6, reverse=False):
        if isinstance(edge, str):
            edge = {soft: 0.4, medium: 0.6, hard: 0.8, total: 1.0}[edge]
        min_val = 1.0 - edge if reverse else 1.0
        max_val = 1.0 if reverse else 1.0 - edge
        BrightnessAnimation(LinearFloatFunc(min_val, max_val)).apply()

    def hue_shift_steps(self, num_steps, step_jump):
        HueShiftAnimation(StepsFloatFunc(num_steps, step_jump, 0.0)).apply()

    def hue_shift(self, edge=0.5):
        if isinstance(edge, str):
            edge = {soft: 0.05, medium: 0.12, hard: 0.25, total: 0.5}[edge]
        HueShiftAnimation(ConstFloatFunc(edge)).apply()

    def brightness(self, val):
        BrightnessAnimation(ConstFloatFunc(val)).apply()

    def hue_blink(self, edge=0.5, reverse=False):
        if isinstance(edge, str):
            edge = {soft: 0.05, medium: 0.12, hard: 0.25, total: 0.5}[edge]
        if reverse:
            edge = -edge
        HueShiftAnimation(HalfFloatFunc(ConstFloatFunc(1.0), ConstFloatFunc(1.0 - edge))).apply()

    def hue_breath(self, edge=0.1):
        if isinstance(edge, str):
            edge = {soft: 0.03, medium: 0.1, hard: 0.2, total: 0.5}[edge]
        HueShiftAnimation(SinFloatFunc(-edge, edge, 0.0, 1)).apply()

    def hue_saw_tooth(self, edge=0.1, reverse=False):
        if isinstance(edge, str):
            edge = {soft: 0.04, medium: 0.08, hard: 0.2, total: 0.35}[edge]
        if reverse:
            edge = -edge
        HueShiftAnimation(LinearFloatFunc(0.0, edge)).apply()

    def random_brightness(self):
        RandBrightnessAnimation().apply()

    def random_saturation(self):
        RandSaturationAnimation().apply()

    def confetti(self):
        ConfettiAnimation(ConstFloatFunc(0.5)).apply()

effect = EffectFactory()

