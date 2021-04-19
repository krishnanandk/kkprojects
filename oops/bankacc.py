class Bank:
    bname="sbi"
    def acCreate(self,acno,name,):
        self.acno=acno
        self.name=name
        self.minimumbal=5000
        self.balance=self.minimumbal

    def deposit(self,amt):
        self.balance+=amt
        print("ypur",Bank.bname,"account has been credited with",amt)
        print("your currrent balance=",self.balance)

    def withdraw(self,amt):
        if amt>self.balance:
            print("insufficient balance")
        else:
            print("account debited with",amt)
            self.balance-=amt

obj=Bank()
obj.acCreate(123,"abc")
obj.deposit(2500)
obj.withdraw(1000)

#instance variables related to objects

#static variable reated to class