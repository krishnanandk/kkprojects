import re
lst=[]
x="[+][9][1]\d{10}"
f=open("phnno","r")
for lines in f:
    match=re.fullmatch(x,lines.rstrip("\n"))
    if match is not None:
        lst.append(lines.rstrip("\n"))
print(lst)