import sys


def fun(n):
    t = []
    for i, j in enumerate(n):
        if j == '(':
            k = i
        elif j == ')':
            t.append(n[k+1:i])
    return t


N, M = map(int, input().split())
lst = [sys.stdin.readline()for i in range(M)]
student = [sys.stdin.readline()for i in range(N)]
a = [0]*M
for i in student:
    ans = 0
    t = fun(i)
    for j in range(M):
        if t[j] == lst[j][4:-1]:
            ans += int(lst[j][0])
        else:
            a[j] += 1
    print(ans)
t = max(a)
if t == 0:
    print('Too simple')
else:
    print(t, end='')
    for i in range(M):
        if a[i] == t:
            print(' %d' % (i+1), end='')
