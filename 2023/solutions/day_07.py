from collections import Counter
from itertools import product


def rank(cards):
    # Corresponds to the hands
    match [count for val, count in Counter(cards).most_common()]:
        case 5, *_:
            return 1
        case 4, *_:
            return 2
        case 3, 2, *_:
            return 3
        case 3, *_:
            return 4
        case 2, 2, *_:
            return 5
        case 2, *_:
            return 6
        case _:
            return 7


def part_1(input_file):
    order = "AKQJT98765432"

    vals = []

    for line in input_file:
        hand, bid = line.split()
        vals.append((rank(hand), [order.index(card) for card in hand], int(bid)))

    vals.sort(reverse=True)

    return sum((i + 1) * v[-1] for i, v in enumerate(vals))


def part_2(input_file):
    order = "AKQT98765432J"

    vals = []

    for line in input_file:
        hand, bid = line.split()
        rank_ = rank(hand)

        for s in product(order[:-1], repeat=hand.count("J")):
            rank_ = min(rank_, rank(hand.replace("J", "") + "".join(s)))

        vals.append((rank_, [order.index(card) for card in hand], int(bid)))

    vals.sort(reverse=True)

    return sum((i + 1) * v[-1] for i, v in enumerate(vals))
