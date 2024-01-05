from src import drawing_variables as dv
from src import settings as sett
from src import msc

from .drawing_variables import colors
from .settings import FONT20, FONT22, FONT25, FONT30, FONT35, FONT40

import pygame
import math
import random
from math import sqrt, cos, sin
from random import randrange, choice, shuffle



def compare_rhythms(timings_a, timings_b):
    result = []

    i = 0
    j = 0

    tolerance_1 = 40
    tolerance_2 = 110

    bonus = 0
    malus = 0
    total = 0

    while i < len(timings_a) and j < len(timings_b):
        t1 = timings_a[i]
        t2 = timings_b[j]

        diff = t1 - t2

        if t1 <= t2 - tolerance_2:
            points = 0
            i += 1
        elif t1 >= t2 + tolerance_2:
            points = 0
            j += 1
        else:
            points = 100
            i += 1
            j += 1
        total += points
        comparison = {'timing': t2, 'diff': diff, 'points': points}
        result.append(comparison)

    for comp in result:
        print(comp['diff'], comp['points'])
    print(total, result)

    return result


def get_average_diff(timings_a, timings_b, BPM):
    i = -5
    j = -5

    tol = 1000 * 60 / (BPM * 2)     # half beat in MS
    diff_list = []

    if timings_a[i] < timings_b[j] - tol:
        i += 1
    elif timings_a[i] > timings_b[j] + tol:
        j += 1

    for t1, t2 in zip(timings_a[i:], timings_b[j:]):
        diff_list.append((t1 - t2))

    n = len(diff_list)
    s = sum(diff_list)

    return s / n


def compare_two_timings(t1, t2, BPM):
    tol = 1000 * 60 / BPM / 2

    if t1 < t2 - tol:
        return None
    else:
        return t1 - t2


def synchronized(timings):
    new_timings = []
    t1 = timings[0]

    for t in timings:
        new_timings.append(t - t1)

    return new_timings






