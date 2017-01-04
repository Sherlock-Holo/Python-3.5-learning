# -*- coding:utf-8 -*-

def str2int(i):

    from functools import reduce        # 导入reduce

    def fn(x,y):
        return 10 * x + y        #将list里面的各个数字组合成一个

    def char2int(n):
        number = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        return number[n]

    inp =  list(map(char2int,i))        # 将输入的str序列转换为int序列

    print(reduce(fn,inp))        # 将int序列用fn函数组合成一个数
