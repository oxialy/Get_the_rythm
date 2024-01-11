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

from src.drawing_functions import draw_screen, draw_screen_b, draw_screen_d, draw_screen_f
from src.music_variables import TOM_A, TOM_B, NOTIF_2, HI_HAT_B, HI_HAT_A
from src.music_variables import channel_1, channel_2
from src.settings import BPM

import pygame
import random

from pygame.locals import *
from random import randrange, choice


# need separate directory  v
def init_userevent(BPM):
    HALF_VALUE = int(1000 * 60 / BPM)
    QUARTER_VALUE = int(500 * 60 / BPM)

    pygame.time.set_timer(GV.METRONOME_BEAT, HALF_VALUE)
    pygame.time.set_timer(GV.METRONOME_HALF_BEAT, QUARTER_VALUE)
    #pygame.time.set_timer(userevent, 0)


def stop_userevent():
    pygame.time.set_timer(GV.METRONOME_BEAT, 0)
    pygame.time.set_timer(GV.METRONOME_HALF_BEAT, 0)
    pygame.time.set_timer(GV.SEQUENCE_TIMING, 0)
    #pygame.time.set_timer(GV.PLAYER_BEAT, 0)


def init_sound():
    channel_1.set_volume(0.3)
    channel_2.set_volume(0.1)


def mute_all():
    channel_1.set_volume(0)
    channel_2.set_volume(0)


def reset_volume():
    channel_1.set_volume(0.3)
    channel_2.set_volume(0.3)


def volume_up():
    channel_1.set_volume(1)
    channel_2.set_volume(1)

# need separate directory  ^


def reset_game_values():
    #GV.BORDER_1.size = (195, 22)
    GV.BORDER_1.timer = 0

    GV.player_score = 0
    GV.sequence_score = 0
    GV.check_timing_1 = 0
    GV.current_sequence = -1
    GV.current_disp_sequence = 0
    GV.current_beat = 0
    GV.current_half_beat = 15
    GV.check_timing_2 = 1

    GV.R1.timings.clear()
    GV.all_player_timings.clear()
    GV.metronome_indic.i = 0

    stop_userevent()


def reset_sequence():
    GV.sequence_score = 0
    GV.check_timing_1 = 0
    GV.current_beat = 0
    GV.current_half_beat = 1
    GV.check_timing_2 = 0
    GV.start_time = pygame.time.get_ticks()

    GV.R1.timings.clear()
    GV.all_player_timings.clear()
    GV.metronome_indic.i = 0


def main_menu(win):

    run_main = True

    while run_main:

        DF.draw_screen_a(win)

        GV.pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GV.CHOSEN_OPTION = 'quit'

            if event.type == pygame.KEYDOWN:
                if event.key in [K_q, K_ESCAPE]:
                    GV.CHOSEN_OPTION = 'quit'

                if event.key == K_m:
                    mute_all()

                if event.key == K_i:
                    reset_volume()

                if event.key == K_s:
                    volume_up()

                if event.key == K_1:
                    GV.CHOSEN_OPTION = 'record'

                if event.key == K_2:
                    GV.CHOSEN_OPTION = 'calibrate'

                if event.key == K_3:
                    GV.CHOSEN_OPTION = 'game'
                    GV.BORDER_1.timer = 0
                    GV.BORDER_1.STATE = 0

                if event.key == K_a:
                    print(win.get_size())

                if event.key == K_SPACE:
                    GV.CHOSEN_OPTION = 'score'

            if event.type == pygame.MOUSEBUTTONDOWN:
                channel_1.play(NOTIF_2)
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

        if GV.BORDER_1.timer < 68:
            if GV.BORDER_1.STATE:
                anim.shorten()
            else:
                anim.increase()

        if GV.CHOSEN_OPTION:
            if GV.CHOSEN_OPTION in ['record', 'calibrate', 'game', 'score', 'quit'] and GV.BORDER_1.timer >= 68:
                GV.BORDER_1.timer = 0
                GV.BORDER_1.STATE = 1
                run_main = False

        pygame.display.update()
        clock.tick(FPS)


def level_menu(win):

    run_main = True

    while run_main:

        DF.draw_screen_e(win)

        GV.pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GV.CHOSEN_OPTION = 'quit'

            if event.type == pygame.KEYDOWN:
                if event.key in [K_q, K_ESCAPE]:
                    GV.CHOSEN_OPTION = 'back'

                if event.key == K_m:
                    mute_all()

                if event.key == K_i:
                    reset_volume()

                if event.key == K_s:
                    volume_up()

                if event.key == K_1:
                    GV.CHOSEN_OPTION = '1'

                if event.key == K_2:
                    GV.CHOSEN_OPTION = '2'

                if event.key == K_3:
                    GV.CHOSEN_OPTION = '3'
                    GV.BORDER_1.timer = 0

                if event.key == K_a:
                    print(win.get_size())

            if event.type == pygame.MOUSEBUTTONDOWN:
                channel_1.play(NOTIF_2)
                GV.hovered_button = msc.check_hovered(GV.pos, GV.buttons_E)
                if GV.hovered_button:
                    GV.CHOSEN_OPTION = GV.hovered_button.text
                    if GV.CHOSEN_OPTION == 'game':
                        GV.BORDER_1.timer = 0

        if GV.hovered_button:
            GV.hovered_button.HOVERED = False

        GV.hovered_button = msc.check_hovered(GV.pos, GV.buttons_E)

        if GV.hovered_button:
            GV.hovered_button.HOVERED = True

        if GV.CHOSEN_OPTION in ['1', '2', '3', 'back', 'quit']:
            if GV.CHOSEN_OPTION == '1':
                pass
            if GV.CHOSEN_OPTION == '2':
                GV.current_sequence = 7
            if GV.CHOSEN_OPTION == '3':
                GV.current_sequence = 14
            run_main = False

        pygame.display.update()
        clock.tick(FPS)


def recorder(win):

    init_userevent(BPM)

    run_main = True

    while run_main:

        GV.pos = pygame.mouse.get_pos()
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
                    GV.OPTION_B1.text = str(n)
                    GV.OPTION_B1.pos = (10 + 30 * n, 40)

                    GV.chosen_save = n

                if event.key in [K_f]:
                    t = pygame.time.get_ticks()
                    GV.R1.timings.append(t)

                if event.key == [K_j]:
                    t = pygame.time.get_ticks()
                    GV.R1.timings.append(-t)

                if event.key == K_m:
                    mute_all()

                if event.key == K_i:
                    reset_volume()

                if event.key == K_s:
                    volume_up()

                if event.key == K_BACKSPACE:
                    if GV.saved_values:
                        GV.saved_values.pop(-1)
                        GV.SAVED_VALUES_INDIC.update_value_3(GV.saved_values)

                if event.key == K_SPACE:
                    if GV.SAVE_MODE:
                        print(62, 'saved')
                        logs.save_timing_values(logs.DATA_FILE, GV.saved_values, GV.chosen_save)
                        GV.saved_values.clear()

                    GV.SAVE_MODE = not GV.SAVE_MODE
                    GV.OPTION_B1.toggle_color()
                    print(61, 'space', GV.OPTION_B1.col, GV.OPTION_B1.STATE)

                if event.key == K_RETURN:
                    GV.R1.convert_timing_to_value()
                    print(67, GV.R1.values)

                    values = GV.R1.true_values(95)
                    GV.saved_values.append(values)
                    GV.SAVED_VALUES_INDIC.update_value_3(GV.saved_values)

                    logs.save_timing_values(logs.DATA_FILE, GV.saved_values, 0)  # autosave

                    print('recorded list', GV.saved_values)

                    if 0 in values:
                        channel_1.play(NOTIF_2)

                    GV.R1.timings.clear()

            if event.type == GV.METRONOME_BEAT:
                t = pygame.time.get_ticks()
                GV.metronome_indic.timer = 0
                GV.metronome_indic.update_metronome()
                channel_1.play(HI_HAT_B)

                GV.R2.timings.append(t)

                if len(GV.R2.timings) >= 5 and len(GV.player_timings) >= 5:
                    GV.average_diff = GF.get_average_diff(GV.player_timings, GV.R2.timings, BPM)

                    GV.CONTINUE = abs(GV.average_diff) < 80

        if GV.hovered_button:
            GV.hovered_button.HOVERED = False

        GV.hovered_button = msc.check_hovered(GV.pos, GV.buttons_B)

        if GV.hovered_button:
            GV.hovered_button.HOVERED = True

        pygame.display.update()
        clock.tick(FPS)

    stop_userevent()


def calibrate(win):

    init_userevent(BPM)

    run_main = True

    while run_main:

        draw_screen(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_main = False
            if event.type == pygame.KEYDOWN:
                if event.key in [K_q, K_ESCAPE]:
                    run_main = False

                if event.key == K_m:
                    mute_all()

                if event.key == K_i:
                    reset_volume()

                if event.key == K_s:
                    volume_up()

                if event.key == K_SPACE:
                    init_userevent(BPM)

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

    init_userevent(BPM)

    run_main = True

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

                if event.key == K_m:
                    mute_all()

                if event.key == K_i:
                    reset_volume()

                if event.key == K_s:
                    volume_up()

                if event.key == K_SPACE:
                    GV.CHOSEN_OPTION = 'score'

                if event.key == K_8:
                    GV.current_sequence = 6
                    GV.current_disp_sequence = 6

                if event.key in [K_f, K_j]:
                    t = pygame.time.get_ticks()
                    timings = rhy.sequences[GV.current_sequence]['rhythm'].timings

                    GV.R1.timings.append(t)

                    if GV.check_timing_1 != len(timings):
                        if timings[GV.check_timing_1] < 0:
                            GV.check_timing_1 += 1

                        diff = abs(t - GV.start_time - timings[GV.check_timing_1])
                        points = GF.eval_diff(diff)

                        print(31, t - GV.start_time - timings[GV.check_timing_1])
                        print(32, timings, GV.check_timing_1, len(timings))

                        if points:
                            GV.sequence_score += points
                            GV.player_score += points
                            GV.check_timing_1 += 1

                if event.key == K_RETURN:
                    timings2 = GF.synchronized(GV.player_timings)
                    GF.compare_rhythms(timings2, GV.timings1)
                    GV.player_timings.clear()

            if event.type == GV.SEQUENCE_TIMING:
                print(71, GV.current_sequence, rhy.sequences[GV.current_sequence]['rhythm'])
                values = rhy.sequences[GV.current_sequence]['rhythm'].values
                v = values[GV.check_timing_2]

                if v > 0 and GV.check_timing_1 == GV.check_timing_2:
                    GV.player_score += 5
                    GV.check_timing_1 += 1
                else:
                    GV.player_score += 0

                if GV.check_timing_2 == len(values) - 1:
                    pygame.time.set_timer(GV.SEQUENCE_TIMING, 0)
                else:
                    v = values[GV.check_timing_2]

                    #pygame.time.set_timer(GV.SEQUENCE_TIMING, 0)
                    pygame.time.set_timer(GV.SEQUENCE_TIMING, int(v))
                    GV.check_timing_2 += 1

            if event.type == GV.METRONOME_BEAT:
                GV.current_beat += 1
                t = pygame.time.get_ticks()

                print('otime ', t - GV.start_time)

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

                if GV.current_beat == 5:
                    pygame.time.set_timer(GV.SEQUENCE_TIMING, sett.tolerance_2)

            if event.type == GV.METRONOME_HALF_BEAT:
                t = pygame.time.get_ticks()
                print('half beat', t - GV.start_time, GV.current_half_beat, GV.current_beat)
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

                    GV.current_sequence += 1

                    if GV.current_sequence == sett.number_of_sequences:
                        GV.max_score = GF.get_max_score(rhy.sequences)
                        score_ratio = round(GV.player_score * 100 / GV.max_score)
                        anim.initialize_score_list(GV.SCORE_INDIC, score_ratio)
                        print(GV.max_score, score_ratio)

                        GV.CHOSEN_OPTION = 'score'
                        run_main = False
                        print('game over')
                        pygame.time.wait(1100)

                    GV.sequence_score = 0
                    GV.check_timing_1 = 0
                    GV.current_half_beat = 1
                    GV.check_timing_2 = 0
                    GV.start_time = pygame.time.get_ticks()

        GV.metronome_indic.timer += 1
        GV.bg_color_indic.timer += 1

        pygame.display.update()
        clock.tick(FPS)


def score_screen(win):

    run_main = True

    GV.start_time = pygame.time.get_ticks()
    anim.initialize_score_list(GV.SCORE_INDIC, 100)
    GV.SCORE_INDIC.value_2 = []

    while run_main:
        GV.time = pygame.time.get_ticks()
        draw_screen_f(win)
        anim.draw_graph(win, GV.SCORE_INDIC.value_2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_main = False
            if event.type == pygame.KEYDOWN:
                if event.key in [K_q, K_ESCAPE]:
                    run_main = False

                if event.key == K_m:
                    mute_all()

                if event.key == K_i:
                    reset_volume()

                if event.key == K_s:
                    volume_up()

                if event.key == K_RETURN:
                    timings2 = GF.synchronized(GV.player_timings)
                    GF.compare_rhythms(timings2, GV.timings1)
                    GV.player_timings.clear()

        anim.increase_value(GV.SCORE_INDIC, 200)
        print(GV.SCORE_INDIC)

        GV.metronome_indic.timer += 1
        GV.bg_color_indic.timer += 1
        GV.SCORE_INDIC.timer += 1

        pygame.display.update()
        clock.tick(FPS)


def main(win):
    init_sound()

    channel_1.play(NOTIF_2)

    run_main = True

    while run_main:

        main_menu(win)

        reset_game_values()

        if GV.CHOSEN_OPTION == 'record':
            recorder(win)

        if GV.CHOSEN_OPTION == 'calibrate':
            calibrate(win)

        if GV.CHOSEN_OPTION == 'game':
            GV.CHOSEN_OPTION = None
            level_menu(win)

            if GV.CHOSEN_OPTION not in ['back', 'quit']:
                game(win)

        if GV.CHOSEN_OPTION == 'score':
            score_screen(win)

        reset_game_values()

        if GV.CHOSEN_OPTION == 'quit':
            run_main = False

        GV.CHOSEN_OPTION = None

    pygame.quit()


logs.data = logs.load_data(logs.DATA_FILE)

print('\nSound control:\nmute: M   reset volume: I   volume up: S')

main(WIN)

