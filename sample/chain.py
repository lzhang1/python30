#!/usr/bin/python
# -*- coding: utf-8 -*-
class Chain(object):

    def __init__(self,path=""):
        self._path = path

    def __getattr__(self,path):
        return Chain('%s/%s'%(self._path,path))

    def __str__(self):
        return self._path

if __name__=="__main__":
    print (Chain().users('michael').repos)
