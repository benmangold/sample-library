from math import sin, pi
from WaveGenerator import WaveGenerator


def generateSine(N: int, params={}):
    y = N * [0]  # [0,0,0,.....,0]
    for i in range(N):  # [0,1,2,...,N]:
        y1 = 4 / pi * sin(2 * pi * i / N)
        y[i] = y1
    return y


class SineGenerator:
    def __init__(self, noteFrequency, params={}):
        self.buffer = WaveGenerator(generateSine, noteFrequency, params).generate()

    def getBuffer(self):
        return self.buffer
