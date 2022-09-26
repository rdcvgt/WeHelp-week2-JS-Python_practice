function avg(data){
	let list = data.employees
	let sum = 0
	let people =0
	for (let i =0; i<list.length; i++){
		
		if (list[i].manager === false){
			sum += list[i].salary
			people++
		}
	}
	console.log(sum/people)

}
avg({
"employees":[
{
"name":"John",
"salary":30000,
"manager":false
},
{
"name":"Bob",
"salary":60000,
"manager":true
},
{
"name":"Jenny",
"salary":50000,
"manager":false
},
{
"name":"Tony",
"salary":40000,
"manager":false
}
]
}); // 呼叫 avg 函式