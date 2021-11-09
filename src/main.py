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

    SampleCollection(SquareGenerator, {"n": 2}, notes, "fourier_squares_two")
    SampleCollection(SquareGenerator, {"n": 3}, notes, "fourier_squares_three")
    SampleCollection(SquareGenerator, {"n": 5}, notes, "fourier_squares_five")

    SampleCollection(MerpGenerator, {"n": 3}, notes, "merp_three")
    SampleCollection(MerpGenerator, {"n": 5}, notes, "merp_five")

    SampleCollection(MeepGenerator, {"n": 3}, notes, "meep_three")
    SampleCollection(MeepGenerator, {"n": 5}, notes, "meep_five")
except:
    traceback.print_exc()
