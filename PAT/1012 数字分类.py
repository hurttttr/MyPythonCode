n = [int(x) for x in input().split()]
a = [0, 0, 0, 0, 0]
a1_f = 0
a3_f = 0
for index, i in enumerate(n):
    if index == 0:
        continue
    if i % 10 == 0:
        a[0] += i
    if i % 5 == 1:
        a[1] += (-1)**a1_f*i
        a1_f += 1
    if i % 5 == 2:
        a[2] += 1
    if i % 5 == 3:
        a[3] += i
        a3_f += 1
    if i % 5 == 4 and i > a[4]:
        a[4] = i
for index, i in enumerate(a):
    if index != 0:
        print(' ', end='')
    if i != 0 and index != 1:
        if index == 3:
            print('%.1f' % (a[3]/a3_f), end='')
        else:
            print(i, end='')
    elif index == 1:
        if a1_f != 0 or i != 0:
            print(i, end='')
        else:
            print('N', end='')
    else:
        print('N', end='')
print()
