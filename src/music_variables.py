
from src import loading as load

import os
import pygame

pygame.mixer.init()


TOM_A = load.load_sound('tom.wav')
TOM_B = load.load_sound('tomB.wav')
HI_HAT_A = load.load_sound('hi-hat2.wav')
HI_HAT_B = load.load_sound('hi-hat.wav')

NOTIF_2 = load.load_sound('notif2.wav')


channel_1 = pygame.mixer.Channel(1)
channel_2 = pygame.mixer.Channel(2)












