##armstrong number

n=int(input("Enter a number"))
temp=n #assign to the temp variable
pow=len(str(n)) #length of the string
sum=0
while(n>0):
    r=n%10
    sum=sum+(r**pow) #sum+(r^pow)
    n=n//10
if(temp==sum): #if the sum is equal to the number
    print("armstrong number")
else:
    print("not armstrong number")