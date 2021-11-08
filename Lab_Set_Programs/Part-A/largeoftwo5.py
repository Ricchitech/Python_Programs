#Python program to find the largest of Two numbers.
import random
a = random.randint(1, 100)  # you can take any number of number as input
b = random.randint(1, 100)
c = random.randint(1, 100)

def largeof2(a,b):
    if(a>b): 
        return a
    else: 
        return b

def largeof3(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

print("The largest of",a,"and",b,"is",largeof2(a,b))
print("Largest of ",a,"and",b,"and",c,"is",largeof3(a,b,c))