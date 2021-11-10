#Program 4 : Find the largest of Five numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))
e = int(input("Enter the fifth number: "))
if a > b and a > c and a > d and a > e:
    print("The largest number is: ", a)
elif b > a and b > c and b > d and b > e:
    print("The largest number is: ", b)
elif c > a and c > b and c > d and c > e:
    print("The largest number is: ", c)
elif d > a and d > b and d > c and d > e:
    print("The largest number is: ", d)
elif e > a and e > b and e > c and e > d:
    print("The largest number is: ", e)
else:
    print("The numbers are equal")
