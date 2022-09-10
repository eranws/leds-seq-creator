import copy

from infra import timing
from led_objects.objects_selector import get_elements


class Animation:
    def __init__(self):
        self.timing = None
        self.repeat_params = None
        self.segments = None

    def to_json_obj(self, compact):

        if compact:
            params = self.get_compact_params_json()
        else:
            params = self.get_params_json()

        json_obj = {
            "t": self.name,
            "p": self.segments if len(self.segments) != 1 else self.segments[0],
            "s": self.timing.get_start_time_ms(),
            "e": self.timing.get_end_time_ms(),
            "params": params,
        }

        if self.timing.repeats:
            cycle_beats = self.timing.cycle_beats
            json_obj["rep_s"] = self.timing.get_cycle_beat_rel_start()
            json_obj["rep_e"] = self.timing.get_cycle_beat_rel_end()
            json_obj["rep_num"] = self.timing.repeats

        if self.repeat_params:
            total_beats = self.timing.number_of_beats()
            curr_length_in_beats = self.repeat_params["curr_length_beats"]
            if not curr_length_in_beats:
                curr_length_in_beats = total_beats
            json_obj["rep_s"] = self.repeat_params["repeat_start_beat"] / float(
                curr_length_in_beats
            )
            json_obj["rep_e"] = self.repeat_params["repeat_end_beat"] / float(
                curr_length_in_beats
            )
            num_repeat = total_beats / curr_length_in_beats
            json_obj["rep_num"] = num_repeat
        return json_obj

    def apply(self):

        self.timing = timing.get_timing()
        elements_to_apply = get_elements()
        if not elements_to_apply:
            raise Exception("animation has no led objects to take effect on")

        leds_segment = {}
        for segment_proxy in elements_to_apply:
            if segment_proxy.led_object not in leds_segment:
                leds_segment[segment_proxy.led_object] = []
            leds_segment[segment_proxy.led_object].append(segment_proxy.segment_name)

        for led_object, segments in leds_segment.items():
            self.segments = segments
            led_object.add_for_segment(segments, copy.deepcopy(self))

    def create_from_template(self):
        self.timing = timing.get_timing()
        self.apply()
