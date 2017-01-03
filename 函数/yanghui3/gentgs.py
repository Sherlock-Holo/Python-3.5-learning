# -*- coding:utf-8 -*-

a = [1]
n = 1

def tgs(cs):
    if n == 1:        # 如果是1则输出[1]
        print(a)
        a = [1,1]
    elif n == 2:        # 如果是2则输出[1,1]
        print(aa)
    else:        # 开始生成杨辉三角
        b = []
        x = 0
        while x <= (len(cs) - 2):
            if b == []:
                b.append(1)
            b.append(cs[x] + cs[x + 1])
            x = x + 1
        b.append(1)
        aa = b
    n = n + 1
    yield(b)

while n <= 10:
    tgs(a)
