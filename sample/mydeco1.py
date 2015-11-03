#!/usr/bin/python
# -*- coding: utf-8 -*-
class locker:
    def __init__(self):
        print ("locker.__inti__() should be not called.")

    @staticmethod
    def acquire():
        print ("locker.acquire() called 静态方法")

    @staticmethod
    def release():
        print ("locker.release() called 静态方法")

def deco(cls):
    def _deco(func):
        def __deco():
            print ("before %s called [%s]." % (func.__name__, cls))
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()
        return __deco
    return _deco

@deco(locker)
def myfunc():
    print ("myfunc() called.")

myfunc()


