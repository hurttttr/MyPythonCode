import sys

n, p = map(int, input().split())
l = [int(x) for x in sys.stdin.readline().split()]
l.sort()
m = 0
for i in range(n):
    min_p = l[i]*p
    end = i+m
    if end >= n:
        break
    for j in range(end, n):
        if l[j] <= min_p:
            m += 1
        else:
            break
print(m)
