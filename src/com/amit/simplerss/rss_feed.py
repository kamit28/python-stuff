'''
Created on 2 Mar. 2018

@author: Amit.Kumar1
'''

## A Single Feed message
class FeedMessage:
    def __init__(self, title = '', link = '', description = '', author = '', guid = ''):
        self.title = title
        self.link = link
        self.description = description
        self.author = author
        self.guid = guid
    
    def __str__(self):
        return str(self.__dict__)
    
    def __eq__(self, other):
        return isinstance(self.__class__, other) and self.__dict__ == other.__dict__
    
## 
class Feed:
    def __init__(self, title = '', link = '', description = '', language = '' , published_on = ''):
        self.title = title
        self.link = link
        self.description = description
        self.language = language
        self.published_on = published_on
        self.entries = []
    
    def __str__(self):
        return str(self.__dict__)
