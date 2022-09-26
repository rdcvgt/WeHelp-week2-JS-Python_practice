def maxZeros(nums):
	max =0
	sum =0
	for i in nums:
		if (i == 0):
			sum +=1
		if (sum>max):
			max =sum
		if (i == 1):
			sum =0
	print(max)




maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3