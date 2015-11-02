#!/usr/bin/python 
<<<<<<< HEAD
# -*- coding: utf-8 -*-
def triangle(cell):
    li = [([0]*cell) for i in range(cell)]
    print (li)
=======

def triangle(cell):
    li = [([0]*cell) for i in range(cell)]
>>>>>>> c9567d881ab593db8a0608dd06a5b1911f7c6a4a
    for i in range(cell):
        for j in range(i+1):
            if i == 0 or j == 0 or j == i:
                li[i][j] = 1
            else:
                li[i][j] = li[i-1][j-1] + li[i-1][j]
    return li
<<<<<<< HEAD
if __name__ == "__main__":
    print ("期待输出：")
    cell = input("Please input your cell: ")
    cell = int(cell)
    listcell = triangle(cell)
    for i in range(cell):
        print (listcell[i][:i+1])
=======
print ("期待输出：")
cell = input("Please input your cell: ")
cell = int(cell)
listcell = triangle(cell)
for i in range(cell):
    print (listcell[i][:i+1])
>>>>>>> c9567d881ab593db8a0608dd06a5b1911f7c6a4a
