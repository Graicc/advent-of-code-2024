from typing import Dict, List, Set, Tuple
from collections import defaultdict

nodes: Dict[str, List[Tuple[int, int]]] = defaultdict(list)

with open('day_8/data.txt', 'r') as f:
	for i,line in enumerate(f.readlines()):
		for j,c in enumerate(line):
			if c != "." and c != "\n":
				nodes[c].append((i,j))
		width = len(line) - 1

antinodes: Set[Tuple[int,int]] = set()

for _,ns in nodes.items():
	for l in ns:
		for r in ns:
			if l == r:
				continue

			x = 2 * r[0] - l[0]
			y = 2 * r[1] - l[1]

			antinodes.add((x,y))

print(len(list(filter(lambda x: x[0] >= 0 and x[0] < width and x[1] >= 0 and x[1] < width, antinodes))))

# part 2

antinodes: Set[Tuple[int,int]] = set()

for _,ns in nodes.items():
	for l in ns:
		for r in ns:
			if l == r:
				continue

			slope = (r[0]-l[0], r[1]-l[1])
			for i in range(-100,100):
				x = r[0] + i * slope[0]
				y = r[1] + i * slope[1]
				antinodes.add((x,y))

print(len(list(filter(lambda x: x[0] >= 0 and x[0] < width and x[1] >= 0 and x[1] < width, antinodes))))