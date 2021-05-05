n = input()
P = n.count('P')
A = n.count('A')
T = n.count('T')
e = n.count('e')
s = n.count('s')
t = n.count('t')
while P or A or T or e or s or t:
    if P != 0:
        print('P', end='')
        P -= 1
    if A != 0:
        print('A', end='')
        A -= 1
    if T != 0:
        print('T', end='')
        T -= 1
    if e != 0:
        print('e', end='')
        e -= 1
    if s != 0:
        print('s', end='')
        s -= 1
    if t != 0:
        print('t', end='')
        t -= 1
print()
