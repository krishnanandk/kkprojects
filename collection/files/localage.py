f= open("D:/Users/user/Downloads/customer","r")
age={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    if data[-1] not in age:
       age[data[3]] =1
    else:
        age[data[3]] +=1
print(age)