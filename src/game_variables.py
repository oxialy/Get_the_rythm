from src import drawing_variables as DV
from src import game_functions as GF
from src import settings as sett
from src import msc

from .drawing_variables import colors
from .settings import WIDTH, HEIGHT
from .rhythm import Rhythm


import pygame

pygame.mixer.init()

TOM_A = pygame.mixer.Sound('C:/Users/jingl/Documents/GitHub/Get_the_rythm/sound_effects/tom.wav')


NOTES_VALUES = {
    2: 2000,
    1: 1000,
    1/2: 500,

}

timing1 = [0, 1000, 2000, 3000]
timings1 = [1000 * x for x in range(20)]

player_timings = []
R1 = player_rythm = Rhythm()

R2 = original_rythm = Rhythm()

#R2.timings = timing1


metronome_indic = msc.Indicator((WIDTH - 80, HEIGHT - 120), (30,30))
bg_color_indic = msc.Indicator((0,0), (10,10), DV.bg_color, DV.gradient)

note_diff_list = [500,500,500,500,500]

average_diff = 500
last_note_diff = 500
on_beat_time = 0

ON_BEAT = True

CONTINUE = False
TEST_COMPLETE = False


METRONOME_BEAT = pygame.USEREVENT
METRONOME_HALF_BEAT = pygame.USEREVENT + 1

questions = [
    {'title': 1, 'answers': [1,2,3]},
    {'title': 2, 'answers': [1,2,3]},
    {'title': 3, 'answers': [1,2,3]}
]


