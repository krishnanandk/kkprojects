def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

print("select operation\n"
      "1.Add\n"
      "2.Substract\n"
      "3.Multiply\n"
      "4.Division")
select=int(input("select operation"))
num1=int(input("enter number 1"))
num2=int(input("enter number 2"))

if select==1:
    print(num1,"+",num2,"=",add(num1,num2))
if select==2:
    print(num1,"-",num2,"=",sub(num1,num2))
if select==3:
    print(num1,"*",num2,"=",mul(num1,num2))
if select==4:
    print(num1,"/",num2,"=",div(num1,num2))