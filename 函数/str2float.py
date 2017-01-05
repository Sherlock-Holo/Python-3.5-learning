# -*- coding:utf-8 -*-

def str2float(s):

    from functools import reduce

    point = 0

    def num(char):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':-1}[char]

    def to_loat(x,y):
        
        nonlocal point
        
        if y == -1:
            point = 1
            return x

        if point == 0:
            return 10 * x + y
        else:
            point = 10 * point
            return x + y / point

    return reduce(to_loat,map(num,s))
