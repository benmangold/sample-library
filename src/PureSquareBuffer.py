from math import sin, pi

from WaveGenerator import WaveGenerator


def generatePureSquare(N, params={}):
    y = N * [0]  # [0,0,0,.....,0]
    for i in range(N):  # [0,1,2,...,N]:
        if i < N / 2:
            y[i] = 1.0
        else:
            y[i] = -1.0
    return y


class PureSquareBuffer:
    def __init__(self, noteFrequency, params, sampleRate=44100):
        self.buffer = WaveGenerator(
            generatePureSquare, noteFrequency, params
        ).generate()

    def getBuffer(self):
        return self.buffer
