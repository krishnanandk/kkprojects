#construction is used to initialise instance variable
#constructor automatically invoke when creating object

class Person:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def printvalue(self):
        print("name:",self.name)
        print("age:",self.age)

obj=Person("kk",24)
obj.printvalue()
