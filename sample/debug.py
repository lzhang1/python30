#!/usr/bin/python
# -*- coding: utf-8 -*-
#import logging
#logging.basicConfig(level=logging.debug)
# debug:
# 1. print()把可能的变量打印出来
# 2. assert断言，出错后抛出异常. python -O 关闭assert
# 3. logging把异常输出到文件中
# 4. pdb 单步调试
import pdb
def foo(s):
    n = int(s)
    #print ('>>> n = %d'%n)
    #assert n != 0, 'n is zero!'
    #logging.info('n = %d'%n)
    pdb.set_trace()
    return 10/n
def main():
    foo('0')

main()
