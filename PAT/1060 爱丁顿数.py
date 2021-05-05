N = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
ans = 0
for i in range(N):
    if lst[i] > i+1:
        ans += 1
print(ans)
