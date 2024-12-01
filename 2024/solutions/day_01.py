from collections import Counter


def part_1(input_file):
    ls, rs = zip(*[(int(x), int(y)) for x, y in [l.split() for l in input_file]])
    ls = sorted(ls)
    rs = sorted(rs)

    return sum(abs(l - r) for l, r in zip(ls, rs))


def part_2(input_file):
    ls, rs = zip(*[(int(x), int(y)) for x, y in [l.split() for l in input_file]])

    number_count = Counter(rs)

    return sum(i * number_count.get(i, 0) for i in ls)
