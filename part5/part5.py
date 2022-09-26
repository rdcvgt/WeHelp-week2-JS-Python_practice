def twoSum(nums, target):
	for i in nums:
		for j in nums:
			iIndex =nums.index(i)
			jIndex =nums.index(j)
			if (i+j == target and iIndex !=jIndex):
				return [iIndex, jIndex]




result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9