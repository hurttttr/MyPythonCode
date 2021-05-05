N, M = map(int, input().split())
value = list(map(int, input().split()))
rightans = list(map(str, input().split()))
for i in range(N):
    ans = 0
    t = list(map(str, input().split()))
    for j in range(M):
        if t[j] == rightans[j]:
            ans += value[j]
    print(ans)
