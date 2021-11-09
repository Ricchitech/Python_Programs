#Python Program to perform Selection Search

def selection_search(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

def main():
    create_array()
    x = int(input("Enter the key element to be searched"))
    n = len(arr)
    result = selection_search(arr, n, x)
    if result != -1:
        print("Element is present at index", result,"or in ",result+1,"place")
    else:
        print("Element is not present in array")

def create_array():
    n = int(input("Enter size of array"))
    for i in range(0, n):
        arr.append(int(input("Enter the elements of array : ")))
    return arr

arr = []
main()