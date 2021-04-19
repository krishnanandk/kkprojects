lst=[10,20,21,33,35]
element=int(input("enter the number"))
flag=0
for i in lst:
        if (i==element):
            flag=1
            break
        else:
            pass
if(flag>0):
    print("element found")
else:
    print("element not foumd")

#linear search- complexity is high

#binary search