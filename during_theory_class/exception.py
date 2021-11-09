a= int(input("Enter a"))
b= int(input("Enter b"))
# c = a/b
# print("a/b = %d" % c)

try:
    c=a/b
    print("a/b = %d"%c)
except:
    print("Cant divide with zero")
