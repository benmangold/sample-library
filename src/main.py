import traceback, json, os

from SampleCollection import SampleCollection

from SineBuffer import SineBuffer
from PureSquareBuffer import PureSquareBuffer
from SquareBuffer import SquareBuffer
from MerpBuffer import MerpBuffer
from MeepBuffer import MeepBuffer

with open("data/notes.json", "r") as notesFile:
    notesData = notesFile.read()

notes = json.loads(notesData)

try:
    SampleCollection(SineBuffer, {}, notes, "simple_sines")

    SampleCollection(PureSquareBuffer, {}, notes, "simple_squares")

    SampleCollection(SquareBuffer, {"n": 1}, notes, "fourier_squares_I")
    SampleCollection(SquareBuffer, {"n": 2}, notes, "fourier_squares_II")
    SampleCollection(SquareBuffer, {"n": 3}, notes, "fourier_squares_III")
    SampleCollection(SquareBuffer, {"n": 5}, notes, "fourier_squares_V")

    SampleCollection(MerpBuffer, {"n": 1}, notes, "merp_I")
    SampleCollection(MerpBuffer, {"n": 2}, notes, "merp_II")
    SampleCollection(MerpBuffer, {"n": 3}, notes, "merp_III")
    SampleCollection(MerpBuffer, {"n": 5}, notes, "merp_V")

    SampleCollection(MeepBuffer, {"n": 1}, notes, "meep_I")
    SampleCollection(MeepBuffer, {"n": 2}, notes, "meep_II")
    SampleCollection(MeepBuffer, {"n": 3}, notes, "meep_III")
    SampleCollection(MeepBuffer, {"n": 5}, notes, "meep_V")
except:
    traceback.print_exc()
