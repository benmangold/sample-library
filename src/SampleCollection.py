from WaveWriter import WaveWriter

import os


class SampleCollection:
    def __init__(self, waveBuffer, waveBufferParams, notes, path):
        print(f"SampleCollection: {path}")
        dirname = os.path.dirname(__file__)
        directory = os.path.join(dirname, f"../lib/{path}")
        if not os.path.exists(directory):
            os.makedirs(directory)

        for note in notes:
            buffer = waveBuffer(note["hertz"], waveBufferParams).getBuffer()
            buffer = 10 * buffer  # lengthen sample to 10 cycles
            filename = f"{path}_{note['note_num']}_{note['note_flat']}"
            filePath = f"{directory}/{filename}"
            WaveWriter(filePath, buffer)
