class Employee:
    companyname="ABC"

    def __init__(self,name,employeeid,salary):
        self.employeeid=employeeid
        self.name=name
        self.salary=salary

    def printDetails(self):
        print("companyname +",self.companyname)
        print("name of employee",self.name)
        print("employeeid",self.employeeid)
        print("salary",self.salary)


    def __str__(self):
        return str(self.employeeid)

obj=Employee("krishna",101,1000000)
print(obj)