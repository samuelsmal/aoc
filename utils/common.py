def read_input(year, day, sample=False):
    with open(f"./{year}/input/day_{day}{'_sample' if sample else ''}.txt") as f:
        return [l.strip() for l in f]
