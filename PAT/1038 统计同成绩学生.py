import sys

n = int(input())
lst = [int(x) for x in sys.stdin.readline().split()]
findlist = [int(x) for x in sys.stdin.readline().split()]
a = [0]*101
for i in lst:
    a[i] += 1
s = []
for i in findlist[1:]:
    s.append(str(a[i]))
print(' '.join(s))
