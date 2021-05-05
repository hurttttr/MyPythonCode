a = 1
b = []
for i in range(3, 60, 2):
    b.append(a)
    a += i*2
n, f = map(str, input().split())
n = int(n)
for i in range(30):
    if n < b[i]:
        break
ans = n-b[i-1]
for j in range(i, 0, -1):
    print((f*(j*2-1)).center(i*2-1).rstrip())
for j in range(1, i):
    print((f*(j*2+1)).center(i*2-1).rstrip())
print(ans)
