# -*- coding:utf-8 -*-
import functools

def _log(*test):
    def _decorator(func):
        def _wrapper(*args,**kw):
            print('%s %s():' %(test,func.__name__))
            return func(*args,**kw)
        return _wrapper
    return _decorator

@_log('name:')
def f():
    print('test')

f()
