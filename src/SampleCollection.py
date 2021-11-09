from WaveWriter import WaveWriter

import os


class SampleCollection:
    def __init__(self, waveGenerator, waveGeneratorParams, notes, path):
        dirname = os.path.dirname(__file__)
        directory = os.path.join(dirname, f"../lib/{path}")
        if not os.path.exists(directory):
            os.makedirs(directory)

        for note in notes:
            buffer = waveGenerator(note["hertz"], waveGeneratorParams).getBuffer()
            buffer = 10 * buffer  # lengthen sample to 10 cycles
            filename = f"{path}_{note['note_num']}_{note['note_flat']}"
            filePath = f"{directory}/{filename}"
            WaveWriter(filePath, buffer)
