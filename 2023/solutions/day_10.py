from collections import deque


def neighbors(grid, x, y):
    neighbors_ = []
    # To the north
    if 1 <= y and grid[y - 1][x] in ["|", "7", "F"]:
        neighbors_.append((x, y - 1))
    # To the west
    if 1 <= x and grid[y][x - 1] in ["-", "L", "F"]:
        neighbors_.append((x - 1, y))
    # To the south
    if y < len(grid) - 1 and grid[y + 1][x] in ["|", "L", "J"]:
        neighbors_.append((x, y + 1))
    # To the east
    if x < len(grid[0]) - 1 and grid[y][x + 1] in ["-", "7", "J"]:
        neighbors_.append((x + 1, y))

    return neighbors_


def find_start(grid, start_symbol="S"):
    for y, line in enumerate(grid):
        for x, symbol in enumerate(line):
            if symbol == start_symbol:
                return (x, y)


def part_1(input_file):
    grid = [l.strip() for l in input_file]

    queue = deque(
        [
            find_start(grid),
        ]
    )

    distances = {queue[0]: 0}

    while queue:
        current = queue.popleft()
        for n in neighbors(grid, *current):
            if n not in distances:
                queue.append(n)
                distances[n] = distances[current] + 1

    # for y in range(len(grid)):
    #     for x in range(len(grid[0])):
    #         if (x, y) in distances:
    #             print(distances[(x, y)], end="")
    #         else:
    #             print(".", end="")
    #     print("\n", end="")

    return max(distances.values())


# The `#` basically symbolises a part of the pipeline. It blocks... Don't ask.

EXPANDS = {
    "|": [".#.", ".#.", ".#."],
    "-": ["...", "###", "..."],
    "L": [".#.", ".##", "..."],
    "J": [".#.", "##.", "..."],
    "7": ["...", "##.", ".#."],
    ".": ["...", "...", "..."],
    "F": ["...", ".##", ".#."],
    "S": ["###", "###", "###"],
}


class Pos(tuple):
    def __add__(self, other):
        return Pos(x + y for x, y in zip(self, other))

    def __neg__(self):
        return Pos(-x for x in self)

    def __mul__(self, other):
        if isinstance(other, int):
            return Pos(x * other for x in self)
        else:
            raise NotImplementedError("like... yeah")


#
# Screw it... switching to memory-layout coordinates
#
SYMBOLS_TO_NEIGHBORS = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(0, 1), (-1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, -1), (1, 0)],
    "F": [(0, 1), (1, 0)],
    "S": [(1, 0), (0, 1), (-1, 0), (0, -1)],
    ".": [],
}
SYMBOLS_TO_NEIGHBORS = {k: [Pos(x) for x in v] for k, v in SYMBOLS_TO_NEIGHBORS.items()}
TOUTES_DIRECTIONS = [
    Pos((1, 0)),
    Pos((0, 1)),
    Pos((-1, 0)),
    Pos((0, -1)),
]


def part_2(input_file):
    grid = {Pos((y, x)): t for y, l in enumerate(input_file) for x, t in enumerate(l)}
    start = next(pos for pos, x in grid.items() if x == "S")

    queue = deque([(start, 0)])
    distances = {}

    while queue:
        pos, dist = queue.popleft()

        if pos in grid and pos not in distances:
            distances[pos] = dist
            for n in SYMBOLS_TO_NEIGHBORS[grid[pos]]:
                queue.append((pos + n, dist + 1))

    expanded = {
        pos * 3 + (i, j): EXPANDS[t][i][j] if pos in distances else EXPANDS["."][i][j]
        for pos, t in grid.items()
        for i in range(3)
        for j in range(3)
    }

    queue = deque([(0, 0)])
    visited = set()

    while queue:
        pos, dist = queue.popleft()

        if pos in expanded and pos not in visited and expanded != "#":
            visited.add(pos)
            for n in TOUTES_DIRECTIONS:
                queue.append(pos + n)

    return sum(
        all(pos * 3 + (i, j) not in visited for i in range(3) for j in range(3))
        for pos in grid.keys()
    )
