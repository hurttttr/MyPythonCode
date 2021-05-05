import sys

strat, N, K = map(int, sys.stdin.readline().split())
data = [0 for i in range(100005)]
next = [0 for j in range(100005)]
lst = [[] for j in range(100005)]
num = 0
for i in range(N):
    a, b, c, = map(int, sys.stdin.readline().split())
    data[a] = b
    next[a] = c
while strat != -1:
    lst[num] = [strat, data[strat], next[strat]]
    num += 1
    strat = next[strat]
a = [[] for j in range(num)]
b = [[] for j in range(num)]
c = [[] for j in range(num)]
la, lb, lc = 0, 0, 0
for i in range(num):
    if lst[i][1] < 0:
        a[la] = lst[i]
        la += 1
    elif 0 <= lst[i][1] <= K:
        b[lb] = lst[i]
        lb += 1
    else:
        c[lc] = lst[i]
        lc += 1
if la > 0:
    for i in range(la-1):
        sys.stdout.write('%05d %d %05d\n' % (a[i][0], a[i][1], a[i+1][0]))
    if lb > 0:
        sys.stdout.write('%05d %d %05d\n' % (a[la-1][0], a[la-1][1], b[0][0]))
    elif lc > 0:
        sys.stdout.write('%05d %d %05d\n' % (a[la-1][0], a[la-1][1], c[0][0]))
    else:
        sys.stdout.write('%05d %d -1\n' % (a[la-1][0], a[la-1][1]))
if lb > 0:
    for i in range(lb-1):
        sys.stdout.write('%05d %d %05d\n' % (b[i][0], b[i][1], b[i+1][0]))
    if lc > 0:
        sys.stdout.write('%05d %d %05d\n' % (b[lb-1][0], b[lb-1][1], c[0][0]))
    else:
        sys.stdout.write('%05d %d -1\n' % (b[lb-1][0], b[lb-1][1]))
if lc > 0:
    for i in range(lc-1):
        sys.stdout.write('%05d %d %05d\n' % (c[i][0], c[i][1], c[i+1][0]))
    sys.stdout.write('%05d %d -1\n' % (c[lc-1][0], c[lc-1][1]))
