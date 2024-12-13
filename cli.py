import argparse
import traceback
import time
from datetime import datetime
from importlib import import_module


def run(fn, input_filename):
    try:
        with open(input_filename) as f:
            try:
                return fn(f)
            except:
                traceback.print_exc()
    except FileNotFoundError:
        return f"File is missing {input_filename}"


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
        start = time.perf_counter_ns()
        solution = run(
            getattr(module, part), f"./{args.year}/input/day_{args.day:02}_sample.txt"
        )
        end = time.perf_counter_ns()
        print(f"Sample:\t{solution}\tSolved in {(end - start)/10**9:0.3f} seconds.")
        start = time.perf_counter_ns()
        solution = run(
            getattr(module, part), f"./{args.year}/input/day_{args.day:02}.txt"
        )
        end = time.perf_counter_ns()
        print(f"  Real:\t{solution}\tSolved in {(end - start)/10**9:0.3f} seconds.")
