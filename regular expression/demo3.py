#quantifiers

# quantifiers
# x='a+'  a including group
# x='a*' count including zero number of a
# x='a?' count a as each including zero no of a
# x='a{2}' 2 no of a position
# x='a{2,3}' minimum 2 a and maximum 3 a
# x='^a'  check starting with a
# x='a$' check ending with a


import re

# x = "a+" #group of a
# r="aaa abc aaaa cga"
# matcher = re.finditer(x,r)
# for match in matcher:
#    print("match available at", match.start())
#    print("group", match.group())

# x = "a*" #count includiing zero number of a
# r="aaa abc aaaa cga"
# matcher = re.finditer(x,r)
# for match in matcher:
#    print("match available at", match.start())
#    print("group", match.group())

# x = "a?" #count as each includiing zero number of a
# r="aaa abc aaaa cga"
# matcher = re.finditer(x,r)
# for match in matcher:
#    print("match available at", match.start())
#    print("group", match.group())

x = "a{3}" #number of position
r="aaa abc aaaa cga"
matcher = re.finditer(x,r)
for match in matcher:
   print("match available at", match.start())
   print("group", match.group())




