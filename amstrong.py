##armstrong number
n=int(input("Enter a number"))
temp=n
pow=len(str(n))
sum=0
while(n>0):
    r=n%10
    sum=sum+(r**pow)
    n=n//10
if(temp==sum):
    print("armstrong number")
else:
    print("not armstrong number")

#length of the number or number of digits in a number
# len=0
# n=int(input("Enter a number"))
# while(n>0):
#     n=n//10
#     len=len+1
# print("length of number is",len)
