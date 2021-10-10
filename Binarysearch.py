#Python Program to perform Binary Search

def binary_search(list1):
    #list = [1,2,3,4,5,6,7,8,9,10]
    print("List is : ", list1)
    search = int(input("Enter the number to be searched: "))
    start = 0
    end = len(list1) - 1
    found = False
    while start <= end and not found:
        mid = (start + end) // 2
        if list1[mid] == search:
            found = True
        else:
            if search < list1[mid]:
                end = mid - 1
            else:
                start = mid + 1
    if found:
        print("Element found at position: ", mid + 1)
    else:
        print("Element not found")

def create_list():
    n=int(input("Enter the size of list: "))
    list1 = []
    for i in range(n):
        list1.append(int(input("Enter element : ")))
    return binary_search(list1)

create_list()