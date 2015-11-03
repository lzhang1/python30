#!/usr/bin/python
# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)'% self.name

if __name__ == "__main__":
    print (Student('Michael'))
