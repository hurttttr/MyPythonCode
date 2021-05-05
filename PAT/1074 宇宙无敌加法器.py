N = list(map(int, input()))
for i in range(len(N)):
    if N[i] == 0:
        N[i] = 10
a = list(map(int, input()))
b = list(map(int, input()))
N.reverse()
a.reverse()
b.reverse()
la, lb = len(a), len(b)
i, f = 0, 0
ans = []
while(i < la or i < lb):
    if i < la and i < lb:
        t = a[i]+b[i]+f
    elif i < la:
        t = f+a[i]
    else:
        t = f+b[i]
    f, t = divmod(t, N[i])
    ans.append(t)
    i += 1
if f != 0:
    ans.append(f)
ans.reverse()
print(int(''.join(str(x)for x in ans)))
