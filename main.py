from sources import read_input_txt, read_stdin
from sources import Puzzle1507


def transformer(line):
    s, e = line.split(" -> ")
    return (s, e)


connections = read_stdin(transformer)
if connections is None:
    connections = read_input_txt(15, 7, transformer)

puzzle = Puzzle1507()
wires = puzzle.solveA(connections)
signal_overrides = {}
signal_overrides["b"] = wires["a"]
wires = puzzle.solveB(connections, signal_overrides)
print(wires["a"])
