from functools import reduce

lefts = []
rights = []

with open('day_2/data.txt', 'r') as f:
	diffs = [[int(a)-int(b) for a,b in zip(line.split(), line.split()[1:])] for line in f.readlines()]

print(len(list(filter(lambda line: all([abs(x) >= 1 and abs(x) <= 3 for x in line]) and (all([x > 0 for x in line]) or all([x < 0 for x in line])), diffs))))

count = 0
for line in diffs:
	options = [ line[:i-1] + [line[i-1] + line[i]] + line[i+1:] for i in range(1,len(line)) ] + [line[:-1]] + [line[1:]]
	if any([all([abs(x) >= 1 and abs(x) <= 3 for x in line]) and (all([x > 0 for x in line]) or all([x < 0 for x in line])) for line in options]):
		count += 1
print(count)
		
# Same thing
# print(len(list(filter(lambda line: any([all([abs(x) >= 1 and abs(x) <= 3 for x in line]) and (all([x > 0 for x in line]) or all([x < 0 for x in line])) for line in [ line[:i-1] + [line[i-1] + line[i]] + line[i+1:] for i in range(1,len(line)) ] + [line[:-1]] + [line[1:]]]), [[int(a)-int(b) for a,b in zip(line.split(), line.split()[1:])] for line in f.readlines()]))))