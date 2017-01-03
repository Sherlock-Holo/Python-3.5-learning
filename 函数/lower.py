# -*- coding: utf-8 -*-

L1 = ['Hello','World',18,'Apple',None]
L2 = []

for i,x in enumerate(L1):
    if isinstance(x,str) == False:
        L1.pop(i)

print([s.lower() for s in L1])
