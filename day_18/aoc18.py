from typing import Set, Dict, List, Tuple
from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])


def add(a: Point, b: Point) -> Point:
    return Point(a.x + b.x, a.y + b.y)


def times(a: Point, scaler: int) -> Point:
    return Point(a.x * scaler, a.y * scaler)


with open("day_18/input.txt", "r") as f:
    data = [map(int, line.split(",")) for line in f.readlines()]

# size = 6
size = 70
# sim = 12
sim = 1024

data = set([Point(x, y) for x, y in data[:sim]])

seen: Set[Point] = set()
boundary = set()
boundary.add(Point(0, 0))

end = Point(size, size)

count = 1
while len(boundary) > 0:
    print(len(seen), len(boundary))
    # print(boundry)
    next_boundary = set()

    for point in boundary:
        seen.add(point)

    found = False
    for point in boundary:
        for neighbor in [
            add(point, Point(0, 1)),
            add(point, Point(1, 0)),
            add(point, Point(0, -1)),
            add(point, Point(-1, 0)),
        ]:
            if (
                neighbor.x < 0
                or neighbor.y < 0
                or neighbor.x > size
                or neighbor.y > size
            ):
                continue

            if neighbor == end:
                found = True

            if neighbor not in data and neighbor not in seen:
                next_boundary.add(neighbor)

    if found:
        break

    boundary = next_boundary
    count += 1

for y in range(size + 1):
    for x in range(size + 1):
        if Point(x, y) in seen:
            print("O", end="")
        if Point(x, y) in data:
            print("#", end="")
    print()

print(count)
