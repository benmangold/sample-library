from math import sin, pi


class MerpGenerator:
    def __init__(self, noteFrequency, sampleRate=44100):
        self.sampleRate = sampleRate  # herts
        self.noteFrequency = noteFrequency  # hertz
        self.samplePeriod = 1 / self.sampleRate  # seconds
        self.notePeriodSeconds = 1 / self.noteFrequency
        self.notePeriodSamples = int(self.notePeriodSeconds / self.samplePeriod)

    def generate(self, params):
        N = self.notePeriodSamples
        harmonics = params["n"]
        y = N * [0]  # [0,0,0,.....,0]
        for i in range(N):  # [0,1,2,...,N]:
            sum = 0
            for harmonic in range(harmonics):
                n = harmonic + 1
                value = (4 / (pi * n) * sin((2 * n) * pi * i / N)) / n
                sum = sum + value
            y[i] = sum
        y = 10 * y  # 10 periods, y length is now 10*N
        return y
