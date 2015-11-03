#!/usr/bin/python
# -*- coding: utf-8 -*-
class Student(object):
    
    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer")
        elif 0 <= value <= 100:
            self.__score = value
        else:
            raise ValueError('score must between 0 ~ 100')

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self,value):
        self.__birth = value

    @property
    def age(self):
        return 2015 - self.__birth

if __name__ == "__main__":
    s = Student()
    s.score = 60
    print (s.score)
    s.score = 9999
