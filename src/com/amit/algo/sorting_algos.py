'''
Created on 23 Feb. 2018

@author: Amit.Kumar1
'''
from array import array


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high - 1):
        if(arr[j] < pivot):
            i = i + 1;
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return i + 1


def quick_sort(arr, low, high):
    if(low < high):
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(0, arr_len - 1):
        for j in range(i + 1, arr_len) :
            if(arr[i] > arr[j]):
                swap(arr, i, j)


arr = [5, 3, 1, 4, 0, 7, 9, 2]

bubble_sort(arr)
print(arr)

arr = [5, 3, 1, 4, 0, 7, 9, 2]
quick_sort(arr, 0, len(arr) - 1)
print(arr)

