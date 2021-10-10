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