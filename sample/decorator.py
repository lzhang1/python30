#!/usr/bin/python
# -*- coding: utf-8 -*-

def now():
    print ('2015-03-25')

#代码运行期间动态增加功能的方式，称之为"装饰器"
def log(func):
    def wrapper(*args, **kw):
        print ('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper

if __name__ == "__main__":
    print (now.__name__)
    f = now
    print (f.__name__)
    @log
    def now():
        print ('2015-03-26')
    print (now())
    now = log(now)
    print (now)
