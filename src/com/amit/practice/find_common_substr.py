'''
Created on 27 Feb. 2018

@author: Amit.Kumar1
'''


def common_substr(str1, str2):
    visited = [False] * 26
    
    for i in range(0, len(str1)):
        visited[str1[i] - 'a'] = True
    
    for i in range(0, len(str2)):
        if(visited[str2[i] - 'a']):
            return True
