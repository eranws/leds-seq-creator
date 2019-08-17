
""" global object - accessed from other modules """
import copy

from infra import stored_animations

tf_global = None
time_frame_factory = None


def get_timing():
    global tf_global
    return copy.deepcopy(tf_global)


class TimeFrame:

    def __init__(self, bpm, start_beat_index, number_of_beats, beats_in_cycle = None, start_offset = 0):
        self.start_offset = start_offset
        self.bpm = bpm
        self.start_beat_index = start_beat_index
        self.end_beat_index = start_beat_index + number_of_beats
        self._beats_in_cycle = beats_in_cycle
        self._cycle_beats = None

    @property
    def beats_in_cycle(self):
        return self._beats_in_cycle

    @beats_in_cycle.setter
    def beats_in_cycle(self, value):
        self._beats_in_cycle = value
        self._cycle_beats = None

    @property
    def repeats(self):
        if self.beats_in_cycle is None:
            return None
        return self.number_of_beats() / self.beats_in_cycle

    @property
    def cycle_beats(self):
        return self._cycle_beats

    @cycle_beats.setter
    def cycle_beats(self, start_end_tuple):
        self._cycle_beats = start_end_tuple

    def get_cycle_beat_rel_start(self):
        if not self._cycle_beats:
            return 0.0
        return self._cycle_beats[0] / float(self.beats_in_cycle)

    def get_cycle_beat_rel_end(self):
        if not self._cycle_beats:
            return 1.0
        return self._cycle_beats[1] / float(self.beats_in_cycle)

    def get_start_time_ms(self):
        return self.get_beat_time_ms(self.start_beat_index)

    def get_end_time_ms(self):
        return self.get_beat_time_ms(self.end_beat_index)

    def number_of_beats(self):
        return self.end_beat_index - self.start_beat_index

    def get_beat_time_ms(self, beat_index):
        beat_time_seconds = self.start_offset + beat_index * self.__get_beats_per_second()
        return int(beat_time_seconds * 1000.0)

    def __get_beats_per_second(self):
        return 60.0 / self.bpm


class TimeFrameFactory:

    def __init__(self, start_offset, bpm, beats_per_episode):
        self.start_offset = start_offset
        self.beats_per_episode = beats_per_episode
        self.bpm = bpm

    def from_beat(self, beat_start_index, beat_end_index):
        return TimeFrame(self.bpm, beat_start_index, beat_end_index - beat_start_index, start_offset=self.start_offset)

    def from_beat_in_episode(self, episode_number, beat_start_index, beat_count):
        return TimeFrame(self.bpm, (episode_number * self.beats_per_episode) + beat_start_index, beat_count, start_offset=self.start_offset)

    def episodes_length(self, episode_start_index, num_of_episodes):
        start_beat = episode_start_index * self.beats_per_episode
        num_of_beats = num_of_episodes * self.beats_per_episode
        return TimeFrame(self.bpm, start_beat, num_of_beats, None, start_offset=self.start_offset)

    def episodes_index(self, episode_start_index, episode_end_index):
        start_beat = episode_start_index * self.beats_per_episode
        num_of_beats = (episode_end_index - episode_start_index) * self.beats_per_episode
        return TimeFrame(self.bpm, start_beat, num_of_beats, start_offset=self.start_offset)

    def single_episode(self, episode_index):
        return self.episodes_length(episode_index, 1)


def song_settings(bpm, beats_per_episode, start_offset = 0):
    global time_frame_factory
    time_frame_factory = TimeFrameFactory(start_offset, bpm, beats_per_episode)


def beats(beat_start_index, beat_end_index):
    global time_frame_factory
    global tf_global
    tf_global = time_frame_factory.from_beat(beat_start_index, beat_end_index)


def beats_in_episode(episode_number, beat_start_index, beat_end_index):
    global time_frame_factory
    global tf_global
    tf_global = time_frame_factory.from_beat_in_episode(episode_number, beat_start_index, beat_end_index - beat_start_index)


def episodes(episode_start_index, episode_end_index):
    global time_frame_factory
    global tf_global
    tf_global = time_frame_factory.episodes_index(episode_start_index, episode_end_index)


def episode(episode_index):
    global time_frame_factory
    global tf_global
    tf_global = time_frame_factory.single_episode(episode_index)


def cycle(beats):
    global tf_global
    tf_global.beats_in_cycle = beats


def cycle_beats(start_beat, end_beat):
    global tf_global
    if start_beat >= end_beat:
        raise Exception("start beat ({0}) should be < end beat ({0})".format(start_beat, end_beat))
    if start_beat < 0:
        raise Exception("start beat({0}) should be >= 0".format(start_beat))
    if end_beat > tf_global.beats_in_cycle:
        raise Exception("current cycle has {0} beats, but end cycle beat set to {1}".format(tf_global.beats_in_cycle, end_beat))

    tf_global.cycle_beats = (start_beat, end_beat)
