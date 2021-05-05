passwd, N = input().split()
N = int(N)
while True:
    t = input()
    if t == '#':
        break
    if t == passwd:
        print('Welcome in')
        break
    else:
        print('Wrong password: %s' % t)
    N -= 1
    if N == 0:
        print('Account locked')
        break
