# taking the idea from others to use complex numbers to store position and direction!
# blew my mind when I saw it, so I had to redo it again...
import io


def walk(grid, start, part=1):
    pos, dir = start, -1
    seen = set()

    while pos in grid and (pos, dir) not in seen:
        seen |= {(pos, dir)}
        if grid.get(pos + dir) == "#":
            dir *= -1j
        else:
            pos += dir

    if part:
        return (pos, dir) in seen
    else:
        return {pos for pos, _ in seen}


def part_1(input_file: io.TextIOWrapper) -> int:
    grid = {
        i + j * 1j: c for i, r in enumerate(input_file) for j, c in enumerate(r.strip())
    }

    start = min(p for p in grid if grid[p] == "^")
    path = walk(grid, start, 0)
    return len(path)


def part_2(input_file: io.TextIOWrapper) -> int:
    grid = {
        i + j * 1j: c for i, r in enumerate(input_file) for j, c in enumerate(r.strip())
    }

    start = min(p for p in grid if grid[p] == "^")

    path = walk(grid, start, 0)

    # brute force! just place an obstacle at every position in the taken path and see if that leads to a loop
    return sum(walk(grid | {o: "#"}, start) for o in path)
