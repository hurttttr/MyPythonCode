N, K = map(int, input().split())
lst = [input().split()for i in range(N)]
lst.sort(key=lambda x: (-int(x[1]), x[0]))
for i in range(K):
    if i == 0:
        t = N//K+N % K
    else:
        t = N//K
    rst = []
    if t % 2 == 0:
        for j in range(t):
            if j % 2 == 0:
                rst.append(lst.pop(0)[0])
            else:
                rst.insert(0, lst.pop(0)[0])
    else:
        rst.append(lst.pop(0)[0])
        for j in range(t-1):
            if j % 2 == 0:
                rst.insert(0, lst.pop(0)[0])
            else:
                rst.append(lst.pop(0)[0])
    print(' '.join(rst))
