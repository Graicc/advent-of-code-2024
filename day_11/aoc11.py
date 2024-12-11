import functools

with open('day_11/data.txt', 'r') as f:
	data = list(map(int, f.read().split()))

@functools.cache # functools.cache my beloved
def num_stone(stone: int, blink_left: int):
	if blink_left == 0:
		return 1

	if stone == 0:
		return num_stone(1, blink_left - 1)
	
	str_stone = str(stone)

	if len(str_stone) % 2 == 0:
		mid = len(str_stone) // 2
		return num_stone(int(str_stone[:mid]), blink_left-1) + num_stone(int(str_stone[mid:]), blink_left-1)
	else:
		return num_stone(stone * 2024, blink_left-1)

	pass

print(sum([num_stone(stone, 25) for stone in data]))
print(sum([num_stone(stone, 75) for stone in data]))