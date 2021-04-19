f = open("C:/Users/user/PycharmProjects/febpython/collection/files/numbers", "r")
lst=[]
for number in f:
  lst.append(int(number.rstrip("\n"))) #int is used to convert it into number, otherwise it is read as string ad sum cannot be calculated.
print(lst)
print(sum(lst))

#\n nxt line
#to remove end character : rstrip function is used
#to remove first character lstrip is used