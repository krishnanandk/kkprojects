class Employee:
    companyname="luminar"
    def __init__(self,name,employeeid,salary):
        self.employeeid=employeeid
        self.salary=salary
        self.name=name

    def printvalue(self):
        print("name:",self.name)
        print("employeeid:",self.employeeid)
        print("salary:",self.salary)
        print("comapny:",Employee.companyname)

obj= Employee("kk",1100,60000)
obj.printvalue()