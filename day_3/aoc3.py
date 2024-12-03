import bisect
import re
from functools import reduce

with open('day_3/data.txt', 'r') as f:
	print(sum([reduce(lambda l,r: l*r, map(int, match.groups())) for match in re.finditer("mul\(([0-9]{1,3}),([0-9]{1,3})\)", f.read())]))

def before(val: int, l: [int]):
	index = bisect.bisect_left(l, val)
	if index == 0:
		return 0
	
	return l[index-1]

with open('day_3/data.txt', 'r') as f:
	data = f.read()
	dos = [x.start() for x in re.finditer(r"do\(\)", data)]
	donts = [x.start() for x in re.finditer(r"don't\(\)", data)]
	muls = re.finditer("mul\(([0-9]{1,3}),([0-9]{1,3})\)", data)
	passed = filter(lambda x: before(x.start(), dos) >= before(x.start(), donts), muls)

	print(sum([reduce(lambda l,r: l*r, map(int, match.groups())) for match in passed]))
