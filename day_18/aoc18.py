from typing import Set, Dict, List, Tuple
from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])


def add(a: Point, b: Point) -> Point:
    return Point(a.x + b.x, a.y + b.y)


with open("day_18/input.txt", "r") as f:
    all_data = [map(int, line.split(",")) for line in f.readlines()]
    all_data = [Point(x, y) for x, y in all_data]

# size = 6
size = 70


def distance(data) -> int:
    seen: Set[Point] = set()
    boundary = set()
    boundary.add(Point(0, 0))

    end = Point(size, size)

    count = 1
    found = False
    while len(boundary) > 0:
        next_boundary = set()

        for point in boundary:
            seen.add(point)

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
                    return count

                if neighbor not in data and neighbor not in seen:
                    next_boundary.add(neighbor)

        boundary = next_boundary
        count += 1

    return -1


print(distance(set(all_data[:1024])))

l = 0
u = len(all_data)
while u > l:
    sim = (u + l) // 2
    if distance(set(all_data[:sim])) != -1:
        l = sim + 1
    else:
        u = sim - 1

assert u == l
print(f"{all_data[u].x},{all_data[u].y}")
