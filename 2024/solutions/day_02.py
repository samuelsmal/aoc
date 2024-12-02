from typing import List


def is_safe_part_1(report):
    diffs = [b - a for a, b in zip(report[:-1], report[1:])]

    if diffs[0] > 0:
        return all(d > 0 for d in diffs) and all(0 < abs(d) < 4 for d in diffs)
    else:
        return all(d < 0 for d in diffs) and all(0 < abs(d) < 4 for d in diffs)


def part_1(input_file):
    return sum(is_safe_part_1([int(i) for i in line.split()]) for line in input_file)


def is_safe_without(report: List[int], pos: int) -> bool:
    report = report[0:pos] + report[pos + 1 :]
    diffs = [b - a for a, b in zip(report[:-1], report[1:])]

    if diffs[0] > 0:
        return all(d > 0 for d in diffs) and all(0 < abs(d) < 4 for d in diffs)
    else:
        return all(d < 0 for d in diffs) and all(0 < abs(d) < 4 for d in diffs)


def is_safe_part_2(report):
    if is_safe_part_1(report):
        return True
    else:
        for pos in range(len(report)):
            if is_safe_without(report, pos):
                return True

    return False


def part_2(input_file):
    return sum(is_safe_part_2([int(i) for i in line.split()]) for line in input_file)
