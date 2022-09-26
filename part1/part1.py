def calculate(min, max, step):
	result = 0
	# range(起始值,結束值,遞增(減)值)
	for i in range(min, max+1, step):
		result += i

	print(result)

calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3,最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8,最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1,最後印出 0