import os
import pygame

pygame.display.init()
pygame.font.init()


src_dir = os.path.split(os.path.abspath(__file__))[0]
main_dir = os.path.split(src_dir)[0]
data_dir = os.path.join(main_dir, 'data')
image_dir = os.path.join(main_dir, 'images')
sound_dir = os.path.join(main_dir, 'sound_effects')


WIDTH, HEIGHT = 430, 260
#WIDTH, HEIGHT = 420, 420

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
BPM = 60

HALF_VALUE = 1000 * 60 / BPM
QUARTER_VALUE = 500 * 60 / BPM

tolerance_1 = 60
tolerance_2 = 110

number_of_sequences = 6

clock = pygame.time.Clock()


FONT10 = pygame.font.SysFont('arial', 10)
FONT12 = pygame.font.SysFont('calibri', 12)
FONT15 = pygame.font.SysFont('calibri', 15)
FONT20 = pygame.font.SysFont('calibri', 20)

FONT22 = pygame.font.SysFont('arial', 22)
FONT25 = pygame.font.SysFont('calibri', 25)
FONT30 = pygame.font.SysFont('arial', 30)

FONT35 = pygame.font.SysFont('arial', 35)
FONT40 = pygame.font.SysFont('arial', 40)


LOGS = []





