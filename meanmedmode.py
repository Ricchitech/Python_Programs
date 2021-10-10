#Find mean, median, mode for the given set of numbers in a list.

#list = [2,5,8,4,7]

def create_list():
    n=int(input("Enter the size of the list: "))
    for i in range(n):
        list.append(int(input("Enter a number: ")))
    print()
    return display_patterns(list)

def mean_list(list):
    sum=0
    for i in list:
        sum+=i
    mean=sum/len(list)
    return mean

def mode_list(list):
    mode=[]
    count=[]
    for i in list:
        if i in mode:
            count[mode.index(i)]+=1
        else:
            mode.append(i)
            count.append(1)
    max_count=max(count)
    for i in range(len(count)):
        if count[i]==max_count:
            return mode[i]

def range_list(list):
    list.sort()
    return list[-1]-list[0]

def Median_list(list):
    list.sort()
    if len(list)%2==0:
        return list[int(len(list)/2)]
    else:
        return (list[int(len(list)/2)]+list[int(len(list)/2)-1])/2

def display_patterns(list):
    print("Mean: ",mean_list(list))
    print("Median: ", Median_list(list))
    print("Mode: ",mode_list(list))
    print("Range: ",range_list(list))

list = []
create_list()