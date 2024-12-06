with open('day_4/data.txt', 'r') as f:
	data = f.readlines()

count = 0
for row in range(0,len(data)):
	for col in range(0,len(data[row])):

		if (data[row][col] != 'X'):
			continue
		
		for dir_x in range(-1,2):
			for dir_y in range(-1,2):
				def has_in_dir(letter: str, r: int) -> bool:
					x = row + (dir_x * r)
					y = col + (dir_y * r)
					if x < 0 or y < 0:
						# Otherwise, this will wrap around the array!
						return False
					try:
						return data[x][y] == letter
					except IndexError:
						return False

				if has_in_dir("M", 1) and has_in_dir("A", 2) and has_in_dir("S",3):
					count += 1

print(count)

count = 0
for row in range(0,len(data)):
	for col in range(0,len(data[row])):
		if (data[row][col] != 'M'):
			continue
		
		# Only diagonals count!!!!
		for dir_x in (-1,1):
			for dir_y in (-1,1):
				def has_in_dir(letter: str, r: int) -> bool:
					x = row + (dir_x * r)
					y = col + (dir_y * r)
					if x < 0 or y < 0:
						# Otherwise, this will wrap around the array!
						return False
					try:
						return data[x][y] == letter
					except IndexError:
						return False

				if has_in_dir("A", 1) and has_in_dir("S", 2):
					# Avoid double counting by only doing the one 
					def has_in_dir_2(letter: str, r: int) -> bool:
						# dir_x, dir_y = -dir_y, dir_x
						dir_x_new = -dir_y
						dir_y_new = dir_x
						x = (row + dir_x - dir_x_new) + (dir_x_new * r) 
						y = (col + dir_y - dir_y_new) + (dir_y_new * r)
						if x < 0 or y < 0:
							# Otherwise, this will wrap around the array!
							return False
						try:
							return data[x][y] == letter
						except IndexError:
							return False

					if has_in_dir_2("M", 0) and has_in_dir_2("S", 2):
						count += 1

print(count)