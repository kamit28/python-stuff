'''
Created on 22 Mar. 2018

@author: Amit
'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks.get(query_name)
    if marks is not None:
        result = sum(x for x in marks)/ len(marks)
        print("%.2f" % result)
