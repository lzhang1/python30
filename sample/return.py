#!/usr/bin/python
# -*- coding: utf-8 -*-

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args[0]:
            ax = ax + n
        return ax
    return sum
#相关参数和变量都保存在返回的函数中，这种称为"闭包"
def count1():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return  fs

def count2():
    def f(j):
        def g():
            return j*j 
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

if __name__=="__main__":
    l = (1,3,5,7,9)
    print (l)
    f1 = lazy_sum(l)
    f2 = lazy_sum(l)
    print (f1==f2)
    f3,f4,f5 = count1()
    print (f3())
    print (f4())
    print (f5())
    f6,f7,f8 = count2()
    print (f6())
    print (f7())
    print (f8())
