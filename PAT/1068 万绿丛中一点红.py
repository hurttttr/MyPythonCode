def judge(i, j, M, N, TOL):
    global lst
    dir = [[-1, 0], [-1, 1], [-1, -1], [0, 1],
           [0, -1], [1, 0], [1, -1], [1, 1]]
    for k in range(8):
        tx = i+dir[k][0]
        ty = j+dir[k][1]
        if 0 <= tx < N and 0 <= ty < M and abs(lst[i][j]-lst[tx][ty]) <= TOL:
            return False
    return True


M, N, TOL = map(int, input().split())
lst = [list(map(int, input().split()))for i in range(N)]
t = {}
for i in range(N):
    for j in range(M):
        t[lst[i][j]] = t.get(lst[i][j], 0)+1
x, y = 0, 0
cnt = 0
for i in range(0, N):
    for j in range(0, M):
        if t[lst[i][j]] != 1:
            continue
        if judge(i, j, M, N, TOL):
            cnt += 1
            x = i+1
            y = j+1
            if cnt > 1:
                break
    if cnt > 1:
        break
if cnt == 0:
    print('Not Exist')
elif cnt > 1:
    print('Not Unique')
else:
    print('(%d, %d): %d' %
          (y, x, lst[x-1][y-1]))
