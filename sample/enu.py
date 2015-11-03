#!/usr/bin/python
# -*- coding: utf-8 -*-
from enum import Enum,unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fir = 5
    Sat = 6

for name, member in Month.__members__.items():
    print (name, '=>', member, ',', member.value)

print ("="*30)
for name, member in Weekday.__members__.items():
    print (name, '=>', member, ',', member.value)
