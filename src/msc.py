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
    def __init__(self, pos, size, col, text=None, font=FONT20, default=None, values=None):
        self.pos = pos
        self.size = size

        self.col = col
        self.col1 = col
        self.col2 = colors['red2']

        self.text = text
        self.text_col = colors['lightgrey1']
        self.font = font

        self.default = default
        self.values = values
        self.value_2 = None

        self.STATE = 0
        self.HOVERED = False
        self.timer = 100
        self.i = 0

    def draw(self, win):
        x, y = self.pos
        w, h = self.size

        rect = centered_rect((x,y,w,h))

        pygame.draw.rect(win, self.col, rect)

        if self.HOVERED:
            self.draw_hovered(win)
        if self.text:
            write_text(win, self.text, self.pos, self.text_col, self.font, True)

    def draw_hovered(self, win):
        x, y = self.pos
        w, h = self.size[0] + 5, self.size[1] + 5

        rect = centered_rect((x,y,w,h))

        pygame.draw.rect(win, colors['grey1'], rect, 3)

        if self.value_2:
            self.draw_hovered_value(win)

    def draw_hovered_value(self, win):
        x, y = self.pos[0] - 70, self.pos[1]
        w, h = 18,18

        rect = centered_rect((x,y,w,h))
        pygame.draw.rect(win, colors['grey1'], rect)
        write_text(win, self.value_2, (x,y), 'black', FONT15, True)

    def update_metronome(self):
        self.pos = WIDTH/2 - 30 + self.i * 20, self.pos[1]
        self.i += 1
        if self.i == 4:
            self.i = 0
        self.timer = 0

    def scale_size(self, scale):
        scale_x, scale_y = scale

        self.size = self.size[0] * scale_x, self.size[1] * scale_y

    def increase_size(self, amount, min_size, max_size):
        increase_x, increase_y = amount
        min_x, min_y = min_size
        max_x, max_y = max_size

        x = self.size[0] + increase_x
        y = self.size[1] + increase_y

        self.size = max(min_x, min(max_x, x)), max(min_y, min(min_y, y))

    def update_text(self):
        pass

    def toggle_color(self):
        self.STATE = not self.STATE
        if self.STATE:
            self.col = self.col2
        else:
            self.col = self.col1

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











