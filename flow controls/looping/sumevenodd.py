lowerlimit=int(input("lower limit"))
upperlimit=int(input("upper limit"))
evensum=0
oddsum=0
for i in range (lowerlimit,upperlimit+1):
    if(i%2==0):
      evensum+=i
    else:
        oddsum+=i
print("odd sum=",oddsum)
print("even sum=",evensum)
