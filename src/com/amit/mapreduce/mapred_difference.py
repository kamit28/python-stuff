'''
Created on 28 Aug. 2018

@author: Amit.Kumar1
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
# This template is based on the framework supplied for a similar challenge, in a Coursera Data Science course: https://www.coursera.org/course/datasci
# And the code supplied here: https://github.com/uwescience/datasci_course_materials/blob/master/assignment3/wordcount.py
# The map-reduce emulator is provided
# You need to fill out the mapper and reducer functions

import json
import sys
from collections import OrderedDict
class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []

    def emitIntermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for line in data:
            record = json.loads(line)
            mapper(record)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        jenc = json.JSONEncoder()
        for item in self.result:
            print("{key:"+str(item[0])+",value:" + str(item[1]) + "}")

mapReducer = MapReduce()

def mapper(record):
    key = record["key"]
    value = record["value"]
    mapReducer.emitIntermediate(value, key)

def reducer(key, list_of_values):
    if len(list_of_values) >= 1 and list_of_values.count('S') == 0:
        mapReducer.emit((key, list_of_values))


if __name__ == '__main__':
    inputData = []
    counter = 0
    try:
        file_handle = open("C:/Users/Amit.Kumar1/Desktop/difference2.txt", "r")
        
        for line in file_handle:
            if counter == 0:
                (R,S) = line.split(" ")
                key = "R"
            else:
                if counter > int(R):
                    counter = 1
                    key = "S"
                inputData.append(json.dumps({"key":key,"value":line}))
            counter += 1
    finally:
        file_handle.close()
    mapReducer.execute(inputData, mapper, reducer)
