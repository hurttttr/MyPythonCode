import sys


def fun(a, b, c):
    if max(a, b, c) == a:
        return 'B'
    elif max(a, b, c) == b:
        return 'C'
    else:
        return 'J'


n = int(sys.stdin.readline())
l = [[x for x in sys.stdin.readline().split()]for i in range(n)]
a = [0, 0, 0, 0, 0, 0]  # 胜负平布锤剪
b = [0, 0, 0, 0, 0, 0]

for i in l:
    if i[0] == 'B':
        if i[1] == 'C':
            a[0] += 1
            a[3] += 1
            b[1] += 1
        elif i[1] == 'J':
            a[1] += 1
            b[0] += 1
            b[5] += 1
        else:
            a[2] += 1
            b[2] += 1
    elif i[0] == 'C':
        if i[1] == 'B':
            a[1] += 1
            b[0] += 1
            b[3] += 1
        elif i[1] == 'C':
            a[2] += 1
            b[2] += 1
        else:
            a[0] += 1
            a[4] += 1
            b[1] += 1
    else:
        if i[1] == 'B':
            a[0] += 1
            a[5] += 1
            b[1] += 1
        elif i[1] == 'C':
            a[1] += 1
            b[0] += 1
            b[4] += 1
        else:
            a[2] += 1
            b[2] += 1
sys.stdout.write('%d %d %d\n' % (a[0], a[2], a[1]))
sys.stdout.write('%d %d %d\n' % (b[0], b[2], b[1]))
sys.stdout.write('%c %c\n' % (fun(a[3], a[4], a[5]), fun(b[3], b[4], b[5])))
