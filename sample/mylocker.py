#!/usr/bin/python
# -*- coding: utf-8 -*-
class mylocker:
    def __init__(self):
        print ("mylocker.__init__() called.")

    @staticmethod
    def acquire():
        print ("mylocker.acquire() called")

    @staticmethod
    def unlock():
        print ("mylock.unlock() called")

class lockerex(mylocker):
    @staticmethod
    def acquire():
        print ("lockerex.acquire() called")

    @staticmethod
    def unlock():
        print ("lockerex.unlock() called")

def lockhelper(cls):
    def _deco(func):
        def __deco(*args,**kw):
            print ("before %s called." % func.__name__)
            cls.acquire()
            try:
                return func(*args,**kw)
            finally:
                cls.unlock()
        return __deco
    return _deco
