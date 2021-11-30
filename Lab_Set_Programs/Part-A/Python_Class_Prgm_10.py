#Program 10 : Program to demonstrate the class property

#class professional
class professional:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o
    def do_work(self):
        print(self.name,"is a/an ",self.occupation)
    def speaks(self):
        print(self.name,"says how are you??")

brg=professional("Bharathraj","Full Stack Devoloper")
brg.do_work()
brg.speaks()

chn=professional("Chinnu","Project Manager")
chn.do_work()
chn.speaks()

# ads = professional("Adarsh", "Software Architect")
# ads.do_work()
# ads.speaks()

print("\n")

# Class customer
class customer:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
        print("The initial Balance is ",self.balance)
    def withdraw(self,amount):
        if(amount>self.balance):
            raise Exception()
        self.balance-=amount
        return self.balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance

lee=customer("Leela",500000)
print(lee.name,"has",lee.balance,"balance")
print("The balance in the account after withdrawal is",lee.withdraw(300000))
print("The balance in the account after deposit is",lee.deposit(500000))

print("\n")

class CSStudent:
    count=0 #Class variable
    def __init__(self,name,roll):
        self.name=name
        self.__roll=roll
        CSStudent.count+=1

    @staticmethod
    def status():
        print("The Total number of students are ",CSStudent.count)
    
    def __private_method(self):
        print("This is a private method")
    
    def public_method(self):
        self.__private_method()


print("\n")


#Objects of CSStudent class

a=CSStudent("Bharathraj",1)
print("The value of the static variable when one object got created is",CSStudent.count)
b=CSStudent("Chinnu",2)
print("private attribute is",a._CSStudent__roll)
a.public_method()
c=CSStudent("Adarsh",3)


print("The value of the static variable when one object got created \"a\"is",a.count)
print("The value of the static variable when one object got created \"b\"is",b.count)
print("The value of the static variable when one object got created \"c\"is",c.count)
print(a.name)
print(b.name)
print(c.name)
print(a._CSStudent__roll)
print(b._CSStudent__roll)
print(c._CSStudent__roll)

CSStudent.status()
