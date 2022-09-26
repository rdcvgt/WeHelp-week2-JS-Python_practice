#================================part1
def calculate(min, max, step):
	result = 0
	# range(起始值,結束值,遞增(減)值)
	for i in range(min, max+1, step):
		result += i

	print(result)

calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3,最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8,最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1,最後印出 0

#================================part2
def avg(data):
	eList = data["employees"]
	salarySum = 0
	people = 0

	for i in eList:
		if (i["manager"] == False):
			salarySum += i["salary"]
			people += 1

	print(salarySum/people)


avg({
"employees":[
{
"name":"John",
"salary":30000,
"manager":False
},
{
"name":"Bob",
"salary":60000,
"manager":True
},
{
"name":"Jenny",
"salary":50000,
"manager":False
},
{
"name":"Tony",
"salary":40000,
"manager":False
}
]
}) # 呼叫 avg 函式

#================================part3
def func(a):
    def others(y, z):
        print(a+y*z)
    return others




func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

#================================part4
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


#================================part5
def twoSum(nums, target):
	for i in nums:
		for j in nums:
			iIndex =nums.index(i)
			jIndex =nums.index(j)
			if (i+j == target and iIndex !=jIndex):
				return [iIndex, jIndex]




result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

#================================part6
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
