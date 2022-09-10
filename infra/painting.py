from infra import timing
from animations import const_color
from animations.alternate_coloring import AlternateColoringAnimation
from animations.rainbow import Rainbow
from float_func.const import ConstFloatFunc


class ColorEffects:
    def __init__(self, led_object):
        self.led_object = led_object

    def uniform(self, color):
        self.led_object.add_animation(
            const_color.const_color(timing.get_timing(), color[0], color[1], color[2])
        )

    def gradient(self, hue_start, hue_end):
        self.led_object.add_animation(
            Rainbow(
                timing.get_timing(), ConstFloatFunc(hue_start), ConstFloatFunc(hue_end)
            )
        )

    def alternate(self, c1, c2, number_of_pixels=3):
        self.led_object.add_animation(
            AlternateColoringAnimation(timing.get_timing(), c1, c2, number_of_pixels)
        )
