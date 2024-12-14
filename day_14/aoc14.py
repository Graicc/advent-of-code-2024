import functools
from typing import List
from collections import namedtuple
import re
import copy
import tempfile
from PIL import Image
import os

Point = namedtuple('Point', ['x', 'y'])

def add(a: Point, b: Point) -> Point:
	return Point(a.x + b.x, a.y + b.y)

def times(a: Point, scaler: int) -> Point:
	return Point(a.x * scaler, a.y * scaler)

data: List[List[Point]] = []

with open('day_14/data.txt', 'r') as f:
	for line in f.readlines():
		px, py, vx, vy = map(int, re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups())
		data.append([Point(px,py), Point(vx, vy)])

# width = 11
# height = 7
width = 101
height = 103

quadrents = [0,0,0,0]

data2 = copy.deepcopy(data)

for robot in data:
	for i in range(100):
		next = add(robot[0], robot[1])
		robot[0] = Point(next.x % width, next.y % height)

	px = robot[0].x
	py = robot[0].y
	if px < width // 2 and py < height // 2:
		quadrents[0] += 1
	if px > width // 2 and py < height // 2:
		quadrents[1] += 1
	if px > width // 2 and py > height // 2:
		quadrents[2] += 1
	if px < width // 2 and py > height // 2:
		quadrents[3] += 1

print(functools.reduce(lambda x,y: x * y, quadrents))

dir = tempfile.TemporaryDirectory()

sizes = []

for i in range(10000):
	im = Image.new("RGBA", (width, height))
	for robot in data2:
		next = add(robot[0], robot[1])
		robot[0] = Point(next.x % width, next.y % height)
		im.putpixel((robot[0].x, robot[0].y), (255, 255, 255))
	
	im.save(f"{dir.name}/{i}.png")
	sizes.append(os.path.getsize(f"{dir.name}/{i}.png"))
print(sizes.index(min(sizes)) + 1)