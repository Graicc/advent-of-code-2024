from typing import Set
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

with open('day_12/data.txt', 'r') as f:
	data = [line.strip() for line in f.readlines()]

visited: Set[Point] = set()

total = 0

def compute_value(point: Point):
	type = data[point.x][point.y]

	seen: Set[Point] = set()
	curr = set()
	curr.add(point)
	
	perimeter = 0

	while len(curr) > 0:
		for x in curr:
			seen.add(x)

		next = set()

		for item in curr:
			for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
				nx = item.x + x
				ny = item.y + y
			
				p = Point(nx,ny)

				if p not in seen:
					if nx >= 0 and nx < len(data) and ny >= 0 and ny < len(data) and data[nx][ny] == type:
						next.add(p)
					else: 
						perimeter += 1


		curr = next

	area = len(seen)
	# print(type, area, perimeter)
	return area * perimeter, seen

for x in range(len(data)):
	for y in range(len(data)):
		point = Point(x,y)
		if point in visited:
			continue

		value, news = compute_value(point)
		for j in news:
			visited.add(j)
		# print(data[x][y], value)
		total += value


print(total)
		
visited: Set[Point] = set()

total = 0

def compute_value(point: Point):
	type = data[point.x][point.y]

	seen: Set[Point] = set()
	curr = set()
	curr.add(point)
	
	perimeter = 0

	while len(curr) > 0:
		for x in curr:
			seen.add(x)

		next = set()

		for item in curr:
			for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
				nx = item.x + x
				ny = item.y + y
			
				p = Point(nx,ny)

				if p not in seen:
					if nx >= 0 and nx < len(data) and ny >= 0 and ny < len(data) and data[nx][ny] == type:
						next.add(p)
					else: 
						perimeter += 1


		curr = next

	area = len(seen)
	# print(type, area, perimeter)

	sides = 0

	for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
		seen_side = set()
		for i in range(len(data)):
			for j in range(len(data)):
				p =Point(i,j)
				if p in seen:
					offset = Point(p.x + x, p.y + y)
					if offset.x >= 0 and offset.x < len(data) and offset.y >= 0 and offset.y < len(data) and data[offset.x][offset.y] == type:
						pass
					else:
						if Point(offset.x - y, offset.y - x) not in seen_side and Point(offset.x + y, offset.y + x) not in seen_side:
							sides += 1
						seen_side.add(offset)

	# 	print(type, " for side ", sides)

	# print(type, area, sides)

	return area * sides, seen

for x in range(len(data)):
	for y in range(len(data)):
		point = Point(x,y)
		if point in visited:
			continue

		value, news = compute_value(point)
		for j in news:
			visited.add(j)
		# print(data[x][y], value)
		total += value


print(total)