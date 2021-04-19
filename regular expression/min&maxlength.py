#min length8 and max length 15 (no nos:)

import re

data=input("enter the data:")
rule="^[A-Z][a-z]+$"
matcher=re.fullmatch(rule,data)
if matcher is not None:
    print("valid")
else:
    print("invalid")