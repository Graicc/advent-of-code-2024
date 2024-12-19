import functools

with open("day_19/input.txt", "r") as f:
    parts = f.read().split("\n\n")
    towels = parts[0].split(", ")
    targets = parts[1].strip().split("\n")


def can_make(target: str) -> bool:
    if len(target) == 0:
        return True

    for towel in towels:
        l = len(towel)
        if target.startswith(towel):
            if can_make(target[l:]):
                return True

    return False


print(len(list(filter(can_make, targets))))


@functools.cache
def num_ways(target: str) -> int:
    if len(target) == 0:
        return 1

    ways = 0
    for towel in towels:
        l = len(towel)
        if target.startswith(towel):
            ways += num_ways(target[l:])

    return ways


print(sum(map(num_ways, targets)))
