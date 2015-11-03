#!/usr/bin/python
# -*- coding: utf-8 -*-

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

if __name__=="__main__":
    try:
        print ('try...')
        bar('0')
        print ('result:',r)
    except ValueError as e:
        print ('ValueError:',e)
    except ZeroDivisionError as e:
        print ('except:',e)
    else:
        print ('no error!')
    finally:
        print ('finally...')
    print ('END')
