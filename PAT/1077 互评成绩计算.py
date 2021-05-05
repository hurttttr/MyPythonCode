N, M = map(int, input().split())
for i in range(N):
    t = list(map(int, input().split()))
    a = []
    for j in t[1:]:
        if 0 <= j <= M:
            a.append(j)
    g2 = (sum(a)-max(a)-min(a))/(len(a)-2)
    g = (t[0]+g2)/2+0.5
    print(int(g))
