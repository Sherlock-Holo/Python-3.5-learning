def my_abs(x):        # 定义一个函数叫做my_abs
    if not isinstance(x,(int,float)):        # 对输入参数进行类型检查
        raise TypeError('参数错误')
    if x >= 0:        # 从这里开始到下面是函数的主体
        return x
    else:
        return -x
