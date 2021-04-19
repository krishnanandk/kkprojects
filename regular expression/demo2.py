# import re
#
# x="[abc]"   #either a,b or c
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#     print("match available at",match.start())
#     print("group",match.group())


# import re
#
# x="[^abc]"   #except a,b or c
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#     print("match available at",match.start())
#     print("group",match.group())

# import re
#
# x = "[a-z]"  # a-z small letters
# matcher = re.finditer(x, "Abt c@5kz")
# for match in matcher:
#    print("match available at", match.start())
#    print("group", match.group())


# import re
#
# x = "[A-Z]"  # A-Z capital letters
# matcher = re.finditer(x, "Abt c@5kz")
# for match in matcher:
#    print("match available at", match.start())
#    print("group", match.group())



# import re
#
# x = "\s"  # space
# matcher = re.finditer(x, "Abt c@5kz")
# for match in matcher:
#    print("match available at", match.start())
#    print("group", match.group())


# import re
#
# x = "\d"  # digits
# matcher = re.finditer(x, "Abt c@5kz")
# for match in matcher:
#    print("match available at", match.start())
#    print("group", match.group())


import re

x = "\w"  # words
matcher = re.finditer(x, "Abt c@5kz")
for match in matcher:
   print("match available at", match.start())
   print("group", match.group()



# x='[abc]' either a b or c
# x='[^abc]' except abc
# x='[a-z]' a to z
# x='[A-Z]' A to Z
# x='[a-zA-Z]' both lower and upper case are checked
# x='[0-9]' check digits
# x='[^a-zA-Z0-9]' special symbols
# x='\s' check space
# x='\d' check the digits
# x='\D' except digits
# x='\w' all words except special characters
# x='\W' for special characters



