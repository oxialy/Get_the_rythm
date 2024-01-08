
from src import loading as load

import os
import pygame

pygame.mixer.init()


TOM_A = load.load_sound('tom.wav')
TOM_B = load.load_sound('tomB.wav')
NOTIF_2 = load.load_sound('notif2.wav')


channel_1 = pygame.mixer.Channel(1)
channel_2 = pygame.mixer.Channel(2)












