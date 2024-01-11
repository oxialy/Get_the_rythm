
from src import game_variables as gv

from src.drawing_variables import colors
from src.settings import WIDTH, HEIGHT

import pygame
from math import pi, sin


def increase():
    timer = gv.BORDER_1.timer + 1
    increase_x2 = 1.3 * (48 / (1 + timer) - 1.6)
    increase_y2 = 0

    increase_x = 69 / (1 + timer) + 0.2
    increase_y = 0

    gv.BORDER_1.increase_size((increase_x, increase_y), min_size=(195, 22), max_size=(WIDTH, 22))
    gv.BORDER_2.increase_size((increase_x2, increase_y), min_size=(195, 22), max_size=(WIDTH, 22))

    gv.BORDER_1.timer += 1
    gv.BORDER_2.timer += 1


def shorten():
    timer = gv.BORDER_1.timer + 1
    increase_x2 = 1.3 * (48 / (1 + timer) - 1.6)
    increase_y2 = 0

    increase_x = 69 / (1 + timer) + 0.2
    increase_y = 0

    gv.BORDER_1.increase_size((-increase_x, increase_y), min_size=(195, 22), max_size=(WIDTH, 22))
    gv.BORDER_2.increase_size((-increase_x2, increase_y), min_size=(195, 22), max_size=(WIDTH, 22))

    gv.BORDER_1.timer += 1
    gv.BORDER_2.timer += 1


def initialize_score_indicator(ind, score):
    ind.text_col = colors['darkgrey1']
    ind.values = []
    ind.timer = 0
    for i in range(score + 1):
        ind.values.append(i)
        if i > 2 * score // 3:
            ind.values.append(i)


def increase_value(ind, n):
    k1 = pi / n
    k2 = len(ind.values) // 2

    i = int(sin(-pi/2 + k1 * ind.timer) * k2) + k2 - (len(ind.values) + 1) % 2

    ind.i = i
    ind.value_2.append(ind.values[i])

    ind.text = ind.values[i]


def draw_graph(win, values):
    for i, val in enumerate(values):
        x = i
        y = val * 2

        w, h = 3, 3

        pygame.draw.rect(win, 'purple', (x,y,w,h))










