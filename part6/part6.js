function maxZeros(nums){
	let max = 0
	let sum =0
	for (let i=0; i<nums.length; i++){
		if  (nums[i]===0){
			sum++
		}
		if (sum>max){
			max = sum
		}
		if (nums[i]===1){
			sum = 0
		}
	}
	console.log(max)
}

maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
maxZeros([1, 1, 1, 1, 1]); // 得到 0
maxZeros([0, 0, 0, 1, 1]) // 得到 3