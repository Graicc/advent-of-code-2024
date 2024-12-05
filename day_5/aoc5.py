from typing import Dict, List
from functools import cmp_to_key

with open('day_5/data.txt', 'r') as f:
	rules, updates = f.read().split("\n\n")

rules = [list(map(int, rule.split("|"))) for rule in rules.split("\n")]
updates = [list(map(int, update.split(","))) for update in updates.split("\n")]

def cmp(l,r):
	return -1 if [l,r] in rules else 1 if [r,l] in rules else 0

sum = 0
sum_2 = 0

for update in updates:
	if all([([update[i], x] not in rules) for i in range(len(update)) for x in update[:i]]):
		mid = update[int(len(update)/2)]
		sum += mid
	else:
		update.sort(key=cmp_to_key(cmp))
		mid = update[int(len(update)/2)]
		sum_2 += mid
		pass

print(sum)
print(sum_2)