#!/usr/bin/python
# -*- coding: utf-8 -*-
import functools
def int2(x,base=2):
    return int(x,base)
#functools中partial function 偏函数,把一个函数的某些参数固定住,返回一个新函数
if __name__=="__main__":
    print (int2('120',8))
    print (int2('10101'))
    int8 = functools.partial(int,base=8)
    print (int8('120'))
    kw = {'base':8}
    print (int('120',**kw))
    max2 = functools.partial(max,10)
    print (max2(5,6,7))
