M, N, S = map(int, input().split())
lst = []
cnt = N-1
for i in range(0, M):
    t = input()
    S -= 1
    if S > 0:
        continue
    cnt += 1
    if N == cnt:
        if t not in lst:
            lst.append(t)
            cnt = 0
        else:
            cnt -= 1
if len(lst) == 0:
    print('Keep going...')
else:
    for i in lst:
        print(i)
