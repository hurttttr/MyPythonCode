def translate(a, b, c):
    l = []
    ans = a+b
    if ans == 0:
        return ['0']
    while ans != 0:
        t = ans % c
        l.append(str(t))
        ans = ans//c
    l.reverse()
    return l


n = [int(x) for x in input().split()]
print(''.join(translate(n[0], n[1], n[2])))
