from typing import Set, Tuple, List
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Tri = namedtuple('Tri', ['a', 'b', 'target'])

def add(a: Point, b: Point) -> Point:
	return Point(a.x + b.x, a.y + b.y)

def times(a: Point, scaler: int) -> Point:
	return Point(a.x * scaler, a.y * scaler)

import numpy as np
def solve(tri: Tri) -> Tuple[int,int]:
	target = [[tri.target.x],[tri.target.y]]
	A = [[tri.a.x * 3, tri.b.x],[tri.a.y * 3, tri.b.y]]
	A_inv = np.linalg.inv(A)
	res = np.linalg.matmul(A_inv, target)
	return res[0][0] * 3, res[1][0]

data: List[Tri] = []

def readline(line: str) -> Point:
	x = line.split("X+")
	x = int(x[1].split(",")[0])
	y = line.split("Y+")
	y  = int(y[1])
	return Point(x,y)

with open('day_13/data.txt', 'r') as f:
	parts = f.read().split("\n\n")
	for part in parts:
		lines = part.split("\n")
		a = readline(lines[0])
		b = readline(lines[1])

		target = lines[2]
		t_x = int(target.split("X=")[1].split(",")[0]) + 10000000000000
		t_y = int(target.split("Y=")[1]) + 10000000000000
		target = Point(t_x, t_y)

		data.append(Tri(a,b,target))


# print(data)

max = 101

# total = 0
# for tri in data:
# 	min = 1000
# 	for press_a in range(max):
# 		for press_b in range(max):
# 			if (add(times(tri.a, press_a), times(tri.b, press_b)) == tri.target):
# 				score = press_a  * 3 + press_b
# 				if score < min:
# 					min = score
	
# 	if min != 1000:
# 		total += min

# print(total)


total = 0
for tri in data:
	# solve(tri)
	a,b = solve(tri)
	print(a,b)
	if abs(round(a) - a) < 0.001 and abs(round(b) - b) < 0.001:
		print("good")
	# if int(b) == b:
		total += a * 3 + b 

print(total)