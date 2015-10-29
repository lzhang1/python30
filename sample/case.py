#!/usr/bin/python
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
def calc(type, x, y):
    calculation = {
            '+':lambda:add(x,y),
            '-':lambda:sub(x,y),
            '*':lambda:multi(x,y),
            '/':lambda:div(x,y),
            }
    return calculation[type]()

result1 = calc('+',3,6)
result2 = calc('-',3,6)
print ("result1:",result1)
print ("result2:",result2)
