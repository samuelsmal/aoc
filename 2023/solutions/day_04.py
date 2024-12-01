from collections import defaultdict


def part_1(input_file):
    lines = [l.strip() for l in input_file]

    total_points = 0

    for l in lines:
        card_number, numbers = l.split(":")
        winning_numbers, drawn_numbers = numbers.strip().split("|")
        winning_numbers = set(int(i) for i in winning_numbers.strip().split(" ") if i)
        drawn_numbers = set(int(i) for i in drawn_numbers.strip().split(" ") if i)

        overlap = winning_numbers.intersection(drawn_numbers)
        points = int((len(overlap) > 0)) * (2 ** (len(overlap) - 1))
        total_points += points

    return int(total_points)


def part_2(input_file):
    lines = [l.strip() for l in input_file]

    n_cards_won = defaultdict(int)

    for i, line in enumerate(lines):
        _, line = line.split(": ")
        winning_numbers, drawn_numbers = map(str.split, line.split(" | "))
        n_matches = sum(drawn_numbers.count(w) for w in winning_numbers)

        n_cards_won[i] += 1
        for j in range(i + 1, i + n_matches + 1):
            n_cards_won[j] += n_cards_won[i]

    return sum(n_cards_won.values())
