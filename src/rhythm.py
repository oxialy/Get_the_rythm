


import pygame


VALUE_MAPPING = {0.25 * x: 250 * x for x in range(1,16)}



class Rhythm:
    def __init__(self):
        self.timings = []
        self.notes = []

    def convert_timing_to_note_value(self):
        self.notes.clear()
        for t1, t2 in zip(self.timings[:-1], self.timings[1:]):
            note_value = t2 - t1

            self.notes.append(note_value)

    def true_values(self, tol):
        return adjust_to_true_note_value(self.notes, tol)

def adjust_to_true_note_value(values, tol):
    new_values = []

    for val in values:
        true_val = 0

        for val0 in [250 * x for x in range(1,16)] + [1000/3 * x for x in range(1,12)]:
            if val0 - tol <= val <= val0 + tol:
                true_val = val0
                break
        new_values.append(true_val)

    return new_values


def adjust_value_to_bpm(values, bpm):
    new_values = []

    for val in values:
        pass










