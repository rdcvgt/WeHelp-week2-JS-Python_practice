def maxProduct(nums):
	max = -float("inf");
	for i in nums:
		for j in nums:
			iIndex = nums.index(i)
			jIndex = nums.index(j)
			if (i*j >max and iIndex != jIndex):
				
				max = i*j

	print(max)


maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10