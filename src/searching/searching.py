# STRETCH: implement Linear Search
def linear_search(arr, target):

    # TO-DO: add missing code
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code
    while low < high:
        if arr[low] == target:
            return low
        elif arr[high] == target:
            return high
        low = low+1
        high = high - 1

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    if len(arr) == 0:
        return -1  # array empty

    middle = len(arr)//2
    # TO-DO: add missing if/else statements, recursive calls
    if arr[middle] == target:
        return middle
    elif arr[middle] > target:
        return binary_search_recursive(arr[0:middle], target, 0, middle)
    elif arr[middle] < target:
        return middle + binary_search_recursive(arr[middle:], target, 0, middle)
