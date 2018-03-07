'''
Created on 22 Feb. 2018

@author: Amit.Kumar1
'''
import sys


def count_lines(afile):
    count = 0;
    for line in afile:
        count += 1
    return count


def count_words(afile):
    count = 0;
    for line in afile:
        words = line.split(" ")
        count += len(words)
    return count


def count_chars(afile):
    count = 0
    for line in afile:
        chars = len(line)
        count += chars
    return count


if(len(sys.argv) == 1 or sys.argv[1] == '-h'):
    print('word_count.py [-w][-c][-l] <filename>')
    sys.exit()

# script = sys.argv[0]
arg_len = len(sys.argv)
flags = []
if(arg_len > 2):
    for i in range(1, arg_len - 1):
        flags.append(sys.argv[i])
file_name = sys.argv[arg_len - 1]   
    
char_count = 0
line_count = 0
word_count = 0
for flag in flags:
    print(file_name)
    file_handle = open(file_name, "r")
    
    if(flag == '-c'):
        char_count = count_chars(file_handle)
    if(flag == '-w'):
        word_count = count_words(file_handle)
    if(flag == '-l'):
        line_count = count_lines(file_handle)

output_str = ''
if(line_count > 0):
    output_str += str(line_count) + "\t"
if(word_count > 0):
    output_str += str(word_count) + "\t"
if(char_count > 0):
    output_str += str(char_count) + "\t"
print(output_str, file_name)
