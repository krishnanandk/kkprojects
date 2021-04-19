class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printVal(self):
        print("name:",self.name)
        print("age:",self.age)
class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed=breed
    def print(self):
        print("breed:",self.breed)

cr=Dog("Britto",5,"lab")
cr.printVal()
cr.print()
