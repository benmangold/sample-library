from math import sin, pi
from WaveGenerator import WaveGenerator


def generateMeep(N, params):
    harmonics = params["n"]
    y = N * [0]  # [0,0,0,.....,0]
    for i in range(N):  # [0,1,2,...,N]:
        sum = 0
        for harmonic in range(harmonics):
            n = (harmonic + 1) + (harmonic * 2)
            value = 4 / (pi * n) * sin((2 * n) * pi * i / N)
            sum = sum + value
        y[i] = sum / 2
    return y


class MeepBuffer:
    def __init__(self, noteFrequency, params, sampleRate=44100):
        self.params = params
        self.buffer = WaveGenerator(generateMeep, noteFrequency, params).generate()

    def getBuffer(self):
        return self.buffer
