class Student:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def printvalue(self):
        print("name:",self.name)
        print("age:",self.age)

    def __str__(self):
        return self.name

f=open("student","r")
for lines in f:
    words=lines.rstrip("\n").split(",")
    name=words[0]
    age=words[1]
    obj=Student(name,age)
    print(obj)
    obj.printvalue()
    print("."*50)