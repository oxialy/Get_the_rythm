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
current_sequence = -1
current_disp_sequence = 0
current_timing = 0

player_score = 0
sequence_score = 0

# record mode
chosen_save = 1
saved_values = []


timings1 = [1000 * x for x in range(20)]

player_timings = []
R1 = player_rhythm = Rhythm([], [])

R2 = original_rhythm = Rhythm([], [])

all_player_timings = []


OPTION_A1 = msc.Indicator((cx, cy - 30), (80,30), colors['purple1'], 'record')
OPTION_A2 = msc.Indicator((cx, cy + 15), (80,30), colors['purple1'], 'calibrate')
OPTION_A3 = msc.Indicator((cx, cy + 55), (80,30), colors['purple1'], 'game')

SAVE_BUTTON = msc.Indicator((40,40), (30,30), colors['orange1'], '1')
CONFIRM_BUTTON = msc.Indicator((cx, cy - 10), (100,30), colors['purple1'], 'confirm')

BORDER_1 = msc.Indicator((cx, 0), (230,22), colors['purple1'])
BORDER_2 = msc.Indicator((cx, HEIGHT-6), (0,12), colors['purple1'])

metronome_indic = msc.Indicator((cx - 30, HEIGHT - 60), (8,8), colors['purple1'], values=[0,1,2,3])
bg_color_indic = msc.Indicator((0,0), (10,10), None, DV.bg_color, DV.gradient)


buttons_A = [OPTION_A1, OPTION_A2, OPTION_A3]


note_diff_list = [500,500,500,500,500]

average_diff = 500
last_note_diff = 500
on_beat_time = 0

hovered_button = None

ON_BEAT = True

CONTINUE = False
TEST_COMPLETE = False
SAVE_MODE = False


METRONOME_BEAT = pygame.USEREVENT
METRONOME_HALF_BEAT = pygame.USEREVENT + 1








