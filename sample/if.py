#!/usr/bin/python
age = input("please your age: ")
age = int(age)
if age > 20:
    print ("You'r adult")
elif age > 10:
    print ("you'r teenager")
elif age > 6:
    print ("you'r kid")
else:
    print ("you'r baby")
