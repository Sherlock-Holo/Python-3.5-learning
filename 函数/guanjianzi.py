# coding:utf-8

def person(name,age,**qt):        # **qt就是关键字的意思，而使用时是相当于插入一个或多个dict，例如grade='Dayi'
    print('name:',name,'age:',age,'other:',qt)
