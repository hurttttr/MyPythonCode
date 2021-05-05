'''
import sys

N, e, D = map(eval, input().split())
lst = [list(map(eval, sys.stdin.readline().split())) for i in range(N)]
maybeempty = empty = 0
for i in lst:
    f = 0
    for j in i[1:]:
        if j < e:
            f += 1
    if f > i[0]/2 and i[0] <= D:
        maybeempty += 1
    if f > i[0]/2 and i[0] > D:
        empty += 1
print('%.1f%% %.1f%%' % (maybeempty/N*100, empty/N*100))
'''
N, e, D = input().split()
N, e, D, maybeempty, empty = int(N), float(e), int(D), 0, 0
for i in range(N):
    t = input().split()
    count = 0
    for j in t[1:]:
        if float(j) < e:
            count += 1
    if count > int(t[0])//2:
        if int(t[0]) > D:
            empty += 1
        else:
            maybeempty += 1
print('%.1f%% %.1f%%' % (maybeempty/N*100, empty/N*100))
