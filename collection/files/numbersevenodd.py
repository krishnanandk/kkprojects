f = open("C:/Users/user/PycharmProjects/febpython/collection/files/numbers", "r")
odd=[]
even=[]
for num in f:
    if int(num) % 2==0:
       even.append(int(num.rstrip("\n")))
    else:
       odd.append(int(num.rstrip("\n")))
print(even)
print(sum(even))
print(odd)
print(sum(odd))
