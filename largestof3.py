#Python program to find the largest of three numbers.
import random
a=random.randint(1,100) #you can take any number of number as input
b=random.randint(1,100)
c=random.randint(1,100)

print(a,"",b,"",c)
if(a>b and a>c):
    print("a is the largest")
elif(b>a and b>c):
    print("b is the largest")
else:
    print("c is the largest")