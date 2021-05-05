M, N, A, B, T = map(int, input().split())
for i in range(M):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if A <= tmp[j] <= B:
            tmp[j] = T
    print(' '.join('{:03}'.format(x)for x in tmp))
