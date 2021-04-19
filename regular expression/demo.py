#pattern matching

#re_ package for pattern matching

# import re
#
# count=0
# matcher=re.finditer('ab','abaabbab')
# for match in matcher:
#     count+=1
# print("count=",count)
#.....................................................

#to get position and group

import re

count=0
matcher=re.finditer('ab','abaabbab')
for match in matcher:
    print("match available at",match.start()) #return position
    print("groups=",match.group())            #which object find match
    count+=1
print("count=",count)


