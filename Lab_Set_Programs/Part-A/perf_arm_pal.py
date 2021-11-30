#Program 6 : Perfect number , armstrong number , Palindrom number

#Find given number is Armstrong number or not
def armstrong():
    num = int(input("Enter Number:"))
    pow=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**pow
        temp//=10
    
    if num==sum:
        print(num,"Armstrong Number")
    else:
        print(num,"is Not Armstrong Number")

#Find given number is Palindrome number or not
def palindrome():
    num = int(input("Enter Number:"))
    temp=num
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp//=10
    if num==rev:
        print(num,"is Palindrome Number")
    else:
        print(num,"is Not Palindrome Number")

#Find given number is perfect number or not
def perfectno():
    num = int(input("Enter Number:"))  
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        print(num,"is Perfect Number")
    else:    
        print(num,"is Not Perfect Number")

while(True):
    print("1.Armstrong Number")
    print("2.Palindrome Number")
    print("3.Perfect Number")
    print("4.Exit\n")
    choice=int(input("Enter your choice:"))
    if choice==1:
        armstrong()
    elif choice==2:
        palindrome()
    elif choice==3:
        perfectno()
    elif choice==4:
        print("Thank you!")
        break
    else:
        print("Invalid Choice")
