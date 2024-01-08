from src import loading as load

from src.settings import main_dir, image_dir, sound_dir
from src.rhythm import Rhythm, convert_all_timing_to_value, convert_all_value_to_timing
from src.game_variables import R1

import random as rd


def shuffle_sequences(sequences):
    new_sequences = sequences.copy()
    rd.shuffle(new_sequences)
    return new_sequences


all_scores = load.load_all_scores()

pattern_values = [
    [500, 500, 250, 250, 500, 750, 250],
    [500, 250, 250, 250, 1250, 500],
    [1750, 250, 500, 250, 250],
    [1500, 1000, 500],
    [250, 750, 250, 1000, 250, 250, 250],
    [250, 250, 750, 250, 500, 250],

    [250, 500, 250, 250, 750, 250, 500, 250],
    [-250, 250, 250, 250, 500, 750, 500, 250],
    [500, 500, 250, 250, 750, 500],
    [500, 500, 250, 500],
    [250, 250, 750, 1250],
    [250, 250, 500, 750, 250, 250, 250, 500],
    [250, 250, 500, 750, 500, 250, 500],
    [500, 1000, 750, 250],
    [500, 750, 500, 250, 250, 250, 250]
]

rhythms = [Rhythm([], pattern) for pattern in pattern_values]
convert_all_value_to_timing(rhythms, start_time=4000)

pattern_max_points = [100 * len(ryt.timings) for ryt in rhythms]

sequences_0 = [{'rhythm': ryt, 'score': score, 'max_points': max} for ryt, score, max in zip(rhythms, all_scores, pattern_max_points)]

#sequences = shuffle_sequences(sequences_0)
sequences = sequences_0.copy()

print(1, sequences)
print(2, sequences[0])


'''
[500, 500, 250, 250, 500, 750, 250],
[500, 250, 250, 250, 1250, 500],
[1750, 250, 500, 250, 250],
[1500, 1000, 500],
[250, 750, 250, 1000, 250, 250, 250],
[250, 250, 750, 250, 500, 250]
'''


'''
[250, 500, 250, 250, 750, 250, 500, 250],
[0, 250, 250, 500, 750, 500, 250],
[250, 250, 250, 500, 750, 500, 250],
[500, 500, 250, 250, 750, 500],
[500, 500, 250, 500],
[250, 250, 666.6666666666666, 1250],
[0, 250, 750, 1250],
[250, 250, 750, 1250],
[250, 250, 500, 750, 250, 250, 250, 500],
[250, 250, 500, 750, 500, 250, 500],
[333.3333333333333, 1000, 750, 250],
[0, 1000, 750, 250],
[500, 1000, 750, 250],
[500, 750, 500, 250, 250, 250, 250]
'''







