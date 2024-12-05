from typing import Dict, List
from functools import cmp_to_key

with open('day_5/data.txt', 'r') as f:
	rules, updates = f.read().split("\n\n")

rules_list = [list(map(int, rule.split("|"))) for rule in rules.split("\n")]

rules: Dict[int, List[int]] = {}

for rule in rules_list:
	l,r = rule
	if l in rules:
		rules[l].append(r)
	else:
		rules[l] = [ r ]

updates = [list(map(int, update.split(","))) for update in updates.split("\n")]

def cmp(l,r):
	if r in rules[l]: # R after L
		return -1
	elif l in rules[r]: # L after R
		return 1
	else:
		return 0

sum = 0
sum_2 = 0

for update in updates:
	good = True
	for i in range(len(update)):
		if not all([x not in update[:i] for x in rules.get(update[i], [])]):
			good = False
			break

	if good:
		mid = update[int(len(update)/2)]
		sum += mid
	else:
		# find correct ordering, p2
		update.sort(key=cmp_to_key(cmp))
		mid = update[int(len(update)/2)]
		sum_2 += mid
		pass

print(sum)
print(sum_2)