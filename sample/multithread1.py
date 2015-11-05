#!/usr/bin/python
# -*- coding: utf-8 -*-
import time, threading
import os

def loop():
    print ('thread %s is running...' % threading.current_thread().name)
    n = 0 
    while n < 5:
        print('Process ID: %s' % os.getpid())
        n = n + 1
        print ('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

if __name__ == "__main__":
    print('Process ID: %s' % os.getpid())
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)
