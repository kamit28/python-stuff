'''
Created on 2 Mar. 2018

@author: Amit.Kumar1
'''
import time

from collections import deque
from functools import reduce

def reverse_text10(text_t):
    return reduce(lambda x, y : y + x, text_t)


def reverse_text9(text_t):
    r = []

    length = len(text_t)
    for i in range(length, 0, -1):
        r.append(text_t[ i - 1])

    return "".join(r)


def reverse_list8(text_t):
    li = list(text_t)  # convert string to list

    ret = [ li[i - 1] for i in range(len(li), 0, -1)  ]  # 1 liner lambda
    return "".join(ret)


def reverse_text7(text_t):
    s = ""
    l = len(text_t)
    for i in range(l):
        s += text_t[l - 1 - i]
        return s


def reverse_text6(text_t):
    return ''.join(item[1] for item in sorted(enumerate(text_t), reverse=True))


def reverse_text5(text):
    q = deque(text)
    return ''.join(q.pop() for _ in range(len(text)))


def reverse_text4(text):
    backwardstext = []
    for letter in text:
        backwardstext.insert(0, letter)
    return ''.join(backwardstext)


def reverse_text3(strs):
    return ''.join([strs[i] for i in range(len(strs) - 1, -1, -1)])


def reverse_text2(iterable):
    d = deque()
    d.extendleft(iterable)
    return ''.join(d)


def reverse_text1(text_t):
    if len(text_t) <= 1:
        return text_t
    
    return reverse_text1(text_t[1:]) + text_t[0]


def reverse_text0(text_t):
    len_str = len(text_t)
    str_list = [''] * len_str
    for i in range(0, len_str // 2):
        str_list[i] = text_t[len_str - i - 1]
        str_list[len_str - i - 1] = text_t[i]
    return ''.join(str_list)

def reverse_text(text_t):
    return text_t[::-1]

current_milli_time = lambda: int(round(time.time() * 1000))

input_str = input("Enter a String: ")
for i in range(0, 50000):
    reverse_text(input_str)
start_time = current_milli_time()
for i in range(0, 10000):
    reverse_text(input_str)
end_time = current_milli_time()
print(end_time - start_time)
