# -*- coding;utf-8 -*-

class Student(object):
    def __init__(self,name,sorce):
        self.__name = name
        self.__sorce = sorce

    def print_source(self):
        print('%s: %s' %(self.__name,self.__sorce))

    def set_sorce(self,sorce):
        self.__sorce = sorce
