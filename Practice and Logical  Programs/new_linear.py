#Python Program to perform Linear Search
list1 = []
def Linear_search():
    take_input()
    display_list()
    num = input("Enter the number to be searched : ")
    for i in range(len(list1)):
        if list1[i] == num:
            print(num," found at position",i+1)
            break
    else:
        print(num," not found")

def take_input():
    n = int(input("Enter the size of list: "))
    for i in range(n):
        list1.append(input("Enter the element: "))

def display_list():
    print("The list is: ",list1)

Linear_search()