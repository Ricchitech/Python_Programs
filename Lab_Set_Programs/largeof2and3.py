def largeof2():
    a = int(input("Enter a First number: "))
    b = int(input("Enter a Second number: "))
    if a > b:
        print("First number is Greater than Second number")
    elif a < b:
        print("Second number is Greater than First number")
    else:
        print("Both first and Second number are Equal")

def largeof3():
    a = int(input("Enter a First number: "))
    b = int(input("Enter a Second number: "))
    c = int(input("Enter a Third number: "))
    if a > b and a > c:
        lnum=a
    elif b > a and b > c:
        lnum = b
    elif c > a and c > b:
        lnum=c
    else:
        lnum="All 3 Numbers are Equal"
    print("Largest number among ",a,"",b,"and",c," is: ",lnum)

while(True):
    print("1. Find the largest number among 2 numbers")
    print("2. Find the largest number among 3 numbers")
    print("3. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        largeof2()
    elif ch == 2:
        largeof3()
    elif ch == 3:
        break
    else:
        print("Invalid Choice")