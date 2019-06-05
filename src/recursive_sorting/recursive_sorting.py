def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    j = 0
    i = 0
    idx = 0
    for x in range(elements):
        if i >= len(arrA):
            merged_arr[idx] = arrB[j]
            idx += 1
            j += 1
        elif j >= len(arrB):
            merged_arr[idx] = arrA[i]
            idx += 1
            i += 1
        elif arrA[i] > arrB[j]:
            merged_arr[idx] = arrB[j]
            j += 1
            idx += 1
        else:
            merged_arr[idx] = arrA[i]
            i += 1
            idx += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
