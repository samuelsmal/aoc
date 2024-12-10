import io
from collections import deque
from typing import Any


def part_1(input_file: io.TextIOWrapper) -> Any:
    input = input_file.read().strip()

    A = deque([])
    space = deque([])
    file_id = 0
    f_ids = []
    pos = 0

    for i, c in enumerate(input):
        if i % 2 == 0:
            for _ in range(int(c)):
                f_ids.append(file_id)
                A.append((pos, 1, file_id))
                pos += 1
            file_id += 1
        else:
            space.append((pos, int(c)))
            for _ in range(int(c)):
                f_ids.append(None)
                pos += 1

    for (pos, size, file_id) in reversed(A):
        for space_i, (space_pos, space_sz) in enumerate(space):
            if space_pos < pos and size <= space_sz:
                for i in range(size):
                    assert f_ids[pos + i] == file_id, f"{f_ids[pos+i]=}"
                    f_ids[pos + i] = None
                    f_ids[space_pos + i] = file_id
                space[space_i] = (space_pos + size, space_sz - size)
                break

    return sum(i * c for i, c in enumerate(f_ids) if c is not None)


def part_2(input_file: io.TextIOWrapper) -> Any:
    input = input_file.read().strip()

    A = deque([])
    space = deque([])
    file_id = 0
    f_ids = []
    pos = 0

    for i, c in enumerate(input):
        if i % 2 == 0:
            A.append((pos, int(c), file_id))
            for _ in range(int(c)):
                f_ids.append(file_id)
                pos += 1
            file_id += 1
        else:
            space.append((pos, int(c)))
            for _ in range(int(c)):
                f_ids.append(None)
                pos += 1

    for (pos, size, file_id) in reversed(A):
        for space_i, (space_pos, space_sz) in enumerate(space):
            if space_pos < pos and size <= space_sz:
                for i in range(size):
                    f_ids[pos + i] = None
                    f_ids[space_pos + i] = file_id
                space[space_i] = (space_pos + size, space_sz - size)
                break

    return sum(i * c for i, c in enumerate(f_ids) if c is not None)
