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