num1=int(input("enter first num"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
if ((num1>num2) & (num1>num3)):
    print("highest element=",num1)
elif((num2>num1) & (num2>num3)):
    print("highest element=",num2)
elif((num3>num1) & (num3>num2)):
    print("highest element=",num3)
else:
    print("equal numbers")