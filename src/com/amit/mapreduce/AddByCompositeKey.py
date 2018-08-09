'''
Created on 8 Aug. 2018

@author: Amit.Kumar1
'''
import json
import sys
from collections import OrderedDict
import math


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
            print("{key:" + item[0] + ",value:" + str(item[1]) + "}")


mapReducer = MapReduce()


def mapper(record):
    key = record["key"]
    value = record["value"]
    # COMPLETE THE LINE BELOW BY FILLING UP THE QUESTION MARKS      
    mapReducer.emitIntermediate(key, float(value))


def reducer(key, list_of_values):
    # COMPLETE THE LINE BELOW BY FILLING UP THE QUESTION MARKS
    mapReducer.emit((key, int(round(sum(list_of_values)))))


if __name__ == '__main__':
    inputData = []
    counter = 0
    try:
        file_handle = open("C:/Users/Amit.Kumar1/Desktop/SumByKeys.txt", "r")

        for line in file_handle:
            counter += 1
            country, state, city, population = line.strip().split("\t")
            inputData.append(json.dumps({"key":country + "," + state, "value":population}))
    finally:
        file_handle.close()
    mapReducer.execute(inputData, mapper, reducer)
