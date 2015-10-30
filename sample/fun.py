#!/usr/bin/python
def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print ('name:',name,'age:',age,'other:',kw)
person('Michael',30)
person('Bob',35,city='Beijing')
person('Jack',24,city='Beijing',addr='Chaoyang')

def f1(a,b,c=0,*args,**kw):
    print ('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
    print ('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

#位置参数(必选参数、默认参数）,可变参数,关键字参数和命名关键字参数
 
f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f2(1,2,d=99,ext=None)
args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)
args=(1,2,3)
kw={'d':88,'x':'#'}
#f2(*args,**kw)
