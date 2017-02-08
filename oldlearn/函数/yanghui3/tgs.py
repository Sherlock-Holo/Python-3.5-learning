# -*- coding:utf-8 -*-

def tgs(cs):
    b = []
    x = 0
    while x <= (len(cs) - 2):
        if b == []:
            b.append(1)
        b.append(cs[x] + cs[x + 1])
        x = x + 1
    b.append(1)
    print(b)
