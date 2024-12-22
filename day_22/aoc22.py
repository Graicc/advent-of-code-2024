import itertools
from collections import defaultdict


def mix(a, b):
    return a ^ b


def prune(a):
    return a % 16777216


def step(x: int) -> int:
    p1 = prune(mix(x, x * 64))
    p2 = prune(mix(p1, p1 // 32))
    return prune(mix(p2, p2 * 2048))


with open("day_22/input.txt", "r") as f:
    data = map(int, f.read().strip().split("\n"))

sum = 0

diffs = defaultdict(list)
vals = defaultdict(list)
for i, x in enumerate(data):
    init = x
    for _ in range(2000):
        n = step(x)
        diff = n % 10 - x % 10
        diffs[i].append(diff)
        vals[i].append(n % 10)
        x = n

    sum += x
print(sum)


import multiprocessing.pool

sequnece_val_map = defaultdict(dict)
for i, diff in diffs.items():
    val = vals[i]
    for j in range(len(diff) - 3):
        key = (diff[j], diff[j + 1], diff[j + 2], diff[j + 3])
        if key not in sequnece_val_map[i]:
            v = val[j + 3]
            sequnece_val_map[i][key] = v


m = 0
for a, b, c, d in itertools.product(
    range(-9, 9), range(-9, 9), range(-9, 9), range(-9, 9)
):
    sum = 0
    for i, x in sequnece_val_map.items():
        sum += x.get((a, b, c, d), 0)
    if sum > m:
        m = sum

print(m)
