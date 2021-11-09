num=int(input("Enter number: "))
exp=int(input("Enter exponential value: "))
res=1
for i in range(1,exp+1):
    res=res*num
print("res is:",res)