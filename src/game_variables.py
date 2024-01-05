from src import drawing_variables as DV
from src import game_functions as GF
from src import settings as sett
from src import msc

from .drawing_variables import colors
from .settings import WIDTH, HEIGHT
from .rhythm import Rhythm


import pygame


CHOSEN_OPTION = None

pos = 0, 0

NOTES_VALUES = {
    2: 2000,
    1: 1000,
    1/2: 500
}

current_beat = 1
current_sequence = 0

timing1 = [0, 1000, 2000, 3000]
timings1 = [1000 * x for x in range(20)]

player_timings = []
R1 = player_rythm = Rhythm()

R2 = original_rythm = Rhythm()

#R2.timings = timing1


option_A1 = msc.Indicator((160, 135), (80,30), 'record')
option_A2 = msc.Indicator((160, 180), (80,30), 'calibrate')
option_A3 = msc.Indicator((160, 225), (80,30), 'game')

metronome_indic = msc.Indicator((WIDTH - 80, HEIGHT - 120), (30,30))
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








