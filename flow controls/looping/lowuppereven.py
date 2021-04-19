lowerlimit=int(input("lower limit"))
upperlimit=int(input("upper limit"))

for i in range (lowerlimit,upperlimit+1,1):
    if(i%2==0):
      print(i)
