#!/usr/bin/python 

def triangle(cell):
    li = [([0]*cell) for i in range(cell)]
    for i in range(cell):
        for j in range(i+1):
            if i == 0 or j == 0 or j == i:
                li[i][j] = 1
            else:
                li[i][j] = li[i-1][j-1] + li[i-1][j]
    return li
print ("期待输出：")
cell = input("Please input your cell: ")
cell = int(cell)
listcell = triangle(cell)
for i in range(cell):
    print (listcell[i][:i+1])
