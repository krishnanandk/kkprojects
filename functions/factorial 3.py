def factorialN(num1):
    fact = 1
    if (num1 < 0):
        print("no factorial")
    elif (num1 == 0):
        print("factorial=1")
    else:
        for i in range(1, num1 + 1):
            fact = fact * i
    return fact
data=factorialN(5)
print(data)