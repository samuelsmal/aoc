import re


def extract_digits(line):
    found_digits = re.findall(r"\d", line)
    return int(found_digits[0]) * 10 + int(found_digits[-1])


digits = {
    "zero": 1,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def part_1(input_file):
    lines = [l.strip() for l in input_file]
    return sum(extract_digits(l) for l in lines)


def part_2(input_file):
    def problem_2_to_problem_1(s):
        # By surrounding the digits with the original words we avoid any overlap with the characters.
        for k, v in digits.items():
            s = s.replace(k, f"{k}{v}{k}")
        return s

    lines = [l.strip() for l in input_file]
    return sum(extract_digits(problem_2_to_problem_1(l)) for l in lines)
