from typing import Dict, List, Set, Tuple

walls: Set[Tuple[int, int]] = set()

start: Tuple[int, int] = (0,0)
start_start: Tuple[int, int] = (0,0)
dir = (-1,0)

positions: Set[Tuple[int, int]] = set()

def move_in_dir(point: Tuple[int, int], dir: Tuple[int, int]) -> Tuple[int, int]:
	point_x, point_y = point
	dir_x, dir_y = dir
	return (point_x + dir_x, point_y + dir_y)

height = 0

with open('day_6/data.txt', 'r') as f:
	for i, row in enumerate(f.readlines()):
		width = len(row)
		height += 1
		for j, item in enumerate(row):
			if item == "#":
				walls.add((i,j))
			elif item == "^":
				start = (i,j)

start_start = start

while (start[0] >= 0 and start[0] < height and start[1] >= 0 and start[1] < width):
	positions.add(start)
	if move_in_dir(start, dir) in walls:
		dir = (dir[1], -dir[0])
	else:
		start = move_in_dir(start, dir)

print(len(positions))


total = 0

walls_walls = walls.copy()

for row in range(height):
	print("row")
	for col in range(width):
		walls = walls_walls.copy()
		walls.add((row, col))

		states: Set[Tuple[Tuple[int, int], Tuple[int, int]]] = set()
		start = start_start
		dir = (-1, 0)
		while (start[0] >= 0 and start[0] < height and start[1] >= 0 and start[1] < width):
			if (start, dir) in states:
				total += 1
				break
			states.add((start, dir))
			if move_in_dir(start, dir) in walls:
				dir = (dir[1], -dir[0])
			else:
				start = move_in_dir(start, dir)

print(total)