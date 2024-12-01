lefts = []
rights = []

with open('data.txt', 'r') as f:
	lefts, rights = map(list, zip(*[map(int, line.split()) for line in f.readlines()]))

lefts.sort()
rights.sort()

diff = sum([abs(l - r) for l,r in zip(lefts,rights)])
print(diff)

from collections import Counter

rights_count = Counter(rights)

print(sum([x * rights_count[x] or 0 for x in lefts]))