d, N = map(int, input().split())
if N == 1:
    print(d)
else:
    ans = [d, 1]
    for i in range(2, N):
        t = []
        num = 1
        for j in range(len(ans)-1):
            if ans[j] == ans[j+1]:
                num += 1
            else:
                t.append(ans[j])
                t.append(num)
                num = 1
        t.append(ans[j+1])
        t.append(num)
        ans = t
    print(''.join(str(x)for x in ans))
