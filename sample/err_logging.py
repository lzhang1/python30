#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

if __name__=="__main__":
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
    print ('END')
