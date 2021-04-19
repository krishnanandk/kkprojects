class Person:
  def m1(self,name,age):
     self.name=name
     self.age=age

class Job:
    def m2(self,job,salary):
    self.job=job
    self.salary=salary

class Child(Person,Job):
    def m3(self,cname,childage):
        self.cname=cname
        self.childage=childage
    def print(self):
        print(self.name,self.age,self.job,self.salary,self.cname,self.childage)

class Mark(Child):
    def m4(self,mark1,mark2):
        self.mark1=mark1
        self.mark2=mark2
    def print2(self):
        print("Child:"self.cname,self.cage,"Marks:",self.mark1,self.mark2)

obj=Mark()



