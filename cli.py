import argparse
import traceback
from datetime import datetime
from importlib import import_module


def run(fn, input_filename):
    with open(input_filename) as f:
        try:
            return fn(f)
        except:
            traceback.print_exc()


if __name__ == "__main__":
    now = datetime.now()
    parser = argparse.ArgumentParser(
        description="CLI to run the Advent of Code puzzles."
    )
    parser.add_argument(
        "--year", "-y", type=int, help="The year to run.", default=now.year
    )
    parser.add_argument(
        "--day", "-d", type=int, help="The day to run.", default=now.day
    )
    args = parser.parse_args()

    solution_module = f"{args.year}.solutions.day_{args.day:02}"

    print(f"#---  AOC   ---#")
    print(f"AOC solution for {solution_module}:")

    module = import_module(solution_module)

    for part in ("part_1", "part_2"):
        if not hasattr(module, part):
            continue

        print(f"#--- {part} ---#")
        print(
            f"Sample:\t{run(getattr(module, part), f'./{args.year}/input/day_{args.day:02}_sample.txt')}"
        )
        print(
            f"Input:\t{run(getattr(module, part), f'./{args.year}/input/day_{args.day:02}.txt')}"
        )
