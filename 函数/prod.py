# -*- coding:utf-8 -*-

# 将输入的序列数字类乘
def prod(intp):

    from functools import reduce

    def lei_cheng(x,y):        # 本体(疑惑?
        return x * y

    return reduce(lei_cheng,intp)
