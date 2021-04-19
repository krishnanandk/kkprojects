import re

# n= "helloo"
# x="\w{6}"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


n= "56kg"
x= "\d{2}[a-z]{2}"                    #"\w{4}"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")