#month
#day
#year

#dd
#mm
#year

#age
birthday=int(input("enter day of birth"))
birthmonth=int(input("enter month of birth"))
birthyear=int(input("enter year of birth"))

curday=int(input("enter current day"))
curmonth=int(input("enter current month"))
curyear=int(input("enter current year"))

age=curyear-birthyear

if(curmonth>birthmonth):
    print("age=",age)
elif (curmonth<birthmonth):
    print("age=", age-1)
else:
    if(curday>=birthday):
        print("age=",age)
    else:
        print("age=",age-1)