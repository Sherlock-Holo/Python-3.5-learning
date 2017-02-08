a = [1,5,10,10,5,1]
b = []
x = 0
print(a)
while x <= (len(a) - 2):
    if b == []:
        b.append(1)
    c = a[x] + a[x + 1]
    b.append(c)
    x = x + 1
b.append(1)
print(b)
