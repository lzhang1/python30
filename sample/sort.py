#!/usr/bin/python
dict1 = {"a" : "apple", "b" : "grape", "c" : "orange", "d" : "banana"}
print ("initial dict1: %s"%dict1)
dict2 = sorted(dict1.items(),key=lambda d:d[0])
print ("order by key: %s"%dict2)
dict3 = sorted(dict1.items(),key=lambda d:d[1])
print ("order by value: %s"%dict3)
ks = list(dict1.keys())
ks.sort()
for k in ks:
    print (k,dict1[k])
dict4 = {value:key for key,value in dict1.items()}
print (dict4)
def sortedDictValue1(adict):
    keys = adict.keys()
    sorted(keys)
    return [adict[key] for key in keys]

print (sortedDictValue1(dict1))
