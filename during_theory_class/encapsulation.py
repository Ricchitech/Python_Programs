#creating a base class for

class Base:
    def __init__(self):

        #Protected member with _underscore
        self._a=2

#creating a derived class for
class Devired(Base):
    def __init__(self):
        #calling constructor of base class
        Base.__init__(self)
        print("Calling protected member of base class: ")
        print(self._a)

obj1=Devired()

obj2=Base()

#calling protected member outside class
print(obj2.a)