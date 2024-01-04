from src import game_functions as GF
from src import game_variables as GV

from src import settings as sett
from src.settings import WIDTH, HEIGHT, clock, FPS

from src.drawing_functions import draw_screen
from src.game_variables import TOM_A
from src.settings import BPM

import pygame
import random

from pygame.locals import *
from random import randrange, choice


WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def init_userevent():
    pygame.time.set_timer(GV.METRONOME_BEAT, 1000)
    pygame.time.set_timer(GV.METRONOME_HALF_BEAT, 500)
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
                    if GV.CONTINUE:
                        GV.TEST_COMPLETE = True
                    else:
                        GV.bg_color_indic.timer = 0

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
                    GF.compare_rhythms(timings2, GV.timings1)
                    GV.player_timings.clear()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

            if event.type == GV.METRONOME_BEAT:
                t = pygame.time.get_ticks()
                GV.metronome_indic.timer = 0
                TOM_A.play()

                GV.R2.timings.append(t)
                print('otime', t)

                if len(GV.R2.timings) >= 5 and len(GV.player_timings) >= 5:
                    GV.average_diff = GF.get_average_diff(GV.player_timings, GV.R2.timings, BPM)

                    GV.CONTINUE = abs(GV.average_diff) < 80

            if event.type == GV.METRONOME_HALF_BEAT:
                GV.ON_BEAT = not GV.ON_BEAT
                t = pygame.time.get_ticks()

                if GV.ON_BEAT:
                    GV.on_beat_time = t
                    pygame.draw.rect(WIN, 'seagreen2', (70,200,15,15))
                if GV.player_timings:
                    GV.last_note_diff = GF.compare_two_timings(GV.player_timings[-1], GV.on_beat_time, BPM)
                    if GV.last_note_diff:
                        GV.note_diff_list.append(GV.last_note_diff)

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

        GV.metronome_indic.timer += 1
        GV.bg_color_indic.timer += 1

        pygame.display.update()
        clock.tick(FPS)

    GV.R2.convert_timing_to_note_value()
    GV.R1.convert_timing_to_note_value()

    print(GV.R2.timings)
    print(GV.R2.notes)

    for t in GV.R2.timings:
        t2 = round(t / 1000, 1)
        print(t2)


    pygame.quit()



main()



