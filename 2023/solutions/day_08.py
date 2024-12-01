import math
from itertools import cycle


def part_1(input_file):
    instructions, mappings = input_file.read().split("\n\n")
    mappings = [m.split(" = ") for m in mappings.splitlines()]
    mappings = {a: b[1:-1].split(", ") for a, b in mappings}

    current_position = "AAA"

    for step_counter, instruction in enumerate(cycle(instructions), start=1):
        current_position = mappings[current_position][instruction == "R"]
        if current_position == "ZZZ":
            return step_counter


def part_2(input_file):
    instructions, mappings = input_file.read().split("\n\n")
    mappings = [m.split(" = ") for m in mappings.splitlines()]
    mappings = {a: b[1:-1].split(", ") for a, b in mappings}

    step_counts = []

    for current in mappings:
        if not current.endswith("A"):
            continue

        # It's possible to have multiple different paths to a solution.
        # The trick is to avoid unnecessary compute steps, meaning when to know that a circle was reached.
        already_visited = set()

        for count, (loop_counter, instruction) in enumerate(
            cycle(enumerate(instructions)), start=1
        ):
            previous, current = current, mappings[current][instruction == "R"]
            already_visited.add((current, loop_counter))

            if previous.endswith("Z") and (current, loop_counter) in already_visited:
                step_counts.append(count - 1)
                break

    return math.lcm(*step_counts)
