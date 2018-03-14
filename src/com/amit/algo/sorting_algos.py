#!/usr/bin/python

'''
partition method to find pivot.
to be used by quicksort
'''
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i + 1]
    return i + 1

'''
The quicksort algorithm
'''
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)

        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

'''
The merge routine for merge sort
'''
def merge_lists(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid

    l_temp = [0] * n1
    r_temp = [0] * n2

    for i in range(0, n1):
        l_temp[i] = arr[low + i]
    for i in range(0, n2):
        r_temp[i] = arr[mid + 1 + i]

    i = 0
    j = 0
    k = low

    while i < n1 and j < n2:
        if l_temp[i] < r_temp[j]:
            arr[k] = l_temp[i]
            i += 1
        else:
            arr[k] = r_temp[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = l_temp[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = r_temp[j]
        j += 1
        k += 1

'''
The merge sort algorithm
'''
def merge_sort(arr, low,  high):
    if high > low:
        mid = (low + high) / 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge_lists(arr, low, mid, high)

