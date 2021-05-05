def fun(a, b):
    if a > b:
        return 'Cong'
    elif a < b:
        return 'Gai'
    else:
        return 'Ping'


N, x, y = map(int, input().split())
for a in range(99, 10, -1):
    b = a % 10*10+a//10
    if abs(a-b)/x == b/y:
        print('{} {} {} {}'.format(a, fun(a, N), fun(b, N), fun(b/y, N)))
        break
else:
    print('No Solution')
