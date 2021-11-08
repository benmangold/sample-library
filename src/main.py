import traceback, json, os

from SineGenerator import SineGenerator
from SquareGenerator3Harmonics import SquareGenerator3Harmonics
from SquareGeneratorPure import SquareGeneratorPure
from SampleCollection import SampleCollection

with open("data/notes.json", "r") as notesFile:
    notesData = notesFile.read()

notes = json.loads(notesData)

try:
    SampleCollection(SineGenerator, notes, "basic_sines").write()
    SampleCollection(SquareGenerator3Harmonics, notes, "basic_squares_3").write()
    SampleCollection(SquareGeneratorPure, notes, "basic_squares_pure").write()
except:
    traceback.print_exc()
