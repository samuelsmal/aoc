import io
from itertools import permutations
from typing import Any


def part_1(input_file: io.TextIOWrapper) -> Any:
    grid = {
        i + j * 1j: c for i, r in enumerate(input_file) for j, c in enumerate(r.strip())
    }

    antinodes = []

    for frequency in {*grid.values()} - {"."}:
        matches = [k for k, v in grid.items() if v == frequency]
        pairs = permutations(matches, 2)

        antinodes += [a + (a - b) for a, b in pairs]

    return len(set(antinodes) & set(grid))


def part_2(input_file: io.TextIOWrapper) -> Any:
    grid = {
        i + j * 1j: c for i, r in enumerate(input_file) for j, c in enumerate(r.strip())
    }

    antinodes = []

    for frequency in {*grid.values()} - {"."}:
        matches = [k for k, v in grid.items() if v == frequency]
        pairs = list(permutations(matches, 2))

        for n in range(50):
            antinodes += [a + n * (a - b) for a, b in pairs]

    return len(set(antinodes) & set(grid))
