#Python program to print ‘n terms of Fibonacci series using iteration.
#fibonacci series like : 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, …

n=int(input("Enter n value:"))

def fibonacci(n): #function to print fibonacci series
    a = 0
    b = 1
    if n < 0 or  n==0:
        print("Incorrect input")
    else:
        print("Fibonacci series:")
        for i in range(n):
            print(a, end=" ")
            c = a + b
            a = b
            b = c

fibonacci(n) #calling the function