#Python Program to find the maximum from a list of numbers.

#by user input
num = int(input("Enter the size of list: "))
list1 = []
newlist = []
#create a list
for i in range(num):
    list1.append(int(input("Enter the element: ")))

#using built-in function max
print("Maximum element in the list is:", max(list1))

#using sort function
list1.sort()
print("Maximum element in the list is:", list1[-1])


#using user defined function
def maxfromlist(list1):
    max = list1[0]
    for i in list1:
        if i > max:
            max = i
    return max
print("Maximum element in the list is:", maxfromlist(list1))