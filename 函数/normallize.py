# -*- coding:utf-8 -*-

def normallize(bad_str):        # 函数将不规范的大小写转换为全小写
    
    def bad2normal(n):        # 调取.lower()来转换
        return n.lower()

    return list(map(bad2normal,bad_str))        # 转换
