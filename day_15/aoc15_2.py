from typing import Set
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])


def add(a: Point, b: Point) -> Point:
    return Point(a.x + b.x, a.y + b.y)


def times(a: Point, scaler: int) -> Point:
    return Point(a.x * scaler, a.y * scaler)


RIGHT = Point(1, 0)
LEFT = Point(-1, 0)

walls: Set[Point] = set()
blocks: Set[Point] = set()

with open("day_15/input.txt", "r") as f:
    parts = f.read().split("\n\n")
    moves = parts[1]
    for y, line in enumerate(parts[0].split("\n")):
        for x, c in enumerate(line.strip()):
            if c == "#":
                walls.add(Point(x * 2, y))
                walls.add(Point(x * 2 + 1, y))
            elif c == "O":
                blocks.add(Point(x * 2, y))
            elif c == "@":
                pos = Point(x * 2, y)


def can_push_block(pos: Point, dir: Point):
    if dir == Point(1, 0):
        possible_walls = [add(pos, times(dir, 2))]
        possible_blocks = [add(pos, times(dir, 2))]
    elif dir == Point(-1, 0):
        possible_walls = [add(pos, dir)]
        possible_blocks = [add(pos, times(dir, 2))]
    else:
        possible_walls = [add(pos, dir), add(pos, add(dir, RIGHT))]
        possible_blocks = [
            add(pos, add(dir, LEFT)),
            add(pos, dir),
            add(pos, add(dir, RIGHT)),
        ]

    return all([wall not in walls for wall in possible_walls]) and all(
        [block not in blocks or can_push_block(block, dir) for block in possible_blocks]
    )


def push_block(pos: Point, dir: Point):
    if pos not in blocks:
        return

    npos = add(pos, dir)

    if dir == Point(1, 0):
        possible_blocks = [add(pos, times(dir, 2))]
    elif dir == Point(-1, 0):
        possible_blocks = [add(pos, times(dir, 2))]
    else:
        possible_blocks = [
            add(pos, add(dir, LEFT)),
            add(pos, dir),
            add(pos, add(dir, RIGHT)),
        ]

    for block in possible_blocks:
        push_block(block, dir)

    blocks.remove(pos)
    blocks.add(npos)


for move in moves:
    match move:
        case "<":
            dir = Point(-1, 0)
        case ">":
            dir = Point(1, 0)
        case "v":
            dir = Point(0, 1)
        case "^":
            dir = Point(0, -1)
        case _:
            continue

    npos = add(pos, dir)
    if npos in walls:
        continue

    if dir.x == 0:
        possible_blocks = [
            add(pos, add(dir, LEFT)),
            add(pos, dir),
        ]
    elif dir.x == -1:
        possible_blocks = [add(pos, times(dir, 2))]
    else:
        possible_blocks = [add(pos, dir)]

    if all(
        [block not in blocks or can_push_block(block, dir) for block in possible_blocks]
    ):
        for block in possible_blocks:
            push_block(block, dir)

        pos = npos

print(sum([100 * block.y + block.x for block in blocks]))
