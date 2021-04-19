employee={"id":1000,"name":"kk","designation":"developer","salary":10000}
print(employee["name"])
print("company"in employee)
employee["company"]="luminar"
employee["salary"]+=15000
print(employee)
for i in employee:
    print(i,":",employee[i])