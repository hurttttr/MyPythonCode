N = int(input())
lst = input().split()
s = set()
for i in range(N):
    s.add(sum(map(int, lst[i])))
print(len(s))
print(' '.join(str(x) for x in sorted(s)))
