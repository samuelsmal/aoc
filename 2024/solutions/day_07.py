import io
import re
from typing import Any
from operator import add, mul


def part_1(input_file: io.TextIOWrapper) -> Any:
    result = 0

    for line in input_file:
        target, first, *rest = map(int, re.findall(r"\d+", line))

        candidates = [first]

        for number in rest:
            candidates = [op(x, number) for x in candidates for op in (add, mul)]

        if target in candidates:
            result += target

    return result


def cat(x, y):
    return int(str(x) + str(y))


def part_2(input_file: io.TextIOWrapper) -> Any:
    result = 0

    for line in input_file:
        target, first, *rest = map(int, re.findall(r"\d+", line))

        candidates = [first]

        for number in rest:
            candidates = [op(x, number) for x in candidates for op in (add, mul, cat)]

        if target in candidates:
            result += target

    return result
