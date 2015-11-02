#!/usr/bin/python
# -*- coding: utf-8 -*-
from functools import reduce
def power(x,n=3):
    res = 1
    for i in range(n):
        res = res * x
    return res

def add(x,y):
    return x + y

def fn(x,y):
    return 10*x + y

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

def ff(x,y):
    return x + y

def normalize(name):
    return name.capitalize()

def fm(x,y):
    return x * y

if __name__ == "__main__":
    l1 = [i for i in range(10)]
    #map()接受参数一个函数f,一个Iterable,生成一个新的Iterator
    print (list(map(power,l1)))
    print (l1)
    print (list(map(str,l1)))
    #reduce()接受一个函数f,一个序列上，会把结果和序列下一个元素累积计算
    #reduce(f,[x1,x2,x3,x4] = f(f(f(x1,x2),x3),x4)
    l2 = [i for i in range(1,10,2)]
    print (l2)
    print (sum(l2))
    print (reduce(add,l2))
    print (reduce(fn,l2))
    str1 = '12345'
    print (reduce(fn,map(char2num,str1)))
    print (reduce(lambda x,y:x*10+y,map(char2num,str1)))

    l3 = ['adam','LIST','BarT']
    print (list(map(normalize,l3)))
    l4 = [1,2,3,4,5]
    print (reduce(fm,l4))
    str2 = '123.4897998956'
    print (str2)
    lstr2 = str2.split('.')
    istr2int = reduce(fn,map(char2num,lstr2[0]))
    dec = 1
    for i in range(len(lstr2[1])):
        dec = dec * 0.1
    dstr2int = dec * reduce(fn,map(char2num,lstr2[1]))
    str2float = istr2int + dstr2int
    print ('%.*f'%(len(lstr2[1]),str2float))
    print (str2float)
