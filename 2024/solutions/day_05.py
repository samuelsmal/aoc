from functools import cmp_to_key


def part_1(input_file):
    rules, pages = input_file.read().strip().split("\n\n")
    rules = {tuple(map(int, x.split("|"))) for x in rules.split()}
    pages = [list(map(int, x.split(","))) for x in pages.split()]

    # The idea is to use the rules to sort them, the comparator is basically given.
    # If the specific page stays the same, everything is in order.
    key = cmp_to_key(lambda a, b: ((b, a) in rules) - ((a, b) in rules))

    return sum(row[len(row) // 2] for row in pages if row == sorted(row, key=key))


def part_2(input_file):
    rules, pages = input_file.read().strip().split("\n\n")
    rules = {tuple(map(int, x.split("|"))) for x in rules.split()}
    pages = [list(map(int, x.split(","))) for x in pages.split()]

    key = cmp_to_key(lambda a, b: ((b, a) in rules) - ((a, b) in rules))

    # Only difference is that we need the newly sorted page.
    return sum(
        new_row[len(row) // 2]
        for row in pages
        if row != (new_row := sorted(row, key=key))
    )
