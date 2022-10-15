# Linear Search in Python
def linearSearch(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1


arr = [5,22,6,1,99,24,2,9]
x = int(input('Enter a number to find : '))
n = len(arr)
result = linearSearch(arr, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)
