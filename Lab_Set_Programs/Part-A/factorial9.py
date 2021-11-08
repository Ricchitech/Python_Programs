#Factorial program with recursion function and without recursion function

def factusingrecursion():
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    n = int(input("Enter a number to compute the factorial : "))
    print("Factorial of",n,"is",factorial(n))


def withoutrecursion():
    n = int(input("Enter a number to compute the factorial : "))
    fact = 1
    if n<0:
        print("Sorry, Factorial does not exist for negative number")
    elif n == 0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1,n+1):
            fact = fact*i
        print("Factorial of",n,"is",fact)

while True:
    print("\n1. Factorial using Recursion function\n2. Factorial without Recursion function\n3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        factusingrecursion()
    elif choice == 2:
        withoutrecursion()
    elif choice == 3:
        print("Thank you")
        break
    else:
        print("Invalid choice")
