n, m = map(int, input().split())
l = [1 for x in range(int(105000)+2)]
l[0] = l[1] = 0
for i in range(2, 105001):
    if l[i] == 1:
        for j in range(i*i, 105001, i):
            l[j] = 0
su = []
for i in range(2, 105001):
    if l[i] != 0:
        su.append(i)
count = 0
for i in range(n-1, m):
    print(su[i], end='')
    if i == m-1:
        print()
    elif (count+1) % 10 == 0:
        print()
    else:
        print(' ', end='')
    count += 1
