"""Advent of Code 2015, day 7: Some Assembly Required"""

from collections import defaultdict, deque
from typing import Optional


class Puzzle1507:

    BITWISE_OPS = {"AND", "OR", "NOT", "LSHIFT", "RSHIFT"}
    MAX_VALUE = 65535

    def __init__(self):
        pass

    def solveA(
        self,
        connections: list[tuple[str, str]],
        signal_overrides: Optional[dict[str, int]] = None,
    ):
        dependents, indegree, signal_map, wires = defaultdict(list), {}, {}, {}
        for signal, wire in connections:
            deps = self._parse_dependencies(signal)
            indegree[wire] = len(deps)
            signal_map[wire] = signal
            if signal_overrides and wire in signal_overrides:
                signal_map[wire] = str(signal_overrides[wire])
            for dep in deps:
                dependents[dep].append(wire)
        queue = deque([w for w in indegree if indegree[w] == 0])

        while queue:
            wire = queue.popleft()
            signal = signal_map[wire]
            wires[wire] = self._evaluate_signal(signal, wires)

            for dependent in dependents[wire]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    queue.append(dependent)

        return wires

    def solveB(
        self, connections: list[tuple[str, str]], signal_overrides: dict[str, int]
    ):
        return self.solveA(connections, signal_overrides)

    def _parse_dependencies(self, signal):
        tokens = signal.split()
        deps = []
        for token in tokens:
            if not token.isnumeric() and token not in self.BITWISE_OPS:
                deps.append(token)
        return deps

    def _evaluate_signal(self, signal, wires):
        tokens = signal.split()

        def get(x):
            return int(x) if x.isnumeric() else wires[x]

        match tokens:
            case [a]:
                return get(a)
            case [a, "AND", b]:
                return get(a) & get(b)
            case [a, "OR", b]:
                return get(a) | get(b)
            case [a, "LSHIFT", b]:
                return (get(a) << get(b)) & self.MAX_VALUE
            case [a, "RSHIFT", b]:
                return get(a) >> get(b)
            case ["NOT", a]:
                return (~get(a)) & self.MAX_VALUE
