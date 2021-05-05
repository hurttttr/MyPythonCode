n, m = map(int, input().split())
l = [x for x in input().split()]
for i in range(m % n):
    l.insert(0, l.pop())
print(' '.join(l))
