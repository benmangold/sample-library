from math import sin, pi


class WaveGenerator:
    def __init__(self, generatorFunction, noteFrequency, params={}, sampleRate=44100):
        self.generatorFunction = generatorFunction
        self.params = params
        samplePeriod = 1 / sampleRate
        notePeriodSeconds = 1 / noteFrequency
        self.N = int(
            notePeriodSeconds / samplePeriod
        )  # length of one oscillation/cycle/period of the the note in samples

    def generate(self):
        return self.generatorFunction(
            self.N, self.params
        )  # we pass the generator function N and params
