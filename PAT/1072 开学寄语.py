N, M = map(int, input().split())
lst = input().split()
pnum, onum = 0, 0
for i in range(N):
    t = input().split()
    ms = []
    for i in t[2:]:
        if i in lst:
            ms.append(i)
            onum += 1
    if len(ms) > 0:
        print('{}: {}'.format(t[0], ' '.join(ms)))
        pnum += 1
print(pnum, onum)
