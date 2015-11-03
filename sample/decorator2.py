#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
def foo():
    print ('in foo()')

def timeit(func):
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print ('used: %f'%(end-start))
    return wrapper

if __name__ == "__main__":
    @timeit
    def foo():
        print ('in foo()')
    foo()
