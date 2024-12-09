from typing import List
from collections import namedtuple

Segment = namedtuple('Segment', 'id start l')

isSpace = False
id = 0

# part 1
data: List[int] = []
# part 2
# This would probably be faster if it was a linked list, since we do a lot of insertions in the middle
segments: List[Segment] = []

first_idx = 0
with open('day_9/data.txt', 'r') as f:
	for c in f.read():
		c = int(c)
		if isSpace:
			segments.append(Segment(-1, len(data), c))
			for i in range(c):
				data.append(-1)
		else:
			segments.append(Segment(id, len(data), c))
			for i in range(c):
				data.append(id)
			id += 1

		isSpace = not isSpace

def first_free():
	global first_idx
	for i in range(first_idx, len(data)):
		if data[i] == -1:
			first_idx = i
			return i

for i in range(len(data)-1,0,-1):
	if data[i] == -1:
		continue

	free = first_free()

	if free > i:
		break

	val = data[i]
	data[i] = -1
	data[free] = val


total = 0
for i,v in enumerate(data):
	if v != -1:
		total += i*v

print(total)

# Part 2

def first_free(l):
	for i,segment in enumerate(segments):
		if segment.id == -1 and segment.l >= l:
			return i,segment

for segment in reversed(segments):
	if segment.id == -1:
		continue
	i,free = first_free(segment.l)

	if i is None or free.start > segment.start:
		continue

	segments.remove(segment)
	segments[i] = Segment(segment.id, free.start, segment.l)
	if free.l > segment.l:
		segments.insert(i + 1, Segment(-1, free.start + segment.l, free.l - segment.l))

	pass

total = 0
for seg in segments:
	if seg.id == -1:
		continue
	for i in range(seg.start, seg.start + seg.l):
		total += i * seg.id

print(total)