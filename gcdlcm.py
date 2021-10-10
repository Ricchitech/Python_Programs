#function to compute gcd, lcm of two numbers
import math

a=int(input("Enter first number: ")) #we can use random.randint(1,100) for random number instead of user input
b=int(input("Enter second number: "))

#using inbuilt function
print(math.gcd(a,b))
print(math.lcm(a,b))

#using while loop
i = 1
while(i <= a and i <= b):
  if(a % i == 0 and b % i == 0):
    gcd = i
  i = i + 1
print("GCD is", gcd)
print("LCM is",int(a*b/gcd))

#using recursion
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
print("GCD is", gcd(a,b))
print("LCM is",int(a*b/gcd(a,b)))




#using for temp variable
c,d=a,b #note: c,d are temporary variables #c=a,d=b
while(b != 0):
  temp = b
  b = a % b
  a = temp
gcd = a
print("GCD is", gcd)
print("LCM is",int(c*d/gcd))