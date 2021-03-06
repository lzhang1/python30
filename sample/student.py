#!/usr/bin/python
# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    
    def print_info(self):
        print ("Name:%s Score:%s"%(self.__name,self.__score))
    
    def get_grade(self):
        if self.__score > 90:
            return 'A'
        elif self.__score > 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

if __name__ == "__main__":
    A = Student("Michael",80)
    B = Student("Mike",100)
    A.print_info()
    B.print_info()
    print (A.get_grade())
