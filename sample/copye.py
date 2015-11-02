#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy
dict1 = {"a" : "apple", "b" : {"g" : "grape","o" : "orange"}}
dict2 = copy.deepcopy(dict1)
dict3 = copy.copy(dict1)
dict2["b"]["g"] = "orange"
print ("dict2: %s"%dict2)
print ("dict1: %s"%dict1)
dict3["b"]["g"] = "orange"
print ("dict3: %s"%dict3)
print ("dict1: %s"%dict1)
