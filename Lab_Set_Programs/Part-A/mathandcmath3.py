#Program 3 : Quadratic Equation using math and cmath functions

import math,cmath
def quadratic(a,b,d):
    if d < 0:
        x1 = (-b + cmath.sqrt(d))/(2*a)
        x2 = (-b - cmath.sqrt(d))/(2*a)
        return print("The roots of the equation are: ", x1, x2)
    elif d>0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        return print("The roots of the equation are {:6.2f} {:6.2f} ".format(x1,x2))
    elif d==0:
        x1=-b/2*a
        x2=x1
        return print("The roots of the equation are: ",x1,x2)

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = (b**2) - (4*a*c)
print(d)
quadratic(a, b, d)
