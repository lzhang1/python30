#!/usr/bin/python
# -*- coding: utf-8 -*-
def deco1(func):
    def _deco():
        print ("before myfunc() called")
        func()
        print ("after myfunc() called")
    return _deco

@deco1 
def myfunc1():
    print ("myfunc() called.")
    return 'ok'
print ("-----1. none arguments-----")
myfunc1()
myfunc1()

def deco2(func):
    def _deco(a,b):
        print ("before myfunc() called")
        ret = func(a,b)
        print ("after myfunc() called")
        return ret
    return _deco

@deco2 
def myfunc2(a,b):
    print ("myfunc(%s,%s) called."%(a,b))
    return a + b

print ("-----1. with arguments-----")
myfunc2(1,2)
myfunc2(3,4)

def deco3(func):
    def _deco(*args,**kw):
        print ("before %s called"%func.__name__)
        ret = func(*args,**kw)
        print ("after %s called. result: %s"%(func.__name__,ret))
        return ret
    return _deco

@deco3
def myfunc3(a,b):
    print ("myfunc(%s,%s) called."%(a,b))
    return a + b

@deco3
def myfunc4(a,b,c):
    print ("myfunc(%s,%s,%s) called."%(a,b,c))
    return a + b + c

print ("-----3. with many arguments-----")
myfunc3(1,2)
myfunc3(3,4)
myfunc4(1,2,3)
myfunc4(3,4,5)

def deco4(arg):
    def _deco(func):
        def __deco():
            print ("before %s called [%s]."%(func.__name__,arg))
            func()
            print ("after %s called [%s]."%(func.__name__,arg))
        return __deco
    return _deco
@deco4("mymodule1")
def myfunc5():
    print ("myfunc5() called")

@deco4("mymodule2")
def myfunc6():
    print ("myfunc6() called")

print ("-----4. arguments-----")
myfunc5()
myfunc6()


