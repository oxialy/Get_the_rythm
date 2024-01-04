
from src import settings as sett
from src import game_variables as GV
from src import drawing_variables as dv
from src import msc, logs

from .drawing_variables import bg_color, colors
from .settings import WIDTH, HEIGHT, FONT15, FONT20, FONT25, FONT12, FONT22, FONT10


import pygame
import random
from random import randrange, choice


def draw_test(win):
    def write_pos(win, positions):
        for pos in positions:
            write_text(win, pos, )

    write_text(win, GV.average_diff, (40, 35))

    if abs(GV.average_diff) < 80:
        pygame.draw.rect(win, colors['green1'], (80,80,20,20))

    write_text(win, GV.last_note_diff, (40, 70))

    col = ['seagreen', 'seagreen1', 'seagreen2', 'seagreen3', 'seagreen4']

    for i, col in enumerate(col):
        pygame.draw.rect(win, col, (i*5,290,3,3))

    for i, col in enumerate(dv.g2):
        pygame.draw.rect(win, col, (80+i*8, 265, 6,6))


def draw_screen(win):
    bg_color = GV.bg_color_indic
    bg_timer = GV.bg_color_indic.timer

    if bg_timer < len(bg_color.values):
        win.fill(bg_color.values[bg_timer])
    elif GV.TEST_COMPLETE:
        win.fill(colors['seagreen1'])
    else:
        win.fill(bg_color.default)

    if GV.metronome_indic.timer < 6:
        GV.metronome_indic.draw(win)

    draw_note_diff(win, GV.note_diff_list)

    draw_test(win)


def draw_elem(win, elements):
    for elem in elements:
        elem.draw(win)

def draw_note_diff(win, note_diff_list):
    center = x0, y0 = 180, 160

    pygame.draw.line(win, colors['grey1'], (70, y0), (280, y0), 2)
    pygame.draw.line(win, colors['grey1'], (x0, 150), (x0, 170), 1)

    k = 150 / 120

    for time in note_diff_list[-7:]:
        A = x0 + time / 3, 150
        B = x0 + time / 3, 170

        col_i = int(abs(time) // k)
        col_i = max(0, min(11, col_i))

        pygame.draw.line(win, dv.g2[col_i], A, B, 3)

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













