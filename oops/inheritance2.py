#multiple inheritance

class Parent:
    parentname="KK"
    def m1(self,age):
        self.age=age
        print("my name is",Parent.parentname)
        print(self.age)

class Mobile:
    def mob(self):
        print("i have Samsung Galaxy M31")

class Child(Parent,Mobile):
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
c.mob()