

VALUE_MAPPING = {0.25 * x: 250 * x for x in range(1,16)}


class Rhythm:
    def __init__(self, timings, values, start=0):
        self.timings = timings
        self.values = values

        self.start = start

        self.max_points = 100 * len(values)

    def __repr__(self):
        return repr((len(self.timings), len(self.values), self.values))

    def convert_timing_to_value(self):
        self.values.clear()
        for t1, t2 in zip(self.timings[:-1], self.timings[1:]):
            note_value = t2 - abs(t1)
            if t1 < 0:
                self.values.append(-note_value)
            else:
                self.values.append(note_value)

    def convert_value_to_timing(self, start_time=0):
        self.timings.clear()

        t = start_time

        self.timings.append(start_time)

        for val in self.values:
            if val < 0:
                self.timings[-1] *= -1
            #self.timings[-1] *= 1 - 2 * (val < 0)
            t += abs(val)
            self.timings.append(t)

    def true_values(self, tol):
        return adjust_to_true_note_value(self.values, tol)

    def adjust_value_to_bpm(self, bpm):
        self.values = adjust_value_to_bpm(self.values, bpm)

    def adjust_timing_to_bpm(self, bpm):
        self.timings = adjust_value_to_bpm(self.timings, bpm)

def adjust_to_true_note_value(values, tol):
    new_values = []

    for val in values:
        true_val = 0
        for val0 in [250 * x for x in range(-4, 4)] + [1000/3 * x for x in range(-3, 3)]:
            if val0 - tol <= val <= val0 + tol:
                true_val = val0
                break
        new_values.append(true_val)

    return new_values


def adjust_value_to_bpm(values, bpm):
    new_values = []
    k = bpm / 60

    for val in values:
        new_val = val * k
        new_values.append(new_val)

    return new_values


def convert_all_timing_to_value(rhythms):
    for r in rhythms:
        r.convert_timing_to_value()


def convert_all_value_to_timing(rhythms, start_time=0):
    for r in rhythms:
        r.convert_value_to_timing(start_time)











