#demonstrate the usage of math and cmath module (for ex: roots of the quadratic equation)

import math,cmath

def using_math(a,b,c):
    d = (b**2) - (4*a*c)
    if d < 0:
        return print("The equation has no real roots")
    else:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        return print("The roots of the equation are: ",x1,x2)

def using_cmath(a,b,c):
    d = (b**2) - (4*a*c)
    if d < 0:
        return print("The equation has no real roots")
    else:
        x1 = (-b + cmath.sqrt(d))/(2*a)
        x2 = (-b - cmath.sqrt(d))/(2*a)
        return print("The roots of the equation are: ",x1,x2)


a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
using_math(a,b,c)
using_cmath(a, b, c)