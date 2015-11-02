#!/usr/bin/python
# -*- coding: utf-8 -*-
t = ['a','b',['A','B']]
print ("intial tuple: ",t)
t[2][0] = 'X'
t[2][1] = 'Y'
print ("updated tuple: ",t)
