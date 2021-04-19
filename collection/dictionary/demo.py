#dictionary

# dic={}
# print(type(dic))

#key-value pairs

# roll=1001
# name=arun
# age=25
#
# key: roll,name,age
# value;1001,arun,25

# student={"roll":1001,"name":"arun","age":24}   #it supports homogenous
# print(student)
#
# student={"roll":1001,"name":"arun","age":24,"age":25}
# print(student) #duplicate key not supported, but value supported

#insertion order preserved

student1={"roll":1001,"name":"arun","age":24,"opp":25}
print(student1["age"]) # to fetch a value using corresponding keys
print(student1["name"])

#roll:1001
#name:arun
#age:25
#opp:25

# for i in student1:
#     print(i,",",student1[i])



#Update

student1["name"]="arjun"
student1["age"]="30"
student1["opp"]+=10
print(student1)

#del

del student1["opp"]
print(student1)


print("total"in student1)#to check a key is present in a dictionary
print("age"in student1)

# to add new key and value
#total 500
student1["total"]=150
print(student1)