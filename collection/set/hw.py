#6

#pairs

#(2,4)

#5

# (1,4),(2,3)

lst=[1,2,3,4,5,6]
lst1=[]
num=int(input("enter the number"))
flag=0
k=0
for i in lst:
    for j in lst:
        if i+j==num:
          lst1.extend([i,j])
          flag=1
          break
    if flag==1:
        break
print(lst1)
