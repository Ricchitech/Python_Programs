# Python Program to perform Merge sort.

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]  # left sublist
        right = arr[mid:]  # right sublist

        mergeSort(left)  # Recursive call on each half
        mergeSort(right)

        i = 0  # Two iterators for traversing the two halves
        j = 0
        k = 0  # Iterator for the main list

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # The value from the left half has been used
                arr[k] = left[i]

                i += 1  # Move the iterator forward
            else:
                arr[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def take_input():
    n = int(input("Enter the size of list: "))
    for i in range(n):
        arr.append(int(input("Enter the element: ")))
    return mergeSort(arr)

arr = []
take_input()
print(arr)
