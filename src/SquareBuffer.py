from math import sin, pi
from WaveGenerator import WaveGenerator


def generateSquare(N, params):
    harmonics = params["n"]
    y = N * [0]  # [0,0,0,.....,0]
    for i in range(N):  # [0,1,2,...,N]:
        sum = 0
        for harmonic in range(harmonics):
            n = 1 + (harmonic * 2)  # 0=1, 1=3, 2=5, etc.
            value = 4 / (n * pi) * sin(2 * n * pi * i / N)
            sum = sum + value
        y[i] = sum
    return y


class SquareBuffer:
    def __init__(self, noteFrequency, params={}, sampleRate=44100):
        self.buffer = WaveGenerator(generateSquare, noteFrequency, params).generate()

    def getBuffer(self):
        return self.buffer
