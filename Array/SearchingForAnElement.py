import array

my_array1 = array.array('i',[1,2,3,4,5])

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search(my_array1, 3))