f= open("C:/Users/user/PycharmProjects/febpython/collection/files/data","r")
dic={}
for lines in f:
    word = lines.rstrip("\n").split(" ")
    for i in word:
      if (i not in dic):
        dic[i] = 1
      else:
        dic[i] += 1
print(dic)