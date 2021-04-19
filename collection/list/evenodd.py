lst=[]
oddlst=[]
evenlst=[]
for i in range (50,201):
     lst.append(i)

for i in lst:
    if(i%2==0):
      evenlst.append(i)
    else:
      oddlst.append(i)
print(lst)
print(oddlst)
print(evenlst)



