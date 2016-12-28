n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:        # %是取余数,这里是判断n除以2的余数是否是0
        continue        # 如果执行了continue，下面的print就不会执行
    print(n)
