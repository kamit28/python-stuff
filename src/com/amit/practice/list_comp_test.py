'''
Created on 22 Mar. 2018

@author: Amit.Kumar1
'''
if __name__ == '__main__':
    n = int(input())
    student_list = [[input(), float(input())] for _ in range(n)]
    student_list.sort(key=lambda student: student[1])
    index = 1
    while index < len(student_list) and student_list[index][1] == student_list[0][1]:
        index += 1
    start = index
    second_lowests = []
    if index < len(student_list):
        second_lowests.append(student_list[index][0])
        index += 1
        while index < len(student_list) and student_list[index][1] == student_list[start][1]:
            second_lowests.append(student_list[index][0])
            index += 1
    
        for name in sorted(second_lowests):
            print(name)
