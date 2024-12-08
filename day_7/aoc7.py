from typing import List

count_one = 0
count_two = 0

def canReachOne(target: int, nums: List[int], curr: int) -> bool:
	if len(nums) == 0:
		return target == curr

	if (sum(nums) + curr > target + len(nums)):  # len(nums) accounts for 1's
		return False

	next_nums = nums[1:]
	if canReachOne(target, next_nums, curr + nums[0]):
		return True
	elif canReachOne(target, next_nums, curr * nums[0]):
		return True
	
	return False

def canReachTwo(target: int, nums: List[int], curr: int) -> bool:
	if len(nums) == 0:
		return target == curr

	if (sum(nums) + curr > target + len(nums)):  # len(nums) accounts for 1's
		return False

	next_nums = nums[1:]
	if canReachTwo(target, next_nums, curr + nums[0]):
		return True
	elif canReachTwo(target, next_nums, curr * nums[0]):
		return True
	elif canReachTwo(target, next_nums, int(str(curr)+str(nums[0]))):
		return True
	
	return False

with open('day_7/data.txt', 'r') as f:
	for line in f.readlines():
		target, nums = line.split(":")
		target = int(target)
		nums = list(map(int, nums.split()))
		
		if canReachOne(target, nums[1:], nums[0]):
			count_one += target 
		if canReachTwo(target, nums[1:], nums[0]):
			count_two += target 

print(count_one)
print(count_two)