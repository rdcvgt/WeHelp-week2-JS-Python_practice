function maxProduct(nums){
	let max = -Infinity

	for (let i =0; i<nums.length; i++){
		for (let j= i+1; j<nums.length; j++){
			if (nums[i]*nums[j]> max){
				max =nums[i]*nums[j]
			}
		}
	}
	console.log(max)
}
maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([10, -20, 0, -3]) // 得到 60
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0 或 -0
maxProduct([5, -1, -2, 0]) // 得到 2
maxProduct([-5, -2]) // 得到 10