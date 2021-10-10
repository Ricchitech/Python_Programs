# Python Program to perform insertion sort.

def insertion_sort(arr):
    print("\nInput Array : ", arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return display_sorted_array(arr)


def display_sorted_array(arr):
    print("\nSorted array is:")
    for i in range(len(arr)):
        print(arr[i], end=" ")


def create_array():
    n = int(input("Enter size of array"))
    for i in range(0, n):
        arr.append(int(input("Enter the elements of array : ")))
    return insertion_sort(arr)


arr = []
create_array()
