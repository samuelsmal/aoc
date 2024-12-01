from itertools import pairwise


def process_line(line):
    if all(i == 0 for i in line):
        return 0
    diffs = [b - a for a, b in pairwise(line)]
    return line[-1] + process_line(diffs)


def part_1(input_file):
    return sum(process_line([int(i) for i in line.split()]) for line in input_file)


def part_2(input_file):
    return sum(
        process_line([int(i) for i in line.split()[::-1]]) for line in input_file
    )
