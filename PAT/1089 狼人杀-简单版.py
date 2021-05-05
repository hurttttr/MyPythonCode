N = int(input())
v = [0]
f = 0
for i in range(N):
    v.append(int(input()))
for i in range(1, N+1):
    for j in range(i+1, N+1):
        lie = []
        a = [1]*(N+1)
        a[i] = a[j] = -1
        for k in range(1, N+1):
            if v[k]*a[abs(v[k])] < 0:
                lie.append(k)
        if len(lie) == 2 and a[lie[0]]+a[lie[1]] == 0:
            print(i, j)
            f = 1
            break
    if f == 1:
        break
if f == 0:
    print('No Solution')
