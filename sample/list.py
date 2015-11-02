#!/usr/bin/python
# -*- coding: utf-8 -*-
sample_list = [i for i in range(10)]
print (sample_list)
print ("first item: ",sample_list[-len(sample_list)])
print ("last item: ",sample_list[len(sample_list)-1])
print ("count of 1 in list: ",sample_list.count(1))
print ("index of 3 in list: ",sample_list.index(3))
sample_list.sort()
print (sample_list)
sample_list.reverse()
print (sample_list)
sample_list.append(1)
print ("count of 1 in list: ",sample_list.count(1))
print (sample_list)
