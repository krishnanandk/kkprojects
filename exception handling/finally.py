lst=[10,4,5]
try:
    i=int(input("index"))
    print(lst[i])

except:
    print("exception occured")

finally:
    print("inside finally")