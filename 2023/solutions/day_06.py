import math


def part_1(input_file):
    races = [map(int, line.split()[1:]) for line in input_file]

    wins = 1
    for time, dist in zip(*races):
        n_possible_wins = sum((time - hold) * hold > dist for hold in range(time))
        wins *= n_possible_wins

    return wins


def part_2(input_file):
    time, dist = [int(line.replace(" ", "").split(":")[1]) for line in input_file]

    a = (time - math.sqrt(time**2 - 4 * dist)) / 2
    b = (time + math.sqrt(time**2 - 4 * dist)) / 2

    return math.floor(b) - math.ceil(a) + 1
