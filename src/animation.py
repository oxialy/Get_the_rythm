
from src import game_variables as gv

import pygame


def animate():
    timer = gv.BORDER_1.timer + 1
    increase_x2 = 1.3 * (48 / (1 + timer) - 1.6)
    increase_y2 = 0

    increase_x = 69 / (1 + timer) + 0.2
    increase_y = 0

    gv.BORDER_1.increase_size((increase_x, increase_y))
    gv.BORDER_2.increase_size((increase_x2, increase_y))

    gv.BORDER_1.timer += 1
    gv.BORDER_2.timer += 1















