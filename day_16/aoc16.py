from typing import Dict, List, Tuple
from collections import namedtuple
import heapq


# ud = up-down or left-right layer
Point = namedtuple("Point", ["x", "y"])
UDPoint = namedtuple("Point", ["x", "y", "ud"])


def add(a: Point, b: Point) -> Point:
    return Point(a.x + b.x, a.y + b.y)


def times(a: Point, scaler: int) -> Point:
    return Point(a.x * scaler, a.y * scaler)


size = 141

walls = set()

start: UDPoint
end: Point
with open("day_16/input.txt", "r") as f:
    for y, line in enumerate(f.readlines()):
        for x, c in enumerate(line.strip()):
            if c == "#":
                walls.add(Point(x, y))
            elif c == "S":
                start = UDPoint(x, y, False)
            elif c == "E":
                end = Point(x, y)

Cell = namedtuple("Cell", ["cost", "parents"])
NCell = namedtuple("NCell", ["position", "parent"])

seen: Dict[UDPoint, Cell] = {}

neighbors: List[Tuple[int, NCell]] = []
heapq.heappush(
    neighbors,
    (
        0,
        NCell(start, None),
    ),
)

while len(neighbors) > 0:
    cost, (position, parent) = heapq.heappop(neighbors)
    if position in seen:
        if cost == seen[position].cost:
            seen[position].parents.append(parent)
        continue

    seen[position] = Cell(cost, [parent] if parent is not None else [])

    if position.ud:
        next_positions = [
            UDPoint(position.x, position.y + 1, position.ud),
            UDPoint(position.x, position.y - 1, position.ud),
        ]
    else:
        next_positions = [
            UDPoint(position.x + 1, position.y, position.ud),
            UDPoint(position.x - 1, position.y, position.ud),
        ]
    next_positions.append(UDPoint(position.x, position.y, not position.ud))

    for next_pos in next_positions:
        if Point(next_pos.x, next_pos.y) in walls:
            continue

        edge_weight = 1
        if position.ud != next_pos.ud:
            edge_weight = 1000
        heapq.heappush(neighbors, (cost + edge_weight, NCell(next_pos, position)))

ends = [UDPoint(end.x, end.y, False), UDPoint(end.x, end.y, True)]
print(min([seen[end].cost for end in ends]))

bt = set()
bt_nexts = set(ends)

while len(bt_nexts) > 0:
    for item in bt_nexts:
        if item == start:
            found = True
        bt.add(item)

    neighbors = set()

    for item in bt_nexts:
        cell = seen[item]
        for i in cell.parents:
            neighbors.add(i)

    bt_nexts = neighbors


print(len(set([(x, y) for x, y, _ in bt])))
