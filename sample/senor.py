#!/usr/bin/python
L = (x*x for x in range(10))
for n in L:
    print (n)

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        n = n + 1
        #print (b)
        yield b
        a,b = b,a+b
    return 'done'

for n in fib(8):
    print (n)
