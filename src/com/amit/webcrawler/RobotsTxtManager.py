'''
Created on 13 Mar. 2018

@author: Amit.Kumar1
'''
import pickle
import sqlite3

class RobotsManager():
    '''
    robots.txt manager for crawled web sites
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.robots_dict = {}
        self.conn = None
        
    def save_robots_data(self, ):
        self.conn = sqlite3.connect(':memory:')
        
    
    def process_robots_data(self, robots_data, site):
        our_instructions = False
        paths = set()
        if robots_data is not None and len(robots_data) > 0:
            for line in robots_data:
                if line == 'User-agent: *':
                    our_instructions = True
                    continue
                if our_instructions == True:
                    instruction, path = line.split(':')
                    if instruction.lower() == 'disallow':
                        paths.add(path)
            
            if len(paths) > 0:
                self.robots_dict[site] = paths 
                