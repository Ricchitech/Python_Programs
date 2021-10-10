#Python Program to perform Merge sort.
arr = [1,2,35,4,5,6,7,8,9]
L=[]
R=[]
def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr)//2 #Finding the mid of the array
        L = arr[:mid] # Dividing the array elements
        R = arr[mid:] # into 2 halves

        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half
        print(mergeSort(L))
        print(mergeSort(R))

mergeSort(arr)
