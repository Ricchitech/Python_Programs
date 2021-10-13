#Python program to find the largest of Two numbers.
import random
a = random.randint(1, 100)  # you can take any number of number as input
b = random.randint(1, 100)
def largeof2(a,b):
    if(a>b): 
        return a
    else: 
        return b

print("The largest of",a,"and",b,"is",largeof2(a,b))