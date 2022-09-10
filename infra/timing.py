""" global object - accessed from other modules """
import copy

time_frame_factory = None


class TimeFrame:
    """
    represent a continues time frame in the song, with data on beats and cycle
    """

    def __init__(
        self,
        bpm: float,
        start_beat_index: float,
        end_beat_index: float,
        beats_in_cycle: float = None,
        start_offset: float = 0,
    ):
        """
        :param start_offset: the offset in ms for the first beat in the song
        :param bpm: the song's beat per minutes
        :param start_beat_index: the index of the beat that start the time frame
        :param end_beat_index: the index of the (one plus) last beat in the time frame
        :param beats_in_cycle: how many beats form a cycle in this time frame
        :param cycle_beats: ?
        """
        self._start_offset = start_offset
        self._bpm = bpm
        self._start_beat_index = start_beat_index
        self._end_beat_index = end_beat_index
        self._beats_in_cycle = beats_in_cycle
        self._cycle_beats = None

    @property
    def start_beat_index(self):
        return self._start_beat_index

    @property
    def end_beat_index(self):
        return self._end_beat_index

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
        return self.get_beat_time_ms(self._start_beat_index)

    def get_end_time_ms(self):
        return self.get_beat_time_ms(self._end_beat_index)

    def number_of_beats(self):
        return self._end_beat_index - self._start_beat_index

    def get_beat_time_ms(self, beat_index):
        beat_time_seconds = (
            self._start_offset + beat_index * self.__get_beats_per_second()
        )
        return int(beat_time_seconds * 1000.0)

    def __get_beats_per_second(self):
        return 60.0 / self._bpm

    def copy(self):
        """
        copy the instance and return a new instance which is a copy of self
        :return: a new TimeFrame instance which is a copy of self
        """
        return copy.deepcopy(self)

    def extend(self, rel_start: float, rel_end: float):
        """
        extent the time frame to start and end at different times,
        relatively to the current start and end times.

        the parameters are the new start and end time, relativily
        to the current time frame, where 0.0 is the current start,
        and 1.0 is the current end.
        for example:
        extend(0.0, 2.0) will double the time frame length,
            while starting at the same time
        extend(-1.0, 0.0) will double the time frame length,
            starting sooner, and ending at the orig end time
        extend(0.0, 0.5) will shorten the time frame to half

        :param rel_start: the new start time, relatively to the current time frame
        :param rel_end: the new end time, relatively to the current time frame
        :raise: ValueError if rel_start >= rel_end
        """

        if rel_start >= rel_end:
            raise ValueError("TimeFrame extend rel_start >= rel _end")

        orig_num_of_beats = self.number_of_beats()
        orig_start_beat = self._start_beat_index
        self._start_beat_index = orig_start_beat + orig_num_of_beats * rel_start
        self._end_beat_index = orig_start_beat + orig_num_of_beats * rel_end


tf_global = None


def get_timing() -> TimeFrame:
    global tf_global
    return tf_global.copy()


def set_timing(src_tf: TimeFrame):
    global tf_global
    tf_global = src_tf.copy()


class TimeFrameFactory:
    def __init__(self, start_offset, bpm, beats_per_episode):
        self.start_offset = start_offset
        self.beats_per_episode = beats_per_episode
        self.bpm = bpm

    def from_beat(self, beat_start_index, beat_end_index):
        return TimeFrame(
            self.bpm, beat_start_index, beat_end_index, start_offset=self.start_offset
        )

    def from_beat_in_episode(
        self, episode_number, beat_start_in_eipsode, beat_end_in_episode
    ):
        beat_start_index = (
            episode_number * self.beats_per_episode
        ) + beat_start_in_eipsode
        beat_end_index = (episode_number * self.beats_per_episode) + beat_end_in_episode
        return TimeFrame(
            self.bpm, beat_start_index, beat_end_index, start_offset=self.start_offset
        )

    def episodes_length(self, episode_start_index, num_of_episodes):
        start_beat_index = episode_start_index * self.beats_per_episode
        end_beat_index = (
            episode_start_index + num_of_episodes
        ) * self.beats_per_episode
        return TimeFrame(
            self.bpm,
            start_beat_index,
            end_beat_index,
            None,
            start_offset=self.start_offset,
        )

    def episodes_index(self, episode_start_index, episode_end_index):
        start_beat_index = episode_start_index * self.beats_per_episode
        end_beat_index = episode_end_index * self.beats_per_episode
        return TimeFrame(
            self.bpm, start_beat_index, end_beat_index, start_offset=self.start_offset
        )

    def single_episode(self, episode_index):
        return self.episodes_length(episode_index, 1)


def song_settings(bpm, beats_per_episode, start_offset=0):
    global time_frame_factory
    time_frame_factory = TimeFrameFactory(start_offset, bpm, beats_per_episode)


def beats(beat_start_index, beat_end_index):
    global time_frame_factory
    global tf_global
    tf_global = time_frame_factory.from_beat(beat_start_index, beat_end_index)


def beats_in_episode(episode_number, beat_start_index, beat_end_index):
    global time_frame_factory
    global tf_global
    tf_global = time_frame_factory.from_beat_in_episode(
        episode_number, beat_start_index, beat_end_index
    )


def episodes(episode_start_index, episode_end_index):
    global time_frame_factory
    global tf_global
    tf_global = time_frame_factory.episodes_index(
        episode_start_index, episode_end_index
    )


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
        raise Exception(
            "start beat ({0}) should be < end beat ({0})".format(start_beat, end_beat)
        )
    if start_beat < 0:
        raise Exception("start beat({0}) should be >= 0".format(start_beat))
    if end_beat > tf_global.beats_in_cycle:
        raise Exception(
            "current cycle has {0} beats, but end cycle beat set to {1}".format(
                tf_global.beats_in_cycle, end_beat
            )
        )

    tf_global.cycle_beats = (start_beat, end_beat)
