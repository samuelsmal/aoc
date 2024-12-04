import re
from io import TextIOWrapper


def part_1(input_file: TextIOWrapper):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, "".join(input_file.readlines()))

    return sum(int(m[0]) * int(m[1]) for m in matches)


def part_2(input_file):
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    matches = re.findall(pattern, "".join(input_file.readlines()))

    enabled = True
    result = 0

    for m in matches:
        match m[0]:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _ if enabled:
                result += int(m[1]) * int(m[2])

    return result
