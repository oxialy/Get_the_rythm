from src import drawing_variables as DV
from src import game_functions as GF
from src import settings as sett
from src import msc

from .drawing_variables import colors
from .settings import WIDTH, HEIGHT
from .rhythm import Rhythm


import pygame
import random

from random import randrange

cx, cy = WIDTH / 2, HEIGHT / 2

CHOSEN_OPTION = None

pos = 0, 0

NOTES_VALUES = {
    2: 2000,
    1: 1000,
    1/2: 500
}

time = 0
start_time = 0
current_beat = 0
current_half_beat = 15
current_sequence = 0


timings1 = [1000 * x for x in range(20)]

player_timings = []
R1 = player_rhythm = Rhythm([], [])

R2 = original_rhythm = Rhythm([], [])

#R2.timings = timing1


option_A1 = msc.Indicator((cx, 90), (80,30), colors['purple1'], 'record')
option_A2 = msc.Indicator((cx, 135), (80,30), colors['purple1'], 'calibrate')
option_A3 = msc.Indicator((cx, 180), (80,30), colors['purple1'], 'game')

BORDER_1 = msc.Indicator((cx, 0), (230,22), colors['purple1'])
BORDER_2 = msc.Indicator((cx, HEIGHT-6), (0,12), colors['purple1'])

metronome_indic = msc.Indicator((WIDTH / 2 - 30, HEIGHT - 60), (8,8), colors['purple1'], values=[0,1,2,3])
bg_color_indic = msc.Indicator((0,0), (10,10), None, DV.bg_color, DV.gradient)

buttons_A = [option_A1, option_A2, option_A3]


note_diff_list = [500,500,500,500,500]

average_diff = 500
last_note_diff = 500
on_beat_time = 0

hovered_button = None

ON_BEAT = True

CONTINUE = False
TEST_COMPLETE = False


METRONOME_BEAT = pygame.USEREVENT
METRONOME_HALF_BEAT = pygame.USEREVENT + 1








