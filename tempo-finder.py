import librosa

# fn='biaxident.wav'
# fn='bad-guy.mp3'
fn = '../audacity-labels/Liquid Tension Experiment - Biaxident.wav'
# fn = '../audacity-labels/Rush - YYZ (HQ).wav'
# fn = '../audacity-labels/KHOOMEY.wav'

y, sr = librosa.load(fn, duration=30)
onset_env = librosa.onset.onset_strength(y=y, sr=sr)
tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)

t, beats=librosa.beat.beat_track(y=y)
# print(librosa. beats)
import scipy.stats
prior = scipy.stats.uniform(30, 300)  # uniform over 30-300 BPM
utempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr, prior=prior)
print(utempo)

import numpy as np

# Dynamic tempo with a proper log-normal prior
prior_lognorm = scipy.stats.lognorm(loc=np.log(120), scale=120, s=1)
dtempo_lognorm = librosa.beat.tempo(onset_envelope=onset_env, sr=sr,
                                    aggregate=None,
                                    prior=prior_lognorm)
print(dtempo_lognorm)

[print(i) for i in dtempo_lognorm]


import matplotlib.pyplot as plt
# Convert to scalar
tempo = tempo.item()
utempo = utempo.item()
# Compute 2-second windowed autocorrelation
hop_length = 512
ac = librosa.autocorrelate(onset_env, max_size=2 * sr // hop_length)
freqs = librosa.tempo_frequencies(len(ac), sr=sr,
                                  hop_length=hop_length)

# Plot on a BPM axis.  We skip the first (0-lag) bin.
fig, ax = plt.subplots()
ax.semilogx(freqs[1:], librosa.util.normalize(ac)[1:],
             label='Onset autocorrelation', base=2)
ax.axvline(tempo, 0, 1, alpha=0.75, linestyle='--', color='r',
            label='Tempo (default prior): {:.2f} BPM'.format(tempo))
ax.axvline(utempo, 0, 1, alpha=0.75, linestyle=':', color='g',
            label='Tempo (uniform prior): {:.2f} BPM'.format(utempo))
ax.set(xlabel='Tempo (BPM)', title='Static tempo estimation')
ax.grid(True)
ax.legend()