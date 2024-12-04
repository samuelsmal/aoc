from collections import defaultdict


def part_1(input_file):
    # the horizontal letters
    letters = [line.strip() for line in input_file]

    n_rows = len(letters)
    n_cols = len(letters[0])

    # the vertical lines
    vertical_lines = list(map(list, zip(*[[l for l in line] for line in letters])))

    # the diagonals left to right
    diag_left = defaultdict(list)
    diag_right = defaultdict(list)

    # the key is that we don't need to care about if the diagonals are complete
    for row in range(n_rows):
        for col in range(n_cols):
            begin = row - col
            diag_left[begin].append(letters[row][col])

            begin = row + col
            diag_right[begin].append(letters[row][col])

    letters.extend("".join(line) for line in vertical_lines)
    letters.extend("".join(line) for line in diag_left.values())
    letters.extend("".join(line) for line in diag_right.values())

    return sum(line.count("XMAS") + line.count("SAMX") for line in letters)


def part_2(input_file):
    # the horizontal letters
    letters = [line.strip() for line in input_file]

    n_rows = len(letters)
    n_cols = len(letters[0])

    count = 0

    for row in range(1, n_rows - 1):
        for col in range(1, n_cols - 1):
            if all(
                (
                    letters[row][col] == "A",
                    letters[row - 1][col - 1] + letters[row + 1][col + 1]
                    in ("MS", "SM"),
                    letters[row - 1][col + 1] + letters[row + 1][col - 1]
                    in ("MS", "SM"),
                )
            ):
                count += 1

    return count
