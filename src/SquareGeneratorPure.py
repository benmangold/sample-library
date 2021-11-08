from math import sin, pi


class SquareGeneratorPure:
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
            if i < N / 2:
                y[i] = 1.0
            else:
                y[i] = -1.0
        y = 10 * y  # 10 periods, y length is now 10*N
        return y
