# coding:utf-8

L = []

def lists(n):
    while n > 0:
        if n % 5 == 0:
            L.insert(0,n)
        n = n - 1
a = input('输入数字: ')
a = int(a)
lists(a)
print(L)
