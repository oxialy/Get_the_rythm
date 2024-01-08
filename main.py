import os.path

from src import drawing_functions as DF
from src import game_functions as GF
from src import game_variables as GV
from src import music_variables as MV
from src import rhythm_patterns as rhy
from src import animation as anim
from src import logs
from src import msc

from src import settings as sett
from src.settings import WIDTH, HEIGHT, clock, FPS, WIN

from src.drawing_functions import draw_screen, draw_screen_b, draw_screen_d
from src.music_variables import TOM_A, TOM_B, NOTIF_2
from src.music_variables import channel_1, channel_2
from src.settings import BPM

import pygame
import random

from pygame.locals import *
from random import randrange, choice


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
    channel_2.set_volume(0.1)


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

                if event.key == K_1:
                    GV.CHOSEN_OPTION = 'record'

                if event.key == K_2:
                    GV.CHOSEN_OPTION = 'calibrate'

                if event.key == K_3:
                    GV.CHOSEN_OPTION = 'game'
                    GV.BORDER_1.timer = 0

                if event.key == K_a:
                    print(win.get_size())

            if event.type == pygame.MOUSEBUTTONDOWN:
                GV.hovered_button = msc.check_hovered(GV.pos, GV.buttons_A)
                if GV.hovered_button:
                    GV.CHOSEN_OPTION = GV.hovered_button.text
                    if GV.CHOSEN_OPTION == 'game':
                        GV.BORDER_1.timer = 0

        if GV.hovered_button:
            GV.hovered_button.HOVERED = False

        GV.hovered_button = msc.check_hovered(GV.pos, GV.buttons_A)

        if GV.hovered_button:
            GV.hovered_button.HOVERED = True

        if GV.BORDER_1.timer < 90:
            anim.animate()

        if GV.CHOSEN_OPTION:
            if GV.CHOSEN_OPTION in ['record', 'calibrate', 'game', 'quit'] and GV.BORDER_1.timer >= 68:
                run_main = False

        pygame.display.update()
        clock.tick(FPS)


def recorder(win):

    init_userevent()

    run_main = True

    while run_main:

        draw_screen_b(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_main = False
            if event.type == pygame.KEYDOWN:
                if event.key in [K_q, K_ESCAPE]:
                    run_main = False

                if event.key in [K_1, K_2, K_3]:
                    MAP = {K_1: 1, K_2: 2, K_3: 3}

                    n = MAP[event.key]
                    GV.SAVE_BUTTON.text = str(n)
                    GV.SAVE_BUTTON.pos = (10 + 30 * n, 40)

                    GV.chosen_save = n

                if event.key in [K_f]:
                    t = pygame.time.get_ticks()
                    GV.R1.timings.append(t)

                if event.key == [K_j]:
                    t = pygame.time.get_ticks()
                    GV.R1.timings.append(-t)

                if event.key == K_m:
                    mute_all()

                if event.key == K_n:
                    unmute_all()

                if event.key == K_BACKSPACE:
                    GV.saved_values.pop(-1)

                if event.key == K_SPACE:
                    if GV.SAVE_MODE:
                        print(62, 'saved')
                        logs.save_timing_values(logs.DATA_FILE, GV.saved_values, GV.chosen_save)
                        GV.saved_values.clear()

                    GV.SAVE_MODE = not GV.SAVE_MODE
                    GV.SAVE_BUTTON.toggle_color()
                    print(61, 'space', GV.SAVE_BUTTON.col, GV.SAVE_BUTTON.STATE)

                if event.key == K_RETURN:
                    GV.R1.convert_timing_to_value()

                    values = GV.R1.true_values(70)
                    GV.saved_values.append(values)

                    logs.save_timing_values(logs.DATA_FILE, GV.saved_values, 0)  # autosave

                    print('recorded list', GV.saved_values)

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


def calibrate(win):

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
                    values1 = GV.R1.values

                    timings1.append(t)
                    GV.R1.convert_timing_to_value()

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
                    pygame.draw.rect(win, 'seagreen2', (70,200,15,15))

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


def game(win):

    init_userevent()

    run_main = True

    #channel_1.play(TOM_A)
    GV.start_time = pygame.time.get_ticks()

    while run_main:
        GV.time = pygame.time.get_ticks()
        draw_screen_d(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_main = False
            if event.type == pygame.KEYDOWN:
                if event.key in [K_q, K_ESCAPE]:
                    run_main = False

                if event.key == K_SPACE:
                    print(22)

                if event.key == K_8:
                    GV.current_sequence = 6
                    GV.current_disp_sequence = 6

                if event.key == K_BACKSPACE:
                    if GV.CONTINUE:
                        GV.TEST_COMPLETE = True
                    else:
                        GV.bg_color_indic.timer = 0

                if event.key in [K_f, K_j]:
                    t = pygame.time.get_ticks()
                    timings = rhy.sequences[GV.current_sequence]['rhythm'].timings

                    GV.R1.timings.append(t)

                    if timings[GV.current_timing] < 0:
                        GV.current_timing += 1

                    diff = abs(t - GV.start_time - timings[GV.current_timing])
                    points = GF.eval_diff(diff)

                    print(31, t - GV.start_time - timings[GV.current_timing])
                    print(32, timings, GV.current_timing, len(timings))

                    if points:
                        GV.sequence_score += points
                        GV.player_score += points
                        GV.current_timing += 1

                if event.key == K_RETURN:
                    timings2 = GF.synchronized(GV.player_timings)
                    GF.compare_rhythms(timings2, GV.timings1)
                    GV.player_timings.clear()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

            if event.type == GV.METRONOME_BEAT:
                GV.current_beat += 1
                t = pygame.time.get_ticks()

                GV.metronome_indic.update_metronome()

                GV.R2.timings.append(t)

                if GV.current_beat == 8:
                    GV.current_beat = 0
                    GV.current_disp_sequence += 1

                    print('current seq', GV.current_sequence)

                if GV.current_beat == 1:
                    GV.start_time = pygame.time.get_ticks()

                if GV.current_beat in [1, 5]:
                    channel_1.play(TOM_B)
                else:
                    channel_1.play(TOM_A)

            if event.type == GV.METRONOME_HALF_BEAT:
                GV.current_half_beat += 1
                pygame.draw.rect(win, '#606099', (20,20,10,10))

                if GV.current_half_beat == 16:
                    seq = rhy.sequences[GV.current_sequence]

                    if GV.sequence_score == seq['max_points']:
                        channel_2.play(NOTIF_2)
                        print('gg')

                if GV.current_half_beat == 17:
                    GV.all_player_timings.append(GV.R1.timings)
                    GV.R1.timings.clear()

                    GV.sequence_score = 0
                    GV.current_timing = 0
                    GV.current_sequence += 1
                    GV.current_half_beat = 1
                    GV.start_time = pygame.time.get_ticks()


        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

        GV.metronome_indic.timer += 1
        GV.bg_color_indic.timer += 1

        pygame.display.update()
        clock.tick(FPS)

logs.data = logs.load_data(logs.DATA_FILE)

# Start game loop

main_menu(WIN)

print(GV.CHOSEN_OPTION)

if GV.CHOSEN_OPTION == 'record':
    recorder(WIN)

if GV.CHOSEN_OPTION == 'calibrate':
    calibrate(WIN)

if GV.CHOSEN_OPTION == 'game':
    game(WIN)

pygame.quit()

