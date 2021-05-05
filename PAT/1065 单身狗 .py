import sys

N = int(input())
cp = [sys.stdin.readline().split()for i in range(N)]
M = int(input())
lst = set(sys.stdin.readline().split())
for i in cp:
    if i[0] in lst and i[1] in lst:
        lst.remove(i[0])
        lst.remove(i[1])
cnt = len(lst)
print(cnt)
if cnt != 0:
    print(' '.join(sorted(lst)))
