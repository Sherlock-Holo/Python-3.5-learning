def _huishu(n):
    n = str(n)
    length = len(n)
    _out = ''
    l = -1
    while l >= length:
        _out = _out + n[-1]
        l = l - 1
    _out = int(_out)
    return _out
