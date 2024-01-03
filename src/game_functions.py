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



def center_rect(rect):
    x, y, w, h = rect

    x2 = x - w//2
    y2 = y - h//2
    new_rect = pygame.Rect(x2, y2, w, h)

    return new_rect


def get_dist(A, B):
    x1, y1 = A
    x2, y2 = B

    return sqrt((x2-x1)**2 + (y2-y1)**2)

def get_point_from_angle(pos, dist, angle):
    x1, y1 = pos

    x2 = x1 + cos(angle) * dist
    y2 = y1 + sin(angle) * dist

    return x2, y2


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

        diff = t2 - t1

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


def synchronized(timings):
    new_timings = []
    t1 = timings[0]

    for t in timings:
        new_timings.append(t - t1)

    return new_timings






