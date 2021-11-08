import traceback, json, os

from SineGenerator import SineGenerator
from SquareGenerator3Harmonics import SquareGenerator3Harmonics
from SquareGeneratorPure import SquareGeneratorPure
from SampleCollection import SampleCollection
from SquareGenerator import SquareGenerator
from MerpGenerator import MerpGenerator

with open("data/notes.json", "r") as notesFile:
    notesData = notesFile.read()

notes = json.loads(notesData)

try:
    SampleCollection(SineGenerator, {}, notes, "basic_sines").write()
    SampleCollection(SquareGenerator3Harmonics, {}, notes, "basic_squares_three").write()
    SampleCollection(SquareGeneratorPure, {}, notes, "basic_squares_pure").write()
    # SampleCollection(SquareGenerator, {'n': 5},notes, "basic_squares_five").write()
    # SampleCollection(SquareGenerator, {'n': 3},notes, "basic_squares_three_b").write()

    SampleCollection(MerpGenerator, {'n': 3}, notes, "merp_three").write()
    SampleCollection(MerpGenerator, {'n': 13}, notes, "merp_thirteen").write()
except:
    traceback.print_exc()
