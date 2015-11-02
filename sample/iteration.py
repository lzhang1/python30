#!/usr/bin/python
<<<<<<< HEAD
# -*- coding: utf-8 -*-
=======
>>>>>>> c9567d881ab593db8a0608dd06a5b1911f7c6a4a
from collections import Iterable
for ch in 'ABCD':
    print (ch)
# 通过collections模块中Iterable类型判断
print (isinstance('abc',Iterable))
print (isinstance([1,2,3,4],Iterable))
print (isinstance(123,Iterable))
#enumerate 把list变成索引-元素对
for index,value in enumerate(['Michael','Bob','Jack','Sarah']):
    print ("index:%s"%index,"value:%s"%value)

for x,y in [(1,2),(3,4),(5,6)]:
    print (x,y)
