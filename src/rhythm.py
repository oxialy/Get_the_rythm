


import pygame



class Rhythm:
    def __init__(self):
        self.timings = []
        self.notes = []

    def convert_timing_to_note_value(self):
        self.notes.clear()
        for t1, t2 in zip(self.timings[:-1], self.timings[1:]):
            note_value = t2 - t1

            self.notes.append(note_value)






