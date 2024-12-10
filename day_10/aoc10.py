from typing import Set
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

with open('day_10/data.txt', 'r') as f:
	data = [ list(map(int, line.strip())) for line in f.readlines()]

trailheads = [Point(x,y) for x,l in enumerate(data) for y,c in enumerate(l) if c == 0]

total = 0
for trailhead in trailheads:
	peaks: Set[Point] = set()
	curr = [trailhead]
	while len(curr) > 0:
		next = []
		for item in curr:
			val = data[item.x][item.y]
			for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
				nx = item.x + x
				ny = item.y + y
				if nx >= 0 and nx < len(data) and ny >= 0 and ny < len(data) and data[nx][ny] == val + 1:
					next.append(Point(nx,ny))
					if data[nx][ny] == 9:
						peaks.add(Point(nx,ny))

		curr = next

	total += len(peaks)

print(total)

total = 0
for trailhead in trailheads:
	def dfs(start: Point):
		val = data[start.x][start.y]
		for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
			nx = start.x + x
			ny = start.y + y
			if nx >= 0 and nx < len(data) and ny >= 0 and ny < len(data) and data[nx][ny] == val + 1:
				if data[nx][ny] == 9:
					global total
					total += 1
				else:
					dfs(Point(nx,ny))
		pass

	dfs(trailhead)

print(total)