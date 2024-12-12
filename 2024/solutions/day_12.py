import io
from collections import defaultdict
from typing import Any


class UnionFind:
    # See https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    def __init__(self, grid):
        self.n_components = len(grid)
        self.id = {k: k for k in grid}
        self.size = {k: 1 for k in grid}

        for loc in grid:
            for d in (1, -1, 1j, -1j):
                if grid.get(nbr := loc + d) == grid[loc]:
                    self.unify(loc, nbr)

    def find(self, loc):
        root = loc
        while root != self.id[root]:
            root = self.id[root]

        # path compression
        while loc != root:
            next_ = self.id[loc]
            self.id[loc] = root
            loc = next_

        return root

    def component_size(self, loc):
        return self.size[self.find(loc)]

    def unify(self, loc1, loc2):
        root1 = self.find(loc1)
        root2 = self.find(loc2)

        if root1 != root2:
            if self.size[root1] < self.size[root2]:
                self.size[root2] += self.size[root1]
                self.id[root1] = root2
            else:
                self.size[root1] += self.size[root2]
                self.id[root2] = root1

            self.n_components -= 1

    def __iter__(self):
        components = defaultdict(set)
        for loc in self.id:
            components[self.find(loc)].add(loc)

        return iter(components.values())


def area(region):
    return len(region)


def perimeter(region):
    return sum(sum(loc + d not in region for d in (1, -1, 1j, -1j)) for loc in region)


def part_1(input_file: io.TextIOWrapper) -> Any:
    grid = {
        i + j * 1j: c for i, r in enumerate(input_file) for j, c in enumerate(r.strip())
    }

    regions = UnionFind(grid)

    return sum(area(component) * perimeter(component) for component in regions)


def n_sides(region):
    visited = set()
    count = 0

    for loc in region:
        for d in (1, -1, 1j, -1j):
            if (loc, d) in visited:
                continue
            visited.add((loc, d))

            if loc + d not in region:
                count += 1

                nbr = loc + d * 1j
                while nbr in region and nbr + d not in region:
                    visited.add((nbr, d))
                    nbr += d * 1j

                nbr = loc - d * 1j
                while nbr in region and nbr + d not in region:
                    visited.add((nbr, d))
                    nbr -= d * 1j
    return count


def part_2(input_file: io.TextIOWrapper) -> Any:
    grid = {
        i + j * 1j: c for i, r in enumerate(input_file) for j, c in enumerate(r.strip())
    }

    regions = UnionFind(grid)

    return sum(area(component) * n_sides(component) for component in regions)
