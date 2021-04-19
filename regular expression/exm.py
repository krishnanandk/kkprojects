import re
n= input("enter the data")
rule="(^a[a-zA-Z0-9\W]*b$)"
match=re.fullmatch(rule,n)
if match is not None:
    print("valid")
else:
    print("invalid")