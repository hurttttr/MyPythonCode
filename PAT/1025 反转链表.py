import sys

strat, n, m = map(int, input().split())
data = [0 for i in range(100005)]
next = [0 for j in range(100005)]
list = [0 for zi in range(100005)]
for i in range(n):
    a, b, c, = map(int, sys.stdin.readline().split())
    data[a] = b
    next[a] = c
sum = 0
while strat != -1:
    list[sum] = strat
    sum += 1
    strat = next[strat]
for i in range(0, sum-sum % m, m):
    list[i:i+m] = reversed(list[i:i+m])
for i in range(sum-1):
    print('%05d %d %05d' % (list[i], data[list[i]], list[i+1]))
print('%05d %d -1' % (list[sum - 1], data[list[sum - 1]]))
