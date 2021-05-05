N, M = map(int, input().split())
dic = {}
for i in range(N):
    a, b = input().split()
    dic[a] = dic.get(a, [])
    dic[a].append(b)
    dic[b] = dic.get(b, [])
    dic[b].append(a)
for i in range(M):
    f = 0
    t = input().split()
    for j in t[1:]:
        if j in dic:
            for k in dic[j]:
                if k in t:
                    f = 1
                    print('No')
                break
        if f == 1:
            break
    else:
        print('Yes')
