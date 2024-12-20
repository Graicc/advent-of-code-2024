from typing import Dict, List, Set, Tuple
import functools
from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])


def add(a: Point, b: Point) -> Point:
    return Point(a.x + b.x, a.y + b.y)


def times(a: Point, scaler: int) -> Point:
    return Point(a.x * scaler, a.y * scaler)


DIRS = [Point(0, 1), Point(0, -1), Point(1, 0), Point(-1, 0)]


walls: Set[Point] = set()
start: Point
end: Point

with open("day_20/input.txt", "r") as f:
    for y, line in enumerate(f.readlines()):
        for x, c in enumerate(line.strip()):
            if c == "#":
                walls.add(Point(x, y))
            elif c == "S":
                start = Point(x, y)
            elif c == "E":
                end = Point(x, y)


def compute_distance_map(starting_point: Point) -> Dict[Point, int]:
    visited: Dict[Point, int] = {}

    neigbors: Set[Point] = set()
    neigbors.add(starting_point)

    current_distance = 0
    while len(neigbors) > 0:
        nexts = set()

        for cell in neigbors:
            visited[cell] = current_distance

        for cell in neigbors:
            for dir in DIRS:
                next = add(cell, dir)
                if next not in walls and next not in visited:
                    nexts.add(next)

        neigbors = nexts
        current_distance += 1

    return visited


map_start = compute_distance_map(start)
map_end = compute_distance_map(end)

non_cheating_distance = map_start[end]

count = 0
for cell, cost in map_start.items():
    for dir in DIRS:
        next = add(cell, times(dir, 2))
        end_cost = map_end.get(next, 1e9)
        total_cost = cost + end_cost + 2
        saved = non_cheating_distance - total_cost
        # if saved > 0:
        #     print(saved)
        if saved >= 100:
            count += 1


print(count)

count = 0

for cell, cost in map_start.items():
    for x in range(-20, 21):
        for y in range(-20, 21):
            cheat_len = abs(x) + abs(y)
            if cheat_len > 20:
                continue

            next = add(cell, Point(x, y))
            end_cost = map_end.get(next, 1e9)
            total_cost = cost + end_cost + cheat_len
            saved = non_cheating_distance - total_cost
            if saved >= 100:
                count += 1


print(count)
