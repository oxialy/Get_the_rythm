from src import settings as sett

from .drawing_variables import colors
from .settings import WIDTH, HEIGHT, FONT15, FONT20, FONT25, FONT12, FONT22, FONT10


import pygame
import random
import math

from pygame import Vector2
from random import sample
from math import sqrt, cos, sin, atan2


pygame.font.init()

FONT30 = pygame.font.SysFont('arial', 30)
FONT35 = pygame.font.SysFont('arial', 35)
FONT40 = pygame.font.SysFont('arial', 40)


class Indicator:
    def __init__(self, pos, size, text=None, default=None, values=None):
        self.pos = pos
        self.size = size

        self.col = colors['purple1']

        self.text = text

        self.default = default
        self.values = values

        self.HOVERED = False
        self.timer = 100

    def draw(self, win):
        x, y = self.pos
        w, h = self.size

        rect = centered_rect((x,y,w,h))

        pygame.draw.rect(win, self.col, rect)

        if self.HOVERED:
            pygame.draw.rect(win, colors['grey1'], rect, 3)

        if self.text:
            write_text(win, self.text, self.pos, center=True)

    def is_clicked(self, pos):
        x,y = self.pos
        w,h = self.size

        rect = centered_rect((x,y,w,h))

        return pygame.Rect(rect).collidepoint(pos)


def check_hovered(pos, buttons):
    for button in buttons:
        if button.is_clicked(pos):
            #button.HOVERED = True
            return button
        else:
            pass


def centered_rect(rect):
    x,y,w,h = rect

    x -= w // 2
    y -= h // 2

    return pygame.Rect((x,y,w,h))


def write_text(win, data, pos, col=colors['grey1'], font=FONT20, center=False, resize_limit=0):
    #font = pygame.font.SysFont('arial', 30)

    text_surf = font.render(str(data), 1, col)
    size = text_surf.get_size()

    if resize_limit != 0 and size[0] > resize_limit:
        text_surf = sett.FONT15.render(str(data), 1, col)
        size = text_surf.get_size()

    if center:
        x = pos[0] - size[0] // 2
        y = pos[1] - size[1] // 2
    else:
        x, y = pos

    win.blit(text_surf, (x,y))





def add_log(logs, data):
    if data not in logs:
        logs.append(data)
        print(data, len(logs))
    return logs











