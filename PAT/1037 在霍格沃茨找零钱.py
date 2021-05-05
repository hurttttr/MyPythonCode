def fun(p, a):
    if p[2] <= a[2]:
        k = a[2]-p[2]
    else:
        k = a[2]+29-p[2]
        a[1] -= 1
    if p[1] <= a[1]:
        s = a[1]-p[1]
    else:
        s = a[1]+17-p[1]
        a[0] -= 1
    g = a[0]-p[0]
    print('%d.%d.%d' % (g, s, k))


p, a = [x for x in input().split()]
p = [int(x) for x in p.split('.')]
a = [int(x) for x in a.split('.')]
if p[0] > a[0] or (p[0] == a[0] and p[1] > a[1]) or (p[0] == a[0] and p[1] == a[1] and p[2] > a[2]):
    print('-', end='')
    fun(a, p)
else:
    fun(p, a)
