#!/usr/bin/python
# -*- coding: utf-8 -*-
def normalize(name):
    return name.capitalize()

if __name__ == "__main__":
    L1 = ["adam","LISA","BAr"]
    L2 = list(map(normalize, L1))
    print (L1)
    print (L2)
