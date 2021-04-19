employee=[[1001,"arun",15000],
         [1002,"arjun",20000],
         [1003, "kk", 25000],
         [1004,"vishnu",10000]]
print(employee)

#nested list

# for i in employee:
#     print(i)
#
# for i in employee:
#     print(i[1])

# for i in employee:
#     if(i[2]>17000):
#        print(i[1])
sum=0
for i in employee:
    sum=sum+i[2]
print(sum)