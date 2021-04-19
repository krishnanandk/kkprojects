import re


# x = "a{1,3}" #min 2a & max 3a
# r="aaa abc aaaa cga"
# matcher = re.finditer(x,r)
# for match in matcher:
#    print("match available at", match.start())
#    print("group", match.group())


# x = "^a" #check starting with a
# r="aaa abc aaaa cga"
# matcher = re.finditer(x,r)
# for match in matcher:
#    print("match available at", match.start())
#    print("group", match.group())


x = "a$" #check ending with a
r="aaa abc aaaa cga"
matcher = re.finditer(x,r)
for match in matcher:
   print("match available at", match.start())
   print("group", match.group())