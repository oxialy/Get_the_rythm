from src import game_functions as GF
from src import game_variables as GV

from src import settings as sett
from src.settings import WIDTH, HEIGHT, clock, FPS

from src.drawing_functions import draw_screen
from src.game_variables import TOM_A

import pygame
import random

from pygame.locals import *
from random import randrange, choice


WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def init_userevent():
    pygame.time.set_timer(GV.METRONOME_BEAT, 1000)
    #pygame.time.set_timer(GV.PLAYER_BEAT, 1000)


def main():

    init_userevent()

    run_main = True

    while run_main:

        draw_screen(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_main = False
            if event.type == pygame.KEYDOWN:
                if event.key in [K_q, K_ESCAPE]:
                    run_main = False

                if event.key == K_SPACE:
                    init_userevent()

                if event.key == K_BACKSPACE:
                    GV.R1.convert_timing_to_note_value()
                    GV.R2.convert_timing_to_note_value()

                    print('')
                    GF.compare_rhythms(GV.R1.timings, GV.R2.timings)

                    pygame.time.set_timer(GV.METRONOME_BEAT, 0)
                    pygame.time.set_timer(GV.PLAYER_BEAT, 0)

                if event.key in [K_f, K_j]:
                    t = pygame.time.get_ticks()
                    print(t)
                    GV.player_timings.append(t)

                    timings1 = GV.R1.timings
                    values1 = GV.R1.notes

                    timings1.append(t)
                    GV.R1.convert_timing_to_note_value()

                    n = len(values1[-5:])
                    s = sum(values1[-5:])
                    if n != 0:
                        print('avg2', s/n)
                    else:
                        print(0)


                if event.key == K_RETURN:
                    timings2 = GF.synchronized(GV.player_timings)
                    GF.compare_rhythms(timings2, GV.timing1)
                    GV.player_timings.clear()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

            if event.type == GV.METRONOME_BEAT:
                t = pygame.time.get_ticks()
                GV.metronome_indic.timer = 0
                TOM_A.play()

                GV.R2.timings.append(t)
                print('otime', t)

            if event.type == GV.PLAYER_BEAT:
                t = pygame.time.get_ticks()
                GV.R1.timings.append(t)

                print(t)

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

        GV.metronome_indic.timer += 1

        pygame.display.update()
        clock.tick(FPS)

    GV.R2.convert_timing_to_note_value()
    GV.R1.convert_timing_to_note_value()
    print(GV.R2.timings)
    print(GV.R2.notes)

    pygame.quit()



main()



