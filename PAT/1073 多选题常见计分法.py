def fun(t):
    rst = []
    for i in range(t):
        if t[i] == '(':
            k = i
        elif t[i] == ')':
            rst.append(t[k+1:i])
    return rst


N, M = map(int, input().split())
rightans = [input().split()for i in range(M)]
wrong = [0]*M
for i in range(N):
    t = fun(input())
    for j in range(M):
        if
