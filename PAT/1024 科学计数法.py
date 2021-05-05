a, b = input().split('E')
if a[0] == '-':
    print('-', end='')
t = ''.join(a[1:].split('.'))
n = int(b)
if n < 0:
    print('0.'+'0'*(-n-1)+t)
else:
    if n < len(t)-1:
        for i in range(n+1):
            print(t[i], end='')
        print('.'+t[n+1:])
    else:
        print(t+'0'*(n-len(t)+1))
