#!/usr/bin/python
d = dict(name='visaya', age=20)
print (d)
c = dict(zip(['name','age'],['visaya',20]))
print (c)
#把listkeys中的元素作为key均赋值为value，默认为0
e = dict.fromkeys(['name','age'],1)
print (e)
