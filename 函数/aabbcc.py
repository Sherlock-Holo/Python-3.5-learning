# coding:utf-8
import math

def jie(a,b,c):
    s= b * b - 4 * a * c
    if s >= 0:        # 进行是否有根判断
        s1 = (-b + math.sqrt(s)) / (2 * a)
        s2 = (-b - math.sqrt(s)) / (2 * a)
        return s1,s2
    else:
        print('方程无解')
