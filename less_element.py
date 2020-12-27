nums = [2, 3, 1, 9]
result = nums[0]
for x in nums:
	if x < result:
		result = x

print(result)