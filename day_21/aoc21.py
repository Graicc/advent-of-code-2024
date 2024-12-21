import functools
from collections import namedtuple
import itertools


Point = namedtuple("Point", ["x", "y"])


def add(a: Point, b: Point) -> Point:
    return Point(a.x + b.x, a.y + b.y)


with open("day_21/input.txt", "r") as f:
    targets = [l.strip() for l in f.readlines()]

numpad = {
    "0": Point(1, 3),
    "1": Point(0, 2),
    "2": Point(1, 2),
    "3": Point(2, 2),
    "4": Point(0, 1),
    "5": Point(1, 1),
    "6": Point(2, 1),
    "7": Point(0, 0),
    "8": Point(1, 0),
    "9": Point(2, 0),
    "A": Point(2, 3),
}

dirpad = {
    "^": Point(1, 0),
    "A": Point(2, 0),
    "<": Point(0, 1),
    "v": Point(1, 1),
    ">": Point(2, 1),
}

dir_to_key = {Point(1, 0): ">", Point(-1, 0): "<", Point(0, 1): "v", Point(0, -1): "^"}


def sign(x: int) -> int:
    if x > 0:
        return 1
    else:
        return -1


# Minimum number of presses with an A at the end
@functools.cache
def min_distance(start: Point, end: Point, layer: int, limit: int = 2) -> int:
    if start == end:
        return 1  # Press A

    dx = end.x - start.x
    dy = end.y - start.y

    if layer == limit:
        return abs(dx) + abs(dy) + 1

    forbidden = Point(0, 3) if layer == 0 else Point(0, 0)

    # Generate a naive walk
    walk = [Point(sign(dx), 0)] * abs(dx) + [Point(0, sign(dy))] * abs(dy)

    min_dist = float("inf")
    # There will be duplicate walks, but memoization on min_distance
    # makes it faster to do this than to ensure unique walks
    for walk in itertools.permutations(walk):
        dist = 0
        curr = dirpad["A"]

        curr_pos = start
        used_forbidden = False

        for move in walk:
            curr_pos = add(curr_pos, move)
            if curr_pos == forbidden:
                used_forbidden = True
                break

            dpad_pos = dirpad[dir_to_key[move]]
            dist += min_distance(curr, dpad_pos, layer + 1, limit)
            curr = dpad_pos
        dist += min_distance(curr, dirpad["A"], layer + 1, limit)

        if dist < min_dist and not used_forbidden:
            min_dist = dist

    # print(f"distance ({layer}) from {start} to {end} is {min_dist}")
    return min_dist


# Limits for each part
for limit in [2, 25]:
    total = 0
    for target in targets:
        total_dist = min_distance(numpad["A"], numpad[target[0]], 0, limit)
        for i in range(len(target) - 1):
            total_dist += min_distance(
                numpad[target[i]], numpad[target[i + 1]], 0, limit
            )

        v = int(target[:-1])
        # print(total_dist, v)
        total += total_dist * v

    print(total)
