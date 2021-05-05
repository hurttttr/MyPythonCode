P, M, N = map(int, input().split())
dic = {}
cnt = P+N+M
for i in range(cnt):
    xh, grade = input().split()
    if i < P:
        dic[xh] = [xh, int(grade), -1, -1, 0]
    elif i < P+M:
        if xh not in dic:
            dic[xh] = [xh, -1, int(grade), -1, 0]
        else:
            dic[xh][2] = int(grade)
    else:
        if xh not in dic:
            dic[xh] = [xh, -1, -1, int(grade), 0]
        else:
            dic[xh][3] = int(grade)
lst = []
for i in dic:
    if dic[i][1] >= 200:
        if dic[i][2] > dic[i][3]:
            dic[i][4] = int(0.4*dic[i][2]+0.6*dic[i][3]+0.5)
        else:
            dic[i][4] = dic[i][3]
        if dic[i][4] >= 60:
            lst.append(dic.get(i))
lst.sort(key=lambda x: (-x[4], x[0]))
for i in lst:
    print('%s %d %d %d %d' % (i[0], i[1], i[2], i[3], i[4]))
