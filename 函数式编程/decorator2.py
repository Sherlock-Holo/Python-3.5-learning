# -*- coding:utf-8 -*-

def _log(func):
    def _wrapper(*args,**kw):
        print('begin call: %s' %(func.__name__))
        _out = 'end call'
        return func(*args,**kw),_out
    return _wrapper

@_log
def test():
    print('test')

test()
