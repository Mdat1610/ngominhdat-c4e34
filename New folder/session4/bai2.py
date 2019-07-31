salary_table = [
{"name": "Duc",
"salary": 30,
"hour": 8,
"days": 20,
},

{"name":"Hoan",
"salary":50,
"hour":5,
"days":25,
},

{"name":"Dat",
"salary":40,
"hour": 7,
"days":30,
}
]
b = 0
for i in salary_table:
    n = i["salary"]*i["hour"]*i["days"]
    b = n + b
    print("Số lương của {0} là: {1}".format(i["name"],n))
print("Số Lương của cả 3 người là:",b)     


