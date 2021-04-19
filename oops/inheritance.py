#single inheritance

class Vehicle:
    vehicle name="Car"
    def m1(self):
        print("",Parent.parentname)
        print(self.age)

class Child(Parent):
    childname="KV"
    def m2(self,cage):
        self.cage=cage
        print("parent name is",Parent.parentname)
        print(self.age)
        print("child name is",Child.childname)
        print(self.cage)

c=Child()
c.m1(23)
c.m2(5)