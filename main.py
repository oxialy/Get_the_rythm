from src import drawing_functions as DF
from src import game_functions as GF
from src import game_variables as GV
from src import music_variables as MV
from src import msc

from src import settings as sett
from src.settings import WIDTH, HEIGHT, clock, FPS

from src.drawing_functions import draw_screen, draw_screen_b
from src.game_variables import TOM_A, NOTIF_2
from src.music_variables import channel_1, channel_2
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


def stop_userevent():
    pygame.time.set_timer(GV.METRONOME_BEAT, 0)
    pygame.time.set_timer(GV.METRONOME_HALF_BEAT, 0)
    #pygame.time.set_timer(GV.PLAYER_BEAT, 0)


def init_sound():
    channel_1.set_volume(0.3)
    channel_2.set_volume(0.3)


def mute_all():
    channel_1.set_volume(0)
    channel_2.set_volume(0)


def unmute_all():
    channel_1.set_volume(0.3)
    channel_2.set_volume(0.3)


def main_menu(win):

    init_sound()

    channel_1.play(NOTIF_2)

    run_main = True

    while run_main:

        DF.draw_screen_a(win)

        GV.pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_main = False
            if event.type == pygame.KEYDOWN:
                if event.key in [K_q, K_ESCAPE]:
                    run_main = False

                if event.key == K_SPACE:
                    GV.CHOSEN_OPTION = 'record'

                if event.key == K_a:
                    print(win.get_size())

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        if pygame.mouse.get_pressed()[0]:
            GV.hovered_button = msc.check_hovered(GV.pos, GV.buttons_A)
            if GV.hovered_button:
                GV.CHOSEN_OPTION = GV.hovered_button.text

        if GV.hovered_button:
            GV.hovered_button.HOVERED = False

        GV.hovered_button = msc.check_hovered(GV.pos, GV.buttons_A)

        if GV.hovered_button:
            GV.hovered_button.HOVERED = True

        if GV.CHOSEN_OPTION:
            if GV.CHOSEN_OPTION in ['record', 'game', 'quit']:
                run_main = False

        pygame.display.update()
        clock.tick(FPS)


def recorder(win):

    init_userevent()

    run_main = True

    while run_main:

        draw_screen_b(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_main = False
            if event.type == pygame.KEYDOWN:
                if event.key in [K_q, K_ESCAPE]:
                    run_main = False

                if event.key in [K_f, K_j]:
                    t = pygame.time.get_ticks()

                    GV.R1.timings.append(t)

                if event.key == K_m:
                    mute_all()

                if event.key == K_n:
                    unmute_all()

                if event.key == K_SPACE:
                    pass

                if event.key == K_RETURN:
                    GV.R1.convert_timing_to_note_value()
                    values = GV.R1.true_values(70)
                    print(values)

                    for val in values:
                        if not val:
                            channel_1.play(NOTIF_2)

                    GV.R1.timings.clear()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

            if event.type == GV.METRONOME_BEAT:
                t = pygame.time.get_ticks()
                GV.metronome_indic.timer = 0
                channel_1.play(TOM_A)

                GV.R2.timings.append(t)

                if len(GV.R2.timings) >= 5 and len(GV.player_timings) >= 5:
                    GV.average_diff = GF.get_average_diff(GV.player_timings, GV.R2.timings, BPM)

                    GV.CONTINUE = abs(GV.average_diff) < 80


        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

        pygame.display.update()
        clock.tick(FPS)

    stop_userevent()

def main(win):

    init_userevent()

    run_main = True

    while run_main:

        draw_screen(win)

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


# Start game loop

main_menu(WIN)

print(GV.CHOSEN_OPTION)

if GV.CHOSEN_OPTION == 'record':
    recorder(WIN)

if GV.CHOSEN_OPTION == 'game':
    main(WIN)


pygame.quit()

