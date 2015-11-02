#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
for x in list(range(5)):
    print (x)

for key,value in os.environ.items():
    print ("key: ",key,"value: ",value)
