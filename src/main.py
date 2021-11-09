import traceback, json, os

from SineGenerator import SineGenerator
from PureSquareGenerator import PureSquareGenerator
from SampleCollection import SampleCollection
from SquareGenerator import SquareGenerator
from MerpGenerator import MerpGenerator
from MeepGenerator import MeepGenerator

with open("data/notes.json", "r") as notesFile:
    notesData = notesFile.read()

notes = json.loads(notesData)

try:
    SampleCollection(SineGenerator, {}, notes, "simple_sines")

    SampleCollection(PureSquareGenerator, {}, notes, "simple_squares")

    SampleCollection(SquareGenerator, {"n": 2}, notes, "fourier_squares_II")
    SampleCollection(SquareGenerator, {"n": 3}, notes, "fourier_squares_III")
    SampleCollection(SquareGenerator, {"n": 5}, notes, "fourier_squares_V")

    SampleCollection(MerpGenerator, {"n": 3}, notes, "merp_III")
    SampleCollection(MerpGenerator, {"n": 5}, notes, "merp_V")

    SampleCollection(MeepGenerator, {"n": 3}, notes, "meep_III")
    SampleCollection(MeepGenerator, {"n": 5}, notes, "meep_V")
except:
    traceback.print_exc()
