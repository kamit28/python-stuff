'''
Created on 27 Feb. 2018

@author: Amit.Kumar1
'''


def longest_palindrome(sourceStr):
    max_length = 1
    start = 0
    str_len = len(sourceStr)
    
    for i in range (1, str_len):
        low = i - 1
        high = i
        
        while low >= 0 and high < str_len and sourceStr[low] == sourceStr[high]:
            if(high - low + 1 > max_length):
                start = low
                max_length = high - low + 1
            low = low - 1
            high = high + 1
    
        low = i - 1
        high = i + 1
        while low >= 0 and high < str_len and sourceStr[low] == sourceStr[high]:
            if(high - low + 1 > max_length):
                start = low
                max_length = high - low + 1
            low = low - 1
            high = high + 1
    
    return sourceStr[start:start + max_length]


in_str = input("Enter input string: ")

longest_palin_str = longest_palindrome(in_str)

print(longest_palin_str)
