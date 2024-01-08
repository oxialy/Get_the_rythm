
from src import game_variables as gv

import pygame


def animate():
    timer = gv.BORDER_1.timer + 1
    increase_x = (320 - timer * 2) / 100
    increase_y = (210 - timer * 3) / 100

    increase_x = 62 / (1 + timer) + 0.2
    increase_y = 0

    gv.BORDER_1.increase_size((increase_x, increase_y))
    gv.BORDER_1.timer += 1















