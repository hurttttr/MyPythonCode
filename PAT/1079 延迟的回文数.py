def judeg(a):
    l = len(a)
    if a == '0':
        return True
    for i in range(0, l//2):
        if a[i] != a[l-1-i]:
            return False
    return True


N = input()
num = 0
if judeg(N):
    print('%s is a palindromic number.' % N)
else:
    for i in range(10):
        n = N[::-1]
        t = str(int(N)+int(n))
        print('{} + {} = {}'.format(N, n, t))
        if judeg(t):
            print('%s is a palindromic number.' % t)
            break
        N = t
    else:
        print('Not found in 10 iterations.')
