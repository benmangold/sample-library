import wave, struct


class WaveWriter:
    def __init__(self, path, sample=None, channels=1, sampleRate=44100, bitDepth=16):
        self.path = path
        self.channels = channels
        self.sampleRate = sampleRate
        self.bitDepth = bitDepth

        # if a sample is not provided, write a 1 second empty buffer
        if not sample:
            print("WaveWriter: No sample provided.  Writing Empty Buffer")
            self.sample = [0] * self.sampleRate
        else:
            self.sample = sample

    def write(self):
        out = wave.open(f"{self.path}.wav", "w")
        out.setnchannels(self.channels)  # Mono
        out.setsampwidth(int(self.bitDepth / 8))  # Sample is 2 Bytes
        out.setframerate(self.sampleRate)  # Sampling Frequency
        out.setcomptype("NONE", "Not Compressed")
        BinStr = b""  # Create a binary string of data
        for i in range(len(self.sample)):
            BinStr = BinStr + struct.pack("h", round(self.sample[i] * 20000))
        out.writeframesraw(BinStr)
        out.close()
