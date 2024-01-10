import pygame

from src import settings as sett
from src import loading as load

from src.rhythm import Rhythm, convert_all_timing_to_value, convert_all_value_to_timing

import random as rd


def adjust_all_to_bpm(rhythms):
    for r in rhythms:
        r.adjust_value_to_bpm(sett.BPM)


def shuffle_sequences(sequences, n):
    if n is None:
        n = len(sequences)

    new_sequences = sequences.copy()
    rd.shuffle(new_sequences)

    return new_sequences[:n]


all_scores = load.load_all_scores()

start_time = 4000 * 60 / sett.BPM
score_0 = pygame.Surface((100, 100)), pygame.Rect((10, 10, 10, 10))
sequence_end = {'rhythm': None, 'score': score_0, 'max_points': None}

pattern_values = [
    [500, 500, 250, 250, 500, 750, 250],
    [500, 250, 250, 250, 1250, 500],
    [1750, 250, 500, 250, 250],
    [1500, 1000, 500],
    [250, 750, 250, 1000, 250, 250, 250],
    [250, 250, 750, 250, 500, 250],

    [250, 500, 250, 250, 750, 250, 500, 250],
    [-250, 250, 250, 250, 500, 750, 500, 250],
    [-250, 500, 500, 250, 250, 750, 500],
    [-750, 500, 500, 250, 500],
    [250, 250, 750, 1250],
    [250, 250, 500, 750, 250, 250, 250, 500],
    [250, 250, 500, 750, 500, 250, 500],
    [500, 1000, 750, 250],
    [500, 750, 500, 250, 250, 250, 250]
]

rhythms = [Rhythm([], pattern) for pattern in pattern_values]
adjust_all_to_bpm(rhythms)
convert_all_value_to_timing(rhythms, start_time)


pattern_max_points = [100 * len(ryt.timings) for ryt in rhythms]

sequences_0 = [{'rhythm': ryt, 'score': score, 'max_points': max} for ryt, score, max in zip(rhythms, all_scores, pattern_max_points)]

'''
def get_sequences():
    sequences = []
    score_0 = pygame.Surface((100, 100)), pygame.Rect((10, 10, 10, 10))
    sequence_end = {'rhythm': None, 'score': score_0, 'max_points': None}

    for ryt, score, max in zip(rhythms, all_scores, pattern_max_points):
        sequence = {'rhythm': ryt, 'score': score, 'max_points': max}
        sequences.append(sequence)
        
    sequences.append(sequence_end)
    
    return sequences'''


sequences = shuffle_sequences(sequences_0, sett.number_of_sequences)
#sequences = sequences_0.copy()[:sett.number_of_sequences]

sequences.append(sequence_end)


print(sequences)


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







