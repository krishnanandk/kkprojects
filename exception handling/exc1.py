# a=int(input("no1"))
# b=int(input("no2"))
# c=a/b
# print(c)

# no1=int(input("number1"))
# no2=int(input("number2"))
# try:
#     res=no1/no2
#     print("res=",res)
# except:
#     print("exception occured")


lst=[10,4,5]
try:
    i=int(input("index"))
    print(lst[i])
except Exception as e:
    print("exception occured")