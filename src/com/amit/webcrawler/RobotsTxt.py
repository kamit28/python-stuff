'''
Created on 13 Mar. 2018

@author: Amit.Kumar1
'''
class RobotsTxt:
    def __init__(self, params):
        '''
        Constructor
        '''
        self.site = ''
        self.disallowed = set()
    
    def getSite(self):
        return self.site
    
    def getDisallowed(self):
        return self.disallowed
    
    def setSite(self, site_name):
        self.site = site_name
    
    def setDisallowed(self, disallowed_set):
        self.disallowed = self.disallowed.union(disallowed_set)
    
    def addDisallowed(self, a_path):
        self.disallowed.add(a_path)
    