import io
from typing import Any


def part_1(input_file: io.TextIOWrapper) -> Any:
    grid = {
        i + j * 1j: int(c)
        for i, r in enumerate(input_file)
        for j, c in enumerate(r.strip())
    }

    def dfs(loc, height, visited):
        if loc in grid and height == grid[loc]:
            if height == 9 and loc not in visited:
                visited.add(loc)
                return 1
            return sum(
                dfs(loc + d, height + 1, visited)
                for d in (1, -1, 1j, -1j)
                if loc + d in grid
            )
        return 0

    return sum(dfs(loc, 0, set()) for loc in grid if grid[loc] == 0)


def part_2(input_file: io.TextIOWrapper) -> Any:
    grid = {
        i + j * 1j: int(c)
        for i, r in enumerate(input_file)
        for j, c in enumerate(r.strip())
    }

    def distinct(loc, height, visited):
        if loc in grid and height == grid[loc]:
            if height == 9:
                visited.add(loc)
                return 1
            return sum(
                distinct(loc + d, height + 1, visited)
                for d in (1, -1, 1j, -1j)
                if loc + d in grid
            )
        return 0

    return sum(distinct(loc, 0, set()) for loc in grid if grid[loc] == 0)
