a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
while b != 0:
    a, b = b, a % b
print("The gcd of", a, "and", b, "is", a)