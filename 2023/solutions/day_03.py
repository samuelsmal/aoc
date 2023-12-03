import math
import re
from collections import defaultdict


def adjacent_indexes(line_index, number_start, number_end, schema_width, schema_length):
    for x, y in [
        (x, line_index + y_i)
        for x in range(number_start - 1, number_end + 1)
        for y_i in (-1, 0, 1)
    ]:
        if (
            x >= 0
            and x < schema_width
            and y >= 0
            and y < schema_length
            and not (y == line_index and (number_start <= x <= number_end - 1))
        ):
            yield (x, y)


def validate_part_candidate(candidate, input_, line, line_index):
    for x, y in adjacent_indexes(
        line_index, candidate.span()[0], candidate.span()[1], len(line), len(input_)
    ):
        candidate_symbol = input_[y][x]
        if candidate_symbol != "." and not candidate_symbol.isalpha():
            return int(candidate.group())


def get_surrounding_numbers(surrounding_fields, input_):
    for x, y in surrounding_fields:
        # print(f"{x}, {y}, {input_[y][x]}")
        if input_[y][x].isdigit():
            for number in re.finditer(r"\d+", input_[y]):
                if number.span()[0] <= x <= number.span()[1]:
                    yield number


def part_1(input_file):
    lines = [l.strip() for l in input_file]
    part_numbers = []
    for line_index, line in enumerate(lines):
        for number_match in re.finditer(r"\d+", line):
            validated = validate_part_candidate(number_match, lines, line, line_index)

            if validated:
                part_numbers.append(validated)

    return sum(part_numbers)


def part_2(input_file):
    """For Part2 I got the wrong answer if I checked for only gears with `*` as a symbol.
    Prompting a rewrite."""
    lines = [l.strip() for l in input_file]

    adj = defaultdict(list)
    for i, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            # Both sides of the match
            idxs = [(match.start() - 1, i), (match.end(), i)]
            # Above
            idxs += [(j, i - 1) for j in range(match.start() - 1, match.end() + 1)]
            # Below
            idxs += [(j, i + 1) for j in range(match.start() - 1, match.end() + 1)]

            for x, y in idxs:
                if (
                    0 <= y < len(lines)
                    and 0 <= x < len(lines[y])
                    and lines[y][x] != "."
                ):
                    adj[y, x].append(int(match.group()))

    return sum(math.prod(vs) for vs in adj.values() if len(vs) == 2)
