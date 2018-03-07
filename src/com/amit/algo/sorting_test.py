#!/usr/bin/python

from sorting_algos import quick_sort
from sorting_algos import merge_sort

arr = [7, 2, 9, 13, 4, 1, 3, 5, 6, 8]

print(arr)        
quick_sort(arr, 0, 9)

print(arr)

arr = [5, 6, 2, 7, 13, 1, 9, 4, 8, 3]
print(arr)
merge_sort(arr, 0, 9)
print(arr)


