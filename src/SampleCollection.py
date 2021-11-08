from WaveWriter import WaveWriter

import os


class SampleCollection:
    def __init__(self, waveGenerator, waveGeneratorParams, notes, path):
        self.generator = waveGenerator
        self.generatorParams = waveGeneratorParams
        self.notes = notes
        self.path = path
        dirname = os.path.dirname(__file__)
        self.directory = os.path.join(dirname, f"../lib/{self.path}")
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def write(self):
        for note in self.notes:
            buffer = self.generator(note["hertz"]).generate(self.generatorParams)
            filename = f"{self.path}_{note['note_num']}_{note['note_flat']}"
            path = f"{self.directory}/{filename}"
            WaveWriter(path, buffer).write()
