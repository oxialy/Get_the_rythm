import os
import pygame

pygame.font.init()

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'images')


WIDTH, HEIGHT = 350, 350

FPS = 60
BPM = 60

clock = pygame.time.Clock()


FONT10 = pygame.font.SysFont('arial', 10)
FONT12 = pygame.font.SysFont('calibri', 12)
FONT15 = pygame.font.SysFont('arial', 15)
FONT20 = pygame.font.SysFont('calibri', 20)

FONT22 = pygame.font.SysFont('arial', 22)
FONT25 = pygame.font.SysFont('arial', 25)
FONT30 = pygame.font.SysFont('arial', 30)

FONT35 = pygame.font.SysFont('arial', 35)
FONT40 = pygame.font.SysFont('arial', 40)


LOGS = []





