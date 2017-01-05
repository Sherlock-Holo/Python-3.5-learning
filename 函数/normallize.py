# -*- coding:utf-8 -*-

def normallize(bad_str):
    
    def bad2normal(n):
        return n.lower()

    return list(map(bad2normal,bad_str))
