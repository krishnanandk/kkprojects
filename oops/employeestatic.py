class Employee:
    companyname="luminar"
    def setVal(self,name,employeeid,salary):
        self.employeeid=employeeid
        self.salary=salary
        self.name=name

    def printvalue(self):
        print("name:",self.name)
        print("employeeid:",self.employeeid)
        print("salary:",self.salary)
        print("comapny:",Employee.companyname)

obj= Employee()
obj.setVal("ram",1001,100000)
obj.printvalue()