N, M = map(int, input().split())
lst = [0]*N
for i in range(M):
    t = list(map(int, input().split()))
    for j in range(N):
        lst[j] += t[j]
print(max(lst))
ans = []
for i in range(N):
    if lst[i] == max(lst):
        ans.append(i+1)
print(' '.join(str(x) for x in ans))
