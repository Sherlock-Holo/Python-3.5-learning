# -*- coding:utf-8 -*-

# 判断是否是回数
def _huishu(n):
    n = str(n)
    length = len(n)
    _out = ''
    l = -1
    # 将输入数字作调转处理
    while l >= (-length):
        _out = _out + str(n[l])
        l = l - 1
    _out = int(_out)
    return _out == int(n)

x = int(input('起始:'))
y = int(input('结尾:')) + 1

_output = filter(_huishu,range(x,y))
print(list(_output))
