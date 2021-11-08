from math import sin, pi


class SineGenerator:
    def __init__(self, noteFrequency, sampleRate=44100):
        self.sampleRate = sampleRate
        self.noteFrequency = noteFrequency
        self.samplePeriod = 1 / self.sampleRate
        self.notePeriodSeconds = 1 / self.noteFrequency
        self.notePeriodSamples = int(self.notePeriodSeconds / self.samplePeriod)

    def generate(self, params=None):
        N = self.notePeriodSamples
        y = N * [0]  # [0,0,0,.....,0]
        for i in range(N):  # [0,1,2,...,N]:
            y1 = 4 / pi * sin(2 * pi * i / N)
            y[i] = y1
        y = 10 * y  # 10 periods, y length is now 10*N
        return y
