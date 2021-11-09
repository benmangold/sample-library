import traceback, json, os

from SineGenerator import SineGenerator
from SquareGeneratorPure import SquareGeneratorPure
from SampleCollection import SampleCollection
from SquareGenerator import SquareGenerator
from MerpGenerator import MerpGenerator
from MeepGenerator import MeepGenerator

with open("data/notes.json", "r") as notesFile:
    notesData = notesFile.read()

notes = json.loads(notesData)

try:
    SampleCollection(SineGenerator, {}, notes, "basic_sines").write()

    SampleCollection(SquareGeneratorPure, {}, notes, "basic_squares_pure").write()

    SampleCollection(SquareGenerator, {"n": 3}, notes, "basic_squares_three").write()
    SampleCollection(SquareGenerator, {"n": 5}, notes, "basic_squares_five").write()
    SampleCollection(SquareGenerator, {"n": 10}, notes, "basic_squares_ten").write()

    SampleCollection(MerpGenerator, {"n": 3}, notes, "merp_three").write()
    SampleCollection(MerpGenerator, {"n": 5}, notes, "merp_five").write()

    SampleCollection(MeepGenerator, {"n": 3}, notes, "meep_three").write()
    SampleCollection(MeepGenerator, {"n": 5}, notes, "meep_five").write()
except:
    traceback.print_exc()
