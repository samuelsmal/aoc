import io
import re
from typing import Any

import numpy as np


def part_1(input_file: io.TextIOWrapper) -> Any:
    def solve(d):
        ax, ay, bx, by, X, Y = map(int, re.findall(r"\d+", d))

        i = (bx * Y - by * X) / (ay * bx - ax * by)
        j = (X - i * ax) / bx

        if (X - i * ax) % bx == 0 and (bx * Y - by * X) % (ay * bx - ax * by) == 0:
            return 3 * int(i) + int(j)
        else:
            return 0

    data = input_file.read().split("\n\n")
    return sum(map(solve, data))


def part_2(input_file: io.TextIOWrapper) -> Any:
    def solve(d):
        ax, ay, bx, by, X, Y = map(int, re.findall(r"\d+", d))

        X += 1e13
        Y += 1e13

        i = (bx * Y - by * X) / (ay * bx - ax * by)
        j = (X - i * ax) / bx

        if (X - i * ax) % bx == 0 and (bx * Y - by * X) % (ay * bx - ax * by) == 0:
            return 3 * int(i) + int(j)
        else:
            return 0

    data = input_file.read().split("\n\n")
    return sum(map(solve, data))
