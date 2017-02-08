# -*- coding:utf8 -*-

def tgs(cs):
    max = len(cs) - 2        # 读取输入的list的长度并且-2为接下来计算做准备
    if len(cs) == 1:        # 如果list长度为1,就生成一个2长度的
        cs.append(cs[0])
        print(cs)
    else:
        n = 0
        b = [cs[0]]
        while n <= max:
            b.append(cs[n] + cs[n + 1])
            n = n + 1
        b.append(cs[-1])
        print(b)

