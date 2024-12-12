import io
from typing import Any


def evolve(stone):
    if stone == 0:
        return (1,)
    elif len(str(stone)) % 2 == 0:
        _s = str(stone)
        return (int(_s[: len(_s) // 2]), int(_s[len(_s) // 2 :]))
    else:
        return (stone * 2024,)


def flatten(xss):
    return [x for xs in xss for x in xs]


def part_1(input_file: io.TextIOWrapper) -> Any:
    stones = [int(s) for s in input_file.read().strip().split(" ")]

    for _ in range(25):
        stones = flatten(evolve(s) for s in stones)

    return len(stones)


def part_2(input_file: io.TextIOWrapper) -> Any:
    from functools import cache
    from math import floor, log10

    # Directly counting to build up the tree

    @cache
    def count(x, d=75):
        if d == 0:
            return 1
        if x == 0:
            return count(1, d - 1)

        l = floor(log10(x)) + 1
        if l % 2:
            return count(x * 2024, d - 1)

        return count(x // 10 ** (l // 2), d - 1) + count(x % 10 ** (l // 2), d - 1)

    data = map(int, input_file.read().split())
    return sum(map(count, data))
