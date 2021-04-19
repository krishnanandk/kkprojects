class Student:
    def __init__(self,name,rollno,course,mark):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.mark=mark
    def printvalue(self):
        print("name:",self.name)
        print("roll no:",self.rollno)
        print("course:",self.course)
        print("mark:",self.mark)

    def __str__(self):
        return self.name

f=open("student2","r")
for lines in f:
    words=lines.rstrip("\n").split(",")
    name=words[0]
    rollno=words[1]
    course=words[-2]
    mark=int(words[-1])
    obj=Student(name,rollno,course,mark)
    if(mark==200):
        print(obj)
        obj.printvalue()
        print("*"*50)
