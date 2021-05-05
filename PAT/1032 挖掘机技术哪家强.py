import sys

n = int(input())
data = [0]*(n+1)
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    data[a] += b
t = max(data)
print(data.index(t), t)
