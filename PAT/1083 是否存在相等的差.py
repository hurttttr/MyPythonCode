from collections import Counter

N = int(input())
lst = list(map(int, input().split()))
ans = []
for i in range(N):
    ans.append(abs(i+1-lst[i]))
s = Counter(ans)
rst = []
for i in s:
    rst.append([i, s[i]])
rst.sort(key=lambda x: x[0], reverse=True)
for i in rst:
    if i[1] > 1:
        print(i[0], i[1])
