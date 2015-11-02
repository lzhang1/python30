#!/usr/bin/python
# -*- coding: utf-8 -*-
names = ["Michael","Bob","Tracy"]
scores = [95,75,85]
d = {}
for i in range(3):
    d[names[i]] = scores[i]
print ("Initial Dict: ",d)
c = d.copy()
if 'Bob' in d:
    print ("Scores of Bob",d['Bob'])
d['Ray'] = 100
print ("Updated Dict: ",d)
del(d["Tracy"])
print ("Updated Dict: ",d)
d.pop("Michael")
print ("Updated Dict: ",d)
d.clear()
print ("Cleard Dict: ",d)

for k in c:
    print ("d[%s] = %s"%(k,c[k]))
print (c)
for key, value in c.items():
    print ("c[%s]="%key,value)

print (c)
for key, value in c.iteritems():
    print ("c[%s]="%key,value)
