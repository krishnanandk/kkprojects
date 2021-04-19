f= open("D:/Users/user/Downloads/customer","r")
location={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    if data[-1] not in location:
       location[data[-1]] =1
    else:
        location[data[-1]] +=1
print(location)