#length of the number or number of digits in a number
len=0
n=int(input("Enter a number"))
while(n>0):
    n=n//10
    len=len+1
print("length of number is",len)
