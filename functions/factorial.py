def factorial():
    fact=1
    num1=int(input("enter number1"))
    if(num1<0):
        print("no factorial")
    elif(num1==0):
        print("factorial=1")
    else:
        for i in range (1,num1+1):
            fact=fact*i
        print(fact)
factorial()