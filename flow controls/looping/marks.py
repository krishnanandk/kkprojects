sub1=int(input("mark of subject 1"))
sub2=int(input("mark of subject 2"))
sub3=int(input("mark of subject 3"))
sub4=int(input("mark of subject 4"))
totalmarks=(sub1+sub2+sub3+sub4)
percentage=((totalmarks/200)*100)
if(percentage>90):
    print("grade obtained= A+")
elif (80<percentage<89):
    print("grade obtained= A")
elif (70<percentage<79):
    print("grade obtained= B+")
elif (60<percentage<69):
    print("grade obtained= B")
elif (50<percentage<59):
    print("grade obtained= C+")
elif(40<percentage<49):
    print("grade obtained= C")

elif(30<percentage<39):
    print("grade obtained= D+")
else:
    print('failed')