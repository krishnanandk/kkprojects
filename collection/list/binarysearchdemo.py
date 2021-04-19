lst=[21,20,10,33,35]
lst.sort()
element=int(input("enter the element"))
low=0
up=len(lst)-1
flag=0
while(low<=up):
    mid=(low + up)//2

    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        up=mid-1
    elif(element==lst[mid]):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("element not found")
