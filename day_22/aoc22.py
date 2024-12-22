from collections import defaultdict


def step(x: int) -> int:
    x ^= x * 64
    x %= 16777216
    x ^= x // 32
    x %= 16777216
    x ^= x * 2048
    x %= 16777216
    return x


with open("day_22/input.txt", "r") as f:
    data = map(int, f.read().strip().split("\n"))

p1 = 0

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

    p1 += x
print(p1)


score_map = defaultdict(int)
for i, diff in diffs.items():
    val = vals[i]
    seen = set()
    for j in range(len(diff) - 3):
        key = (diff[j], diff[j + 1], diff[j + 2], diff[j + 3])
        if key not in seen:
            seen.add(key)
            score_map[key] += val[j + 3]


print(max(score_map.values()))
