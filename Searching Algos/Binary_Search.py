# Binary Search in python
class binarySearch:
    def __init__(self):
        self.a = 0
    def binarySearch(self,array, x, low, high):
        while low <= high:
            mid = low + (high - low)//2
            if array[mid] == x:
                return mid
            elif array[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return -1


def main():

    array = [3, 4, 5, 6, 7, 8, 9]
    x = int(input("Enter a number to search : "))
    b = binarySearch()
    result = b.binarySearch(array, x, 0, len(array)-1)
    if result != -1:
        print("Element is present at index " + str(result))
    else:
        print("Not found")
main()

