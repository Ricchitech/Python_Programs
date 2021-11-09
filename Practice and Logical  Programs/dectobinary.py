
def create_array():
    for i in range(0, 4):
        arr.append(int(input()))
    return decimaltobinary(arr)

def decimaltobinary(arr):
    for i in range(0, len(arr)):
        print(bin(arr[i])[2:])

arr=[]
create_array()
