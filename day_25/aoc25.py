keys = []
locks = []

with open("day_25/input.txt", "r") as f:
    parts = f.read().strip().split("\n\n")
    for part in parts:
        lines = [l.strip() for l in part.split("\n")]

        is_lock = lines[0][0] == "#"

        counts = [0] * 5
        for col in range(5):
            for i in range(1, len(lines) - 1):
                if lines[i][col] == "#":
                    counts[col] += 1

        if is_lock:
            locks.append(counts)
        else:
            keys.append(counts)

count = 0
for lock in locks:
    for key in keys:
        if all([lock[i] + key[i] < 6 for i in range(5)]):
            count += 1

print(count)
